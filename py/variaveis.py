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
        '-h': 'socorro',
        '--help': 'socorro' 
    }
