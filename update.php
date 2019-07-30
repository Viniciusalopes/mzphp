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
            $novos_pacotes = 0;
            $doc = new DOMDocument();

            foreach ($_SESSION['repositorios'] as $repo) {

                $doc->loadHTMLFile($repo->url);
                $tags = $doc->getElementsByTagName('a');

                # Diretórios do repositório
                foreach ($tags as $tag) {
                    $url = (object) [
                                'repo_name' => $repo->name,
                                'repo_dirlib' => $repo->dirlib,
                                'repo_url' => $repo->url,
                                'folder' => ''
                    ];
                    if (strpos($tag->nodeValue, '/') !== FALSE) {
                        $url->folder = $tag->nodeValue;
                        $urls[] = $url;
                    }
                } // foreach tags de urls
                $_SESSION['urls'] = $urls;
            } // foreach repositorios
            #
            
            ## Packages, descs e sha256
            foreach ($urls as $url) {

                $doc->loadHTMLFile($url->repo_url . $url->folder);
                $tags = $doc->getElementsByTagName('a');

                foreach ($tags as $tag) {

                    $txt = explode('-', $tag->nodeValue);
                    $len = strlen($tag->nodeValue);

                    if (substr($tag->nodeValue, $len - 3) === '.mz') {
                        # Existe o .mz no repositório
                        $repo_dirlib = $url->repo_dirlib;
                        $file_desc = $tag->nodeValue . '.desc';
                        $file_json = $tag->nodeValue . '.json';
                        if (file_exists($repo_dirlib . '/json' . $file_json)) {
                            # Inclui o package na lista
                            $packages[] = json_decode($repo_dirlib . '/json' . $file_json);
                        } else {
                            # Existe o .mz mas não existe o .json
                            $novos_pacotes ++;
                            $package = (object) [
                                        'repo_name' => $url->repo_name,
                                        'repo_url' => $url->repo_url,
                                        'repo_dirlib' => $repo_dirlib,
                                        'folder' => $url->folder,
                                        'name' => $txt[0],
                                        'version' => str_replace($txt[0] . '-', '', str_replace('.mz', '', $tag->nodeValue)),
                                        'maintainer' => '',
                                        'license' => '',
                                        'url' => '',
                                        'deps' => '',
                                        'file_mz' => $tag->nodeValue,
                                        'file_desc' => $file_desc,
                                        'file_sha256' => $tag->nodeValue . '.sha256',
                                        'file_json' => $file_json,
                                        'desc' => ''
                            ];

                            # Download do .desc
                            $remote_file = $url->repo_url . $url->folder . $file_desc;
                            $local_file = '/tmp/' . $file_desc;
                            if (!file_exists($local_file)) {
                                # obtém o arquivo package.desc
                                $curl = 'curl -o ' . $local_file . ' ' . $remote_file;
                                shell_exec($curl);
                            }

                            $txt_file_desc = file_get_contents($local_file);

                            if (strpos($txt_file_desc, "<title>File Not Found</title>") === FALSE) {

                                # Detalhes do pacote
                                $txt = explode('|', str_replace("\"", "'", str_replace('==', '', str_replace('#', '|'
                                                                , explode('#####', explode('maintainer=', $txt_file_desc)[1])[0]))));

                                $package->maintainer = trim(str_replace("'", '', explode('<', $txt[0])[0]));
                                foreach ($txt as $key => $value) {
                                    if (strpos($value, 'license=') !== FALSE) {
                                        $package_license = trim(explode('license=', $txt[$key])[1]);
                                        $package->license = str_replace("'", '', $package_license);
                                        
                                    }
                                    if (strpos($value, 'desc=') !== FALSE) {
                                        $package->desc = trim(explode("'", (explode('desc=', $txt[$key])[1]))[1]);
                                    }
                                    if (strpos($value, 'url=') !== FALSE) {
                                        $package->url = trim(explode("'", explode('url=', $txt[$key])[1])[1]);
                                        
                                    }
                                    if (strpos($value, 'dep=(') !== FALSE) {
                                        $package_deps = trim(str_replace(')', '', explode('dep=(', $value)[1]));
                                        $package->deps = str_replace('  ', ' ', str_replace(',', ', ', str_replace("'", '', str_replace("' '", ', ', $package_deps))));
                                        
                                    }
                                }
                            } else {
                                #Não tem o .desc
                                $package->maintainer = 'Desconhecido';
                                $package->license = 'Desconhecida';
                                $package->desc = 'Não disponível';
                                $package->url = 'Não disponível';
                                $package->deps = 'Não disponível';
                            } // if File Not Found
                            // Tranforma o objeto $package em JSON
                            $dados_json = json_encode($package, JSON_UNESCAPED_SLASHES | JSON_PRETTY_PRINT);

                            // Cria o arquivo cadastro.json
                            // O parâmetro "a" indica que o arquivo será aberto para escrita
                            $fp = fopen($repo_dirlib . 'json/' . $file_json, 'w+');

                            // Escreve o conteúdo JSON no arquivo
                            $escreve = fwrite($fp, $dados_json);

                            // Fecha o arquivo
                            fclose($fp);
                            $packages[] = $package;
                        } // if (!file_exists($file_json)
                    } // if existe .mz no repositório
                } // foreach tags
            } // foreach urls

            $_SESSION['packages'] = $packages;
            ?>
            <div class="m-4">
                <?php
                echo "Novos pacotes: $novos_pacotes<br>";
                if (count($packages) > 0) {
                    
                    require 'html/tabela.php';
                }
                ?>
            </div>
            <!--div id="mussum-ipsun" class="text-justify">
                <img src="img/mussum-ipsun.png" class="float-left" alt="Cacildis">
    <?php #require_once './bin/etc.php'                    ?>
            </div-->

            <?php
        } catch (Exception $exc) {
            echo $exc->getTraceAsString();
        }
        ?>
<?php require './bin/../html/scripts.php' ?>
    </body>
</html>
<?php
$_SESSION['time']->fim = date('Yjd-h:i:s');
