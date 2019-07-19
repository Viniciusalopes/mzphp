<?php
if ($_SERVER['HTTP_HOST'] == 'vovolinux.com.br') {
    header('location: fora-do-ar.php');
    return;
}
require_once './bin/sessao.php';
$_SESSION['time'] = (object) [
            'inicius' => date('Yjd-h:i:s'),
            'fim' => NULL
];
//require_once './bin/Mirror.php';
//require_once './bin/Dir.php';
//require_once './bin/Package.php';
//require_once './bin/Os.php';
//$Os = new Os();
//try {
//    if (file_exists('var/lib/mz/mz_base.csv')) {
//        $packages = (new Package())->get_csv();
//    }
//} catch (Exception $exc) {
//    echo $exc->getTraceAsString();
//}
?>
<!DOCTYPE html>
<!--
A licença MIT

Copyright 2019 Viniciusalopes Tecnologia <suporte@viniciusalopes.com.br>.

É concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia
deste software e dos arquivos de documentação associados (o "Software"), para
negociar o Software sem restrições, incluindo, sem limitação, os direitos de uso,
cópia, modificação e fusão, publicar, distribuir, sublicenciar e/ou vender cópias
do Software, e permitir que as pessoas a quem o Software é fornecido o façam,
sujeitas às seguintes condições:

O aviso de copyright acima e este aviso de permissão devem ser incluídos em
todas as cópias ou partes substanciais do Software.

