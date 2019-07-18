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
        $mirrors = [];
        $dirs = [];
        $doc = new DOMDocument();

        foreach ($_SESSION['mirrors_urls'] as $mirror) {
            $doc->loadHTMLFile($mirror->url);
            $tags = $doc->getElementsByTagName('a');

            foreach ($tags as $tag) {
                if (strpos($tag->nodeValue, '/') !== FALSE) {
                    $dirs[] = (object) [
                                'mirror_name' => $mirror->name,
                                'mirror' => $mirror->url,
                                'name' => $tag->nodeValue,
                                'packages' => []
                    ];
                }
            }
            $_SESSION['dirs'] = $dirs;
//            foreach ($dirs as $d) {
//                $doc->loadHTMLFile($d->mirror . $d->name);
//                $tags = $doc->getElementsByTagName('a');
//
//                foreach ($tags as $tag) {
//                    $len = (int) strlen($tag->nodeValue);
//                    if (substr($tag->nodeValue, $len - 5) !== '.desc' &&
//                            substr($tag->nodeValue, $len - 7) !== '.sha256' &&
//                            substr($tag->nodeValue, $len - 4) !== '.sig') {
//                        $pkg = explode('-', $tag->nodeValue);
//                        $d->packages[] = (object) [
//                                    'mirror_name' => $d->mirror_name,
//                                    'mirror' => $d->mirror,
//                                    'dir' => $d->name,
//                                    'pkgname' => $pkg[0],
//                                    'version' => count($pkg)
//                        ];
//                    }
//                }
//                $mirrors[] = (object) ['url' => $mirror->url, 'dirs' => $dirs];
//        }
        }
        $_SESSION['mirrors'] = $mirrors;
        ?>
        <div class="m-4">
            <?php
            $packages = [];
            foreach ($mirrors as $mirror) {
                foreach ($mirror->dirs as $dir) {
                    foreach ($dir->packages as $package) {
                        $packages[] = $package;
                    }
                }
            }

            if (count($packages) > 0) {
                #require 'html/tabela.php';
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
