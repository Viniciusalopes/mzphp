<?php
/*
 * A licença MIT
 *
 * Copyright 2019 Viniciusalopes Tecnologia <suporte@viniciusalopes.com.br>.
 *
 * É concedida permissão, gratuitamente, a qualquer pessoa que obtenha uma cópia
 * deste software e dos arquivos de documentação associados (o "Software"), para
 * negociar o Software sem restrições, incluindo, sem limitação, os direitos de uso,
 * cópia, modificação e fusão, publicar, distribuir, sublicenciar e/ou vender cópias
 * do Software, e permitir que as pessoas a quem o Software é fornecido o façam,
 * sujeitas às seguintes condições:
 *
 * O aviso de copyright acima e este aviso de permissão devem ser incluídos em
 * todas as cópias ou partes substanciais do Software.
 *
 * O SOFTWARE É FORNECIDO "NO ESTADO EM QUE SE ENCONTRA", SEM NENHUM TIPO DE GARANTIA,
 * EXPRESSA OU IMPLÍCITA, INCLUINDO, MAS NÃO SE LIMITANDO ÀS GARANTIAS DE COMERCIALIZAÇÃO,
 * ADEQUAÇÃO A UM FIM ESPECÍFICO E NÃO VIOLAÇÃO. EM NENHUMA CIRCUNSTÂNCIA, OS AUTORES
 * OU PROPRIETÁRIOS DE DIREITOS DE AUTOR PODERÃO SER RESPONSABILIZADOS POR QUAISQUER
 * REIVINDICAÇÕES, DANOS OU OUTRAS RESPONSABILIDADES, QUER EM AÇÃO DE CONTRATO,
 * DELITO OU DE OUTRA FORMA, DECORRENTES DE, OU EM CONEXÃO COM O SOFTWARE OU O USO
 * OU OUTRAS NEGOCIAÇÕES NO PROGRAMAS.
 * ------------------------------------------------------------------------------------------
 * Projeto   : mzphp
 * Criado em : 18/07/2019
 * Autor     : Viniciusalopes (Vovolinux) <suporte@vovolinux.com.br>
 * Finalidade: 
 * ------------------------------------------------------------------------------------------
 */
require_once '../bin/sessao.php';
?>
<hr>
<table id="table-packages" class="table table-sm table-hover">
    <thead class="thead-dark text-left">
        <tr>
            <th scope="col">Instalado</th>
            <th>Repositório</th>
            <th>Espelho</th>
            <th>Diretório</th>
            <th>Nome</th>
            <th>Versão</th>
            <th>Build</th>
            <th>Mantenedor</th>
            <th>Descrição</th>
        </tr>
    </thead>
    <tbody>
        <?php
        /**
         * ObjPackage
          $pkgs[] = (object) [
          'repo' => $pkg[0],
          'mirror' => $pkg[1],
          'folder' => $pkg[2],
          'name' => $pkg[3],
          'version' => $pkg[4],
          'build' => $pkg[5]
          ];
         */
        foreach ($packages as $package) {
            ?>
            <tr scope="row">
                <td><!--?php echo $Os->instalado($pkgname) ?--></td>
                <td><?php echo $package->pkgname ?></td>
                <td><?php echo $package->version ?></td>
                <td><?php echo '( ' . $package->mirror_name . ' )' . $package->mirror ?></td>
                <td><?php echo $package->dir ?></td>
                <td></td>
                <td><?php echo $package->desc ?></td>
            </tr>
            <?php
        }
        ?>
    </tbody>
</table>