O SOFTWARE É FORNECIDO "NO ESTADO EM QUE SE ENCONTRA", SEM NENHUM TIPO DE GARANTIA,
EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
ADEQUAÇÃO A UM FIM ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUMA CIRCUNSTÂNCIA, OS AUTORES
OU PROPRIETÁRIOS DE DIREITOS DE AUTOR PODERÃO SER RESPONSABILIZADOS POR QUAISQUER
REIVINDICAÇÕES, DANOS OU OUTRAS RESPONSABILIDADES, QUER EM AÇÃO DE CONTRATO,
DELITO OU DE OUTRA FORMA, DECORRENTES DE, OU EM CONEXÃO COM O SOFTWARE OU O USO
OU OUTRAS NEGOCIAÇÕES NO PROGRAMAS.
------------------------------------------------------------------------------------------
Projeto   : mzphp
Criado em : 15/07/2019
Autor     : Viniciusalopes (Vovolinux) <suporte@vovolinux.com.br>
Finalidade: No início a terra era vazia e sem forma.
------------------------------------------------------------------------------------------
-->
<html lang="pt-BR">
    <head>
        <?php require_once 'html/head.php' ?>
    </head>

    <body>
        <?php require_once 'html/style.php' ?>
        <?php require_once 'html/menu.php' ?>
        <?php require_once 'html/subtitulo.php' ?>

        <?php
        try {


            $_SESSION['server'] = $_SERVER;
            $urls = [];
            $packages = [];

            $doc = new DOMDocument();

            foreach ($_SESSION['mirrors_urls'] as $mirror) {

                # filecsv
                $filecsv = $mirror->filecsv;

                if (file_exists($filecsv)) {
                    # Remove o .csv atual
                    shell_exec('rm -f ' . $filecsv);
                }

                $doc->loadHTMLFile($mirror->url);
                $tags = $doc->getElementsByTagName('a');

                # Diretórios do repositório
                foreach ($tags as $tag) {
                    $url = (object) [
                                'mirror_name' => $mirror->name,
                                'mirror_dirlib' => $mirror->dirlib,
                                'mirror_filecsv' => $mirror->filecsv,
                                'mirror' => $mirror->url,
                                'folder' => ''
                    ];
                    if (strpos($tag->nodeValue, '/') !== FALSE) {
                        $url->folder = $tag->nodeValue;
                        $urls[] = $url;
                    }
                } // foreach tags de urls
                $_SESSION['urls'] = $urls;
            } // foreach mirrors
            #
        ## Packages, descs e sha256
            foreach ($urls as $url) {

                $doc->loadHTMLFile($url->mirror . $url->folder);
                $tags = $doc->getElementsByTagName('a');

                foreach ($tags as $tag) {
//                if (count($packages) >= 1) {
//                    break;
//                }
                    $txt = explode('-', $tag->nodeValue);
                    $len = strlen($tag->nodeValue);


                    if (substr($tag->nodeValue, $len - 3) === '.mz') {
                        
                        if(file_exists($url->mirror_dirlib))
                        
                        # Existe o .mz
                        $package = (object) [
                                    'repo' => $url->mirror_name,
                                    'mirror' => $url->mirror,
                                    'dirlib' => $url->mirror_dirlib,
                                    'filecsv' => $url->mirror_filecsv,
                                    'folder' => $url->folder,
                                    'name' => $txt[0],
                                    'version' => str_replace($txt[0] . '-', '', str_replace('.mz', '', $tag->nodeValue)),
                                    'maintainer' => '',
                                    'license' => '',
                                    'url' => '',
                                    'deps' => '',
                                    'file_mz' => $tag->nodeValue,
                                    'file_desc' => $tag->nodeValue . '.desc',
                                    'file_sha256' => $tag->nodeValue . '.sha256',
                                    'desc' => ''
                        ];

                        # Constrói mz_base.csv
                        $texto = $package->folder . ','
                                . $package->file_mz . ','
                                . $package->file_desc . ','
                                . $package->file_sha256;
                        shell_exec("echo \"" . $texto . "\" >> " . $package->filecsv);

                        # Inclui o package na lista
                        $packages[] = $package;
                    } // if existe .mz no repositório
                } // foreach tags
            } // foreach urls

            foreach ($packages as $package) {

                # Verifica se já existe .desc local/servidor
                $remote_file = $package->mirror . $package->folder . $package->file_desc;
                $dirlib = $package->dirlib;
                $file = $dirlib . 'desc/' . $package->file_desc;
                if (!file_exists($file)) {
                    # Download do .desc
                    $curl = 'curl -o ' . $file . ' ' . $remote_file;
                    shell_exec($curl);
                }

                # obtém o arquivo package.desc
                $file_desc = file_get_contents($file);

                if (strpos($file_desc, "<title>File Not Found</title>") === FALSE) {

                    # Detalhes do pacote
                    $txt = explode('|', str_replace("\"", "'", str_replace('==', '', str_replace('#', '|'
                                                    , explode('#####', explode('maintainer=', $file_desc)[1])[0]))));

                    $package->maintainer = trim(str_replace("'", '', explode('<', $txt[0])[0]));
                    foreach ($txt as $key => $value) {
                        if (strpos($value, 'license=') !== FALSE) {
                            $package->license = trim(explode('license=', $txt[$key])[1]);
                        }
                        if (strpos($value, 'desc=') !== FALSE) {
                            $package->desc = trim(explode("'", (explode('desc=', $txt[$key])[1]))[1]);
                        }
                        if (strpos($value, 'url=') !== FALSE) {
                            $package->url = trim(explode("'", explode('url=', $txt[$key])[1])[1]);
                        }
                        if (strpos($value, 'dep=(') !== FALSE) {
                            $package->deps = trim(str_replace(')', '', explode('dep=(', $value)[1]));
                        }
                    }
                }
            } //foreach packages

            $_SESSION['packages'] = $packages;
            if (count($packages) > 0) {
                #require 'html/tabela.php';
                echo 'pronto.';
            }
            ?>
            <!--div id="mussum-ipsun" class="text-justify">
                <img src="img/mussum-ipsun.png" class="float-left" alt="Cacildis">
            <?php #require_once './bin/etc.php'  ?>
            </div-->

            <?php require_once './bin/sessao.php' ?>
            <?php
        } catch (Exception $exc) {
            echo $exc->getTraceAsString();
        }
        ?>
    </body>
</html>
<?php
$_SESSION['time']->fim = date('Yjd-h:i:s');
