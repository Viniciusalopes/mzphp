#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

hostname=socket.gethostname()
porta = '9090'
index = 'http://'+ hostname + ':' + porta
nav = 'exo-open --launch WebBrowser '+ index
pid = 0
php = 'php -S ' + hostname + ':' + porta

is_root = False

root_dir_local = '/opt/mzphp/'
log_file = '/var/log/mzphp/mzphp.log'
pid_json = '/tmp/pid.json'
arquivos_tmp = [pid_json]

frmLogin = None
tbSenha = None
frmErro = None
ret = None

txtErro = ''
sessao_root_valida = 'O último login como root ainda é válido.'

arg = ''

# Dicionário de dados com as opções do menu
argumentos = {
        '-s': 'inicius',
        '--start': 'inicius', 
        '-k': 'opa',
        '--kill': 'opa',
        '-o': 'phpHostOff',
        '--off': 'phpHostOff',
        '-p': 'opa',
        '--pid': 'opa', 
        '-c': 'limpa_log',
        '--clear-log': 'limpa_log', 
        '-h': 'socorro',
        '--help': 'socorro' 
    }
linha = ('-------------------------------------------------------------------------------')    
txtHelp = (linha + '''\n\'mzPhp 0.2' é um gerenciador de pacotes que pesquisa e administra programas e
pacotes na distribuição GNU/Linux MazonOs.

Uso:
 mzphp [opções]     gerenciamento de pacotes
    
Opções:
 -s, --start        inicia o servidor web php e abre o sistema no navegador
                      (o servidor pode ser iniciado manualmente com o comando:
                       $ sudo php -S hostname:9090)
 -k, --kill         encerra o servidor web php
                      (o servidor pode ser encerrado manualmente com o comando:
                       $ sudo kill 0000, onde 0000 deve ser o pid do serviço)
 -o, --off          inicia o serviço de desligamento automático do servidor web
 -p, --pid          fornece o pid de servidor web php
 -c, --clear-log    limpa o registro de log (/tmp/mzphp.log)
  
 -h, --help         exibe esta ajuda
 
''' + linha + '''
Página do gerenciador online: <https://vovlinux.com.br/vovomazon/packages/>
Página do projeto mzPhp <https://github.com/Viniciusalopes/mzphp/>
Página da distribuição GNU/Linux MazonOs: <http://mazonos.com/>
''' + linha)
