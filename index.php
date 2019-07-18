<?php
require_once './bin/sessao.php';
require_once './bin/Mirror.php';
require_once './bin/Package.php';
require_once './bin/Os.php';
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
        $mirror = (new Mirror())->get_url();

        $doc = new DOMDocument();
        $doc->loadHTMLFile($mirror);
        $tags = $doc->getElementsByTagName('a');

        $dirs = [];
        foreach ($tags as $tag) {
            if (strpos($tag->nodeValue, '/') !== FALSE) {
                $dirs[] = (object) ['dir' => $tag->nodeValue];
            }
        }
        $_SESSION['dirs'] = $dirs;

        $packages = [];
        foreach ($dirs as $d) {
            $doc->loadHTMLFile($mirror . $d->dir);
            $tags = $doc->getElementsByTagName('a');

            foreach ($tags as $tag) {
                $len = (int) strlen($tag->nodeValue);
                $pos = (int) strpos($tag->nodeValue, '.mz');
                if ($pos === $len - 3) {
                    $pkg = explode('-', $tag->nodeValue);
                    $packages[] = (object) [
                                'mirror' => $mirror,
                                'dir' => $d->dir,
                                'pkgname' => $pkg[0],
                                'version' => $pkg[1]
                    ];
                }
            }
        }
        $_SESSION['packages'] = $packages;
        ?>
        <div class="m-4">
            <?php if (count($packages) > 0) { ?>
                <hr>
                <table id="table-packages" class="table table-sm table-hover">
                    <thead class="thead-dark text-left">
                        <tr>
                            <th scope="col">Instalado</th>
                            <th>Nome do pacote</th>
                            <th>Versão</th>
                            <th>Espelho</th>
                            <th>Mantenedor</th>
                            <th>Descrição</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        foreach ($packages as $package) {
                            ?>
                            <tr scope="row">
                                <td><!--?php echo $Os->instalado($pkgname) ?--></td>
                                <td><?php echo $package->pkgname ?></td>
                                <td><?php echo $package->version ?></td>
                                <td><?php echo $package->mirror ?></td>
                                <td></td>
                                <td></td>
                            </tr>
                            <?php
                        }
                    }
                    ?>
                </tbody>
            </table>
            <!--            <div id="mussum-ipsun" class="text-justify">
                            <img src="img/mussum-ipsun.png" class="float-left" alt="Cacildis">
            <!--?php require_once './bin/etc.php' ?>
        </div>-->
        </div>
        <?php require './html/scripts.php' ?>
    </body>
</html>
