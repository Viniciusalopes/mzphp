#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, subprocess, threading, time
from variaveis import *
from funcoes import *

#Para ativar o DEBUG, substituir "#print('[ DEBUG ]" por "print('[ DEBUG ]"

def socorro():
    print('''-------------------------------------------------------------------------------
\'mzPhp 0.2' é um gerenciador de pacotes que pesquisa e administra programas e
    pacotes na distribuição GNU/Linux MazonOs.

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
 
-------------------------------------------------------------------------------
Página do gerenciador online: <https://vovlinux.com.br/vovomazon/packages/>
Página do projeto mzPhp <https://github.com/Viniciusalopes/mzphp/>
Página da distribuição GNU/Linux MazonOs: <http://mazonos.com/>
-------------------------------------------------------------------------------''')
def xdg():
    try:
        #print('[ DEBUG ] xdg()->inicio')
        comando = "echo ${XDG_SESSION_TYPE}"
        #print('[ DEBUG ] xdg()->subprocess.check_output()')
        xdg = subprocess.check_output(comando, shell=True)
        return xdg.decode('utf-8').replace('\n','')

    except Exception as e:
        txtErro = 'Opa!\nXDG muito estranho... ôO'
        print(txtErro)
        print('-------------------------------------------------------------------------------')
        print('returncode-> ' + str(e.returncode))
        print(str(e.output))
        print('-------------------------------------------------------------------------------')        
        exit(1)

def root_on():
    try:
        #print('[ DEBUG ] root_on()->inicio')
        comando = 'echo belesma | sudo -S id'
        #print('[ DEBUG ] root_on()->subprocess.check_output()')
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        #print('[ DEBUG ] root_on()->subprocess.run()')
        var = subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
        #print('[ DEBUG ] root_on()->return True->var->' + str(var))
        return True
    except:
        #print('[ DEBUG ] root_on()->return False')
        return False

# THREADS
def phpHost():
    global is_root
    pid = getPid()
    
    is_root = root_on()
    print('[ DEBUG ] phpHost->is_root-> '+str(is_root))
    if is_root:
        os.system('sudo '+ php)
        print('[ DEBUG ] phpHost->os.system()')
    else:
        #print('[ DEBUG ] phpHost->exit(1)')
        exit(1)


def startThreadPhpHost():
    global pid
    global is_root
    
    print('Iniciando servidor Web...')
    p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
    p.start()
    
    i = 0;
    pid = getPid()
    
    while pid == 0 and i <= 10:
        i += 1
        print('Aguardando inicialização do host...[ ' + str(i) + 's ]')
        pid = getPid()
        time.sleep(1)
        
    print('Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')
'''
def startThreadPhpHostOff():
    #global pid_json
    #global frmLogin
    
    print('Iniciando AutoPowerOff do servidor web...')
    #p = threading.Thread(target=phpHostOff, name='phpHostOff')
    #p.start()
    os.system('sudo /usr/bin/env python3 /opt/mzphp/stopphp')
    exit(0)
'''    
def getPid():
    global is_root
    global pid
    try:           
        comando = "ps -C \"php -S " + hostname + ":9090\" | grep -v PID | sed 's/?\|pts/_/g' | cut -d_ -f1"
        #print('[ DEBUG ] comando-> ' + comando)
        pid = subprocess.check_output(comando, shell=True)
        #print('[ DEBUG ] type(pid)-> ' + str(type(pid)))
        #print('[ DEBUG ] getPid_resultado->' + str(pid.decode('utf-8')).replace('  ',' ') + '---')
        
        if len(pid) == 0:
            pid = 0
        else:
            # Dispensa do login porque já tem servidor web php rodando como root
            is_root = True

        # a Python object (dict):
        p = {
          "pid": pid
        }

        f = open(pid_json, "w")
        f.write(str(p))
        f.close()

        return int(pid)

    except Exception as e:
        txtErro = 'Opa!\nPid muito estranho... Oô'
        print(txtErro)
        print('---------------------------------------------------------------------')
        print('returncode-> ' + str(e.returncode))
        print(str(e.output))
        print('---------------------------------------------------------------------')        
        exit(1)

def webBrowser():

    print('[ DEBUG ] webBrowser->is_root-> ' + str(is_root))    
    print('Abrindo o navegador...')        


def limpa_tmp():
    for arquivo in arquivos_tmp:
        if os.path.isfile(arquivo):
            os.remove(arquivo)

def php_on():
    try:
        response = urlopen(index, timeout=10)
        return True
    except:
        return False
        
def opa():
    print('Opa!\nEm desenvolvimento. Vovolinux workando...')
    socorro()
    exit(0)
