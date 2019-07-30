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
<style type="text/css">
    tr.detalhes{
        cursor: pointer !important;
    }
    div.modal-body > p{
        margin: 0 !important;
    }
    div.modal-body > p > a{
        margin-right: 1em !important;

    }

</style>
<hr>
<table id="table-packages" class="table table-sm table-hover">
    <thead class="thead-dark text-left">
        <tr>
            <th scope="col">Nome</th>
            <th scope="col">Versão</th>
            <th scope="col">Licença</th>
            <th scope="col">Repositório</th>
            <th scope="col">Mantenedor</th>

<!--            <th>Versão</th>
            <th>Licença</th>-->
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
            $id = str_replace('.', '_', $package->name . $package->version);
            ?>

            <tr scope="row" id="<?php echo $id ?>"class="detalhes" onclick="setModal('<?php echo $id ?>')">
                <td>
                    <?php echo $package->name ?>
                </td>
                <td>
                    <?php echo $package->version ?>
                </td>
                <td>
                    <?php echo $package->license ?>
                </td>
                <td>
                    <?php echo ucfirst($package->repo_name) ?>
                </td>
                <td>
                    <?php echo $package->maintainer ?>
                </td>
            </tr>
            <?php
        }
        ?>

    </tbody>
</table>
<!-- Modal -->
<div class="modal fade" id="ModalDetalhes" tabindex="-1" role="dialog" aria-labelledby="TituloModalDetalhes" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div id="modal-content" class="modal-content">

        </div>
    </div>
</div>



<script type="text/javascript">
    function setModal(id) {
        $('#modal-content').load('./html/modal_content.php?id=' + id);
        $('#ModalDetalhes').modal('show');
    }
</script>