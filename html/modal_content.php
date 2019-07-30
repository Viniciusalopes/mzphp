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
 * Criado em : 29/07/2019
 * Autor     : Viniciusalopes (Vovolinux) <suporte@vovolinux.com.br>
 * Finalidade: 
 * ------------------------------------------------------------------------------------------
 */

require_once '../bin/sessao.php';
$id = str_replace('-', '', str_replace('_', '', $_GET['id']));
foreach ($_SESSION['packages'] as $p) {
    if ($id == str_replace('-', '', str_replace('.', '', str_replace('_', '', $p->name . $p->version)))) {
        $descricao = $p->desc;
        $repo_name = ($p->repo_name == 'vovolinux') ? 'vovomazon': $p->repo_name;
        $repo_url = $p->repo_url;
        $repo_dirlib = $p->repo_dirlib;
        $folder = $p->folder;
        $name = $p->name;
        $version = $p->version;
        $maintainer = $p->maintainer;
        $license = $p->license;
        $url = $p->url;
        $deps = (strlen($p->deps) == 0) ? 'Nenhuma.' : $p->deps;
        $file_mz = $p->file_mz;
        $file_desc = $p->file_desc;
        $file_sha256 = $p->file_sha256;
        $file_json = $p->file_json;
        $desc = $p->desc;
        break;
    }
}
$link_mz = $repo_url . $folder . $file_mz;
$link_desc = $repo_url . $folder . $file_desc;
$link_sha256 = $repo_url . $folder . $file_sha256;
$link_json = "https://vovolinux.com.br/vovomazon/packages/var/lib/mzphp/json/$file_json";


$repositorio = "REPOSIÓRIO:<a href=\"$repo_url" . "$folder\">".ucfirst($repo_name)."</a>";
$tituloModal = $name . '-' . $version . '.mz';
$modalBody = "<p>MANTENEDOR: $maintainer</p>"
        . "<hr>"
        . "<p>FONTE DO PROGRAMA:<br><a href=\"$url\">" . str_replace('/', '/<wbr>', $url) . "</a></p>"
        . "<br>"
        . "<p>DEPENDÊNCIAS: $deps</p>"
        . "<hr>"
        . "<p>ARQUIVOS: <a href=\"$link_json\">.json</a><a href=\"$link_desc\">.desc</a><a href=\"$link_sha256\">.sha256</a></p>"
        . "<hr>"
        . "<p>DESCRIÇÃO: $desc</p>"
;
?>

<div class = "modal-header">
    <span class="h5 modal-title" id="TituloModalDetalhes"><?php echo $tituloModal ?></span>
    <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
        <span aria-hidden="true">&times;</span>
    </button>
</div>
<div class="modal-body">
    <p><span><?php echo $repositorio ?></span>
        <span><?php echo $modalBody ?></span></p>

</div>
<div class="modal-footer">
    <div class="paginate_button page-item next">
        <a class="page-link btn-light">Instalar</a>
    </div>
    <div class="paginate_button page-item next">
        <a class="page-link btn-light-green" href="<?php echo $link_mz ?>">Download .mz</a>
    </div>
</div>
