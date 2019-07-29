<?php
$path = str_replace('/vovomazon/packages/var/lib/mzphp/', '', $_SERVER['SCRIPT_URL']);
$voltar = ($path == 'unreleased/') ? '../../../../' : '../';
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
Criado em : 29/07/2019
Autor     : Viniciusalopes (Vovolinux) <suporte@vovolinux.com.br>
Finalidade: 
------------------------------------------------------------------------------------------
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Index of /<?php echo $path ?></title>
        <style type="text/css">
            html {
                display: block;
                color: -internal-root-color;
            }

            head {
                display: none;
            }
            body {
                display: block;
                margin: 8px;
            }
            h1 {
                display: block;
                font-size: 2em;
                margin-block-start: 0.67em;
                margin-block-end: 0.67em;
                margin-inline-start: 0px;
                margin-inline-end: 0px;
                font-weight: bold;
            }


            a:-webkit-any-link {
                color: -webkit-link;
                cursor: pointer;
                text-decoration: underline;
            }

            table{
                margin-left: 1em;
            }
            td{
                padding-left: 1em;
            }
            hr {
                display: block;
                unicode-bidi: isolate;
                margin-block-start: 0.5em;
                margin-block-end: 0.5em;
                margin-inline-start: auto;
                margin-inline-end: auto;
                overflow: hidden;
                border-style: inset;
                border-width: 1px;
            }

        </style>
    </head>
    <body>
        <h1>Index of /<?php echo $path ?></h1>
        <a href="<?php echo $voltar ?>"><- voltar</a>
        <pre>
            <hr>
            <?php
            // Obter a listagem dos Arquivos do diretório
            $local = './';
            $itens = [];
            if (is_dir($local)) {
                $diretorio = dir($local);

                while ($arquivo = $diretorio->read()) {
                    if ($arquivo != '..' && $arquivo != '.' && $arquivo != 'index.php') {
                        $itens[] = (object) [
                                    'dir' => (is_dir($arquivo) ? $arquivo . '/' : $arquivo),
                                    'modificado' => date('Y-m-d H:i', filemtime($local . $arquivo))
                        ];
                    }
                }
                $diretorio->close();
            }
            usort($itens, function( $a, $b ) {
                if ($a->dir == $b->dir) {
                    return 0;
                }
                return (( $a->dir < $b->dir ) ? -1 : 1 );
            }
            );
            ?>
            <table>
                <thead>
                <tr>
                    <th>Nome</th>
                    <th>Modificado em</th>
                </tr>
                </thead>
                <tbody>
                    <?php foreach ($itens as $i) { ?>
                                    <tr>
                                        <td><a href='<?php echo $i->dir ?>'><?php echo $i->dir ?></a></td>
                                        <td><?php echo $i->modificado ?></td>
                                    </tr>
                    <?php } ?>
                </tbody>
            </table>
            <hr>
        </pre>
    </body>
</html>
