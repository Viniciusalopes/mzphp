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

# Arrays
argumentos = [
                '-s', '--start', 
                '-k', '--kill',
                '-o', '--off',
                '-p', '--pid', 
                '-h', '--help' 
            ]
