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
 * Criado em : 15/07/2019
 * Autor     : Viniciusalopes (Vovolinux) <suporte@vovolinux.com.br>
 * Finalidade: 
 * ------------------------------------------------------------------------------------------
 */

/**
 * Description of Mirror
 *
 * @author vovostudio
 */
class Mirror {

    private $url = '';
    private $dirs = [];
    private $packages = [];

    # Construtor
    function __construct($url, $dirs) {
        $this->url = $url;
        $this->dirs = $dirs;
    }

    # GET

    function get_url() {
        return $this->url;
    }

    function get_dirs() {
        return $this->dirs;
    }

    # SET

    private function set_url($url) {
        $this->url = $url;
    }

    private function set_dirs($dirs) {
        $this->dirs = $dirs;
    }

    private function set_mirror($url, $dirs, $packages) {
        $this->set_url($url);
        $this->set_dirs($dirs);
        $this->set_packages($packages);
    }
}
