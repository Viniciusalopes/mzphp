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
require_once './bin/sessao.php';
?>
<hr>
<table id="table-packages" class="table table-sm table-hover">
    <thead class="thead-dark text-left">
        <tr>
            <?php echo ($_SERVER['HTTP_HOST'] == 'vovolinux.com.br') ? '' : "<th scope=\"col\">Instalado</th>" ?>
            <th>Nome</th>
            <th>Versão</th>
            <th>Licença</th>
            <th>Repositório</th>
            <th>Mantenedor</th>
            <th>Dependências</th>
<!--            <th>Url</th>
            <th>Descrição</th>-->
        </tr>
    </thead>
    <tbody>
        <?php
        /**
          [1] => stdClass Object
          (
          [repo_name] => oficial
          [repo_url] => http://mazonos.com/packages/
          [repo_dirlib] => /var/lib/mzphp/
          [folder] => base/
          [name] => automake
          [version] => 1.16.1-1
          [maintainer] => Diego Sarzi
          [license] =>
          [url] => http://www.linuxfromscratch.org/lfs/view/stable/chapter06/automake.html
          [deps] => ''
          [file_mz] => automake-1.16.1-1.mz
          [file_desc] => automake-1.16.1-1.mz.desc
          [file_sha256] => automake-1.16.1-1.mz.sha256
          [file_json] => automake-1.16.1-1.mz.json
          [desc] => The Automake package contains programs for generating Makefiles
          for use with Autoconf.
          )
         */
        foreach ($packages as $package) {
            $deps = (strlen($package->deps) > 50) ? substr($package->deps, 0, 50) . ' (...)' : $package->deps;
            ?>
            <tr scope="row">
                <?php echo ($_SERVER['HTTP_HOST'] == 'vovolinux.com.br') ? '' : "<th scope=\"col\">???</th>" ?>
                <td><?php echo $package->name ?></td>
                <td><?php echo $package->version ?></td>
                <td><?php echo $package->license ?></td>
                <td><?php echo $package->repo_name ?></td>
                <td><?php echo $package->maintainer ?></td>
                <td><?php echo $deps ?></td>
    <!--                <td>< ?php echo $package->url ?></td>
                <td>< ?php echo $package->desc ?></td>-->
            </tr>
            <?php
        }
        ?>
    </tbody>
</table>