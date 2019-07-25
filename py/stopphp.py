#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys

#Para ativar o DEBUG, substituir "#print('[ DEBUG ]" por "print('[ DEBUG ]"


# THREADS

def help():
    print(''' mzPhp 0.2

 'mzPhp' é um gerenciador de pacotes que pesquisa e administra pacotes na
 distribuição GNU/Linux MazonOs.

Uso:
 mzphp [opções]     gerenciamento de pacotes
    
Opções:
 -s, --start        inicia o servidor web php e abre o sistema no navegador
                      (o servidor pode ser iniciado manualmente com o comando:
                       $ sudo php -S php -S hostname:9090)
 -k, --kill         encerra o servidor web php
                      (o servidor pode ser encerrado manualmente com o comando:
                       $ sudo kill 0000, onde 0000 deve ser o pid do serviço)
 -o, --off          inicia o serviço de desligamento automático do servidor web
 -p, --pid          fornece o pid de servidor web php
  
 -h, --help         exibe esta ajuda

Página do gerenciador online: <https://vovlinux.com.br/vovomazon/packages/>
Página do projeto mzPhp <https://github.com/Viniciusalopes/mzphp>

''')

def phpHostOff():
    global is_root
    global pid_json
    global pid
    
    pid = getPid()
    
    i = 10
    while os.path.isfile(pid_json) and i > 0:
        i -= 1
        print('[ DEBUG ] O servidor web php será desligado em ' + str(i + 1) + ' segundos [ pid-> ' + str(pid) + ' ]')
        time.sleep(1)
        
    print('Desligando servidor Web...')
    print('[ DEBUG ] phpHostOff->os.system(sudo kill ' + str(pid) + ')')
    os.system('sudo kill ' + str(pid))
    print('Servidor Web desligado automaGicamente. =)')
    print('[ DEBUG ] phpHostOff->exit(0)')
   

# FIM-THREADS

def startThreadPhpHostOff():
    global pid_json
    global frmLogin
    
    print('Iniciando AutoPowerOff do servidor web...')
    p = threading.Thread(target=phpHostOff, name='phpHostOff')
    p.start()
