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
            $packages = [];
            // Obter a listagem dos Arquivos do diretório
            $local = $_SESSION['dirlib'] . 'json/';

            if (is_dir($local)) {
                $diretorio = dir($local);

                while ($arquivo = $diretorio->read()) {
                    $ext = pathinfo($local . $arquivo, PATHINFO_EXTENSION);
                    if (is_file($local . $arquivo) && $ext == 'json') {
                        $txt_file_json = file_get_contents($local . $arquivo);

                        $pkg = json_decode($txt_file_json);

                        $packages[] = $pkg;
                    }
                }
                $diretorio->close();
            }
            usort($packages, function( $a, $b ) {
                if ($a->name == $b->name) {
                    return 0;
                }
                return (( $a->name < $b->name ) ? -1 : 1 );
            }
            );


            $_SESSION['packages'] = $packages;
            ?>
            <div class="m-4">
                <?php
                if (count($packages) > 0) {

                    require 'html/tabela.php';
                }
                ?>
            </div>


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
