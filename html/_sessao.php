<?php
require_once 'bin/sessao.php';
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
Projeto   : LightSun
Criado em : 06/07/2019
Autor     : Viniciusalopes (Vovolinux) <suporte@viniciusalopes.com.br>
Finalidade: Exibir variáveis da sessão
------------------------------------------------------------------------------------------
-->
<html>
    <head>
        <meta charset="UTF-8">
        <title>Sessão</title>
    </head>
    <body>
        <style type="text/css">
            a{
                margin-right: 2em;
            }
            
            .red {
                color: red;
            }

            .black {
                color: black;
            }

            .bold {
                font-weight: bold;
            }

            .uppercase {
                text-transform: uppercase;
            }

            
        </style>
        <pre>
            <?php
            if (count($_SESSION) > 0) {
                ?><a href="_limpar_sessao.php">Limpar Sessão</a><?php
                # itens para o menu

                $itens = [(object) ['item' => 'top', 'link' => "<a classe href=\"#top\">top</a>"]];
                
                foreach ($_SESSION as $key => $value) {
                    $itens [] = (object) [
                                'item' => $key,
                                'link' => "<a classe href=\"#$key\" >$key</a>"
                    ];
                }

                foreach ($_SESSION as $key => $value) {
                    $var = "<div id=\"$key\">"; # identifica a var
                    # Monta o menu
                    $menu = "<div id=\"menu\"><hr>";
                    foreach ($itens as $item) {
                        $link = ($item->item == $key) ?
                                str_replace('classe', "class=\"red bold uppercase\"", $item->link) : # Seleciona o item atual do menu
                                str_replace('classe', '', $item->link);                       # Remove a flag da classe
                        $menu .= $link;
                    }
                    $menu .= '<hr></div>';

                    echo $var . $menu . "<p class=\"black bold uppercase\">$key</p>"; # imprime o inicio da var e o menu
                    print_r($value);   # imprime o valor da variável
                    echo "</div>";     # fecha a div
                }
            } else {
                echo "Nenhuma variável na sessão.";
            }
            ?>
        </pre>
    </body>
</html>

<?php

