<?php
require_once './bin/Package.php';
require_once './bin/Os.php';
$Os = new Os();
try {
    if (file_exists('var/lib/mz/mz_base.csv')) {
        $packages = (new Package())->get_csv();
    }
} catch (Exception $exc) {
    echo $exc->getTraceAsString();
}
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
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <title>mzPhp</title>
        <meta name="description" content="mzPhp gerenciador de pacotes">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="css/bootstrap.css">
    </head>

    <body>

        <style type="text/css">
            #menu{
                padding-bottom: 60px;
            }

            #mussum-ipsun > img {
                width: 30%;
                padding: 1em;
            }

        </style>
        <div id="menu">
            <nav class="navbar navbar-dark bg-dark fixed-top">
                <nav class="nav">
                    <a class="navbar-brand active" href="#">mzPhp v0.2</a>
                </nav>
            </nav>
        </div>        
        <div id="subtitulo" class="container text-left p-3">
            <div class="h5">
                <strong>mzphp</strong> é um gerenciador de pacotes em php para pesquisar e administrar pacotes utilizando o <strong><a href="https://bananapkg.github.io/">bananapkg</a></strong>.
            </div>
        </div>
        <hr class="m-0 mb-3">
        <nav class="navbar navbar-light bg-light">
            <a class="navbar-brand">Pacotes para Mazon OS</a>
            <form class="form-inline">
                <input class="form-control mr-sm-2"
                       id="pkgname"
                       name="pkgname"
                       type="search" placeholder="Pesquisar pacotes..." aria-label="Pesquisar pacotes...">
                <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Pesquisar</button>
            </form>
        </nav>
        <div class="m-4">
            <?php
            if (count($packages) > 0) {
                echo count($packages) . ' encontrados.'
                ?>
                <hr>
                <table cellspacing="0">
                    <thead class="text-left">
                        <tr class="border-botton">
                            <th class="border-botton">Instalado</th>
                            <th class="border-botton">Nome do pacote</th>
                            <th class="border-botton">Versão</th>
                            <th class="border-botton">Mantenedor</th>
                            <th class="border-botton">Descrição</th>
                        </tr>
                    </thead>
                    <tbody>
                        <?php
                        foreach ($packages as $package) {
                            $p = explode('-', $package[1]);
                            $pkgname = $p[0];
                            $version = $p[1];
                            ?>
                            <tr>
                                <td class="border-botton"><?php echo $Os->instalado($pkgname) ?></td>
                                <td class="border-botton"><?php echo $pkgname ?></td>
                                <td class="border-botton"><?php echo $version ?></td>
                                <td class="border-botton"></td>
                                <td class="border-botton"></td>
                            </tr>
                            <?php
                        }
                    }
                    ?>
                </tbody>
            </table>
                <div id="mussum-ipsun" class="text-justify">
                <img src="img/mussum-ipsun.png" class="float-left" alt="Cacildis">
                <?php require_once './bin/etc.php'; ?>
            </div>
        </div>
    </body>
</html>
