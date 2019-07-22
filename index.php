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
        <form class="form-inline"autocomplete="off" method="post" action="terminal.php">
            <input type="hidden" name="persist_command_id" id="persist_command_id" />
            <div class="form-group mx-sm-3 mb-2">
                <label class="col-sm-2 col-form-label">root</label>
                <label for="command" class="sr-only">Senha</label>
                <input type="password" class="form-control" id="command" name="command" placeholder="Senha" autocomplete="off">
            </div>
            <button type="submit" class="btn btn-primary mb-2">OK</button>
        </form>
        <div>
            <pre>
                <?php
                #comando("ps -C \"php -S `hostname`\" | grep php ");
                #comando('/opt/mzphp/bin/starthost');
                comando("whoami");
                //exec('sudo php -S studio-nb:9091');

                function comando($cmd) {
                    exec($cmd . ' 2>&1', $response, $error_code);
                    if ($error_code > 0 AND $response == array()) {
                        $response = array($error_code);
                    }
                    echo "\n";

                    foreach ($response as $r) {
                        #echo htmlentities($r), "\n";
                        echo $r . "\n";
                        #echo explode(' ', $r)[0];
                    }
                    #print_r($response);
                }
                //header('location: http://studio-nb:9091');
                ?>
            </pre>
        </div>
    </body>
</html>
<?php
$_SESSION['time']->fim = date('Yjd-h:i:s');
