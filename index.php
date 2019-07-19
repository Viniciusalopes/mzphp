<?php
header('location: fora-do-ar.php');
require_once './bin/sessao.php';
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
        $urls = [];
        $packages = [];

        $doc = new DOMDocument();

        foreach ($_SESSION['mirrors_urls'] as $mirror) {
            $doc->loadHTMLFile($mirror->url);
            $tags = $doc->getElementsByTagName('a');

            # Diretórios do repositório

            foreach ($tags as $tag) {
                $url = (object) [
                            'mirror_name' => $mirror->name,
                            'mirror' => $mirror->url,
                            'folder' => ''
                ];
                if (strpos($tag->nodeValue, '/') !== FALSE) {
                    $url->folder = $tag->nodeValue;
                    $urls[] = $url;
                }
            }
        }
        $_SESSION['urls'] = $urls;

        # Packages, descs e sha256

        foreach ($urls as $url) {

            $doc->loadHTMLFile($url->mirror . $url->folder);
            $tags = $doc->getElementsByTagName('a');

            $filecsv = 'mz/mz_base.csv';
            if (file_exists($filecsv)) {
                # Remove o .desc atual
                shell_exec('rm -f ' . $filecsv);
            }
            
            foreach ($tags as $tag) {
                $package = (object) [
                            'repo' => $url->mirror_name,
                            'mirror' => $url->mirror,
                            'folder' => $url->folder,
                            'name' => '',
                            'version' => '',
                            'desc' => '',
                            'maintainer' => '',
                            'license' => '',
                            'url' => '',
                            'deps' => '',
                            'file_mz' => '',
                            'file_desc' => '',
                            'file_sha256' => ''
                ];

                $txt = explode('-', $tag->nodeValue);
                $len = strlen($tag->nodeValue);


                if (substr($tag->nodeValue, $len - 3) === '.mz') {
                    # Existe o .mz
                    $package->name = $txt[0];
                    $package->version = str_replace($package->name . '-', '', str_replace('.mz', '', $tag->nodeValue));
                    $package->file_mz = $tag->nodeValue;
                }

                if (substr($tag->nodeValue, $len - 5) === '.desc') {
                    # Existe o .desc
                    $package->file_desc = $tag->nodeValue;

                    # Verifica se já existe .desc local/servidor
                    $remote_file = $package->mirror . $package->folder . $package->file_desc;
                    $file = 'desc/' . $package->file_desc;
                    if (!file_exists($file)) {
                        # Download do .desc
                        shell_exec('curl -o ' . $file . ' ' . $remote_file);
                    }

                    # Detalhes do pacote
                    $txt = explode('|', str_replace("\"", "'", str_replace('==', '', str_replace('#', '|'
                                                    , explode('#####', explode('maintainer=', file_get_contents($file))[1])[0]))));

                    $package->maintainer = '[' . trim(str_replace("'", '', explode('<', $txt[0])[0])) . ']';
                    foreach ($txt as $key => $value) {
                        if (strpos($value, 'license=') !== FALSE) {
                            $package->license = '[' . trim(explode('license=', $txt[$key])[1]) . ']';
                        }
                        if (strpos($value, 'desc=') !== FALSE) {
                            $package->desc = '[' . trim(explode("'", (explode('desc=', $txt[$key])[1]))[1]) . ']';
                        }
                        if (strpos($value, 'url=') !== FALSE) {
                            $package->url = '[' . trim(explode("'", explode('url=', $txt[$key])[1])[1]) . ']';
                        }
                        if (strpos($value, 'dep=(') !== FALSE) {
                            $package->deps = '[' . trim(str_replace(')', '', explode('dep=(', $value)[1])) . ']';
                        }
                    }
                }

                if (substr($tag->nodeValue, $len - 7) === '.sha256') {
                    # Existe o .sha256
                    $package->file_sha256 = $tag->nodeValue;
                }

                # Constrói mz_base.csv
                $texto = $package->folder . ','
                        . $package->file_mz . ','
                        . $package->file_desc . ','
                        . $package->file_sha256;

                //Variável $fp armazena a conexão com o arquivo e o tipo de ação.
                $fp = fopen($filecsv, "a+");

                //Escreve no arquivo aberto.
                fwrite($fp, $texto);

                //Fecha o arquivo.
                fclose($fp);

                $packages[] = $package;
            }
        }
        $_SESSION['packages'] = $packages;
        if (count($pkgs) > 0) {
            #require 'html/tabela.php';
            echo 'pronto.';
        }
        ?>
        <!--            <div id="mussum-ipsun" class="text-justify">
                        <img src="img/mussum-ipsun.png" class="float-left" alt="Cacildis">
        <!--?php require_once './bin/etc.php' ?>
    </div>-->
    </div>
    <?php require './html/scripts.php' ?>
</body>
</html>
