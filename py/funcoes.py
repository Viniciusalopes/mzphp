#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, subprocess, threading, time, json, webbrowser
from variaveis import *

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
                       $ sudo php -S hostname:9090)
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
        #print('[ DEBUG ] funcoes.py->xdg()->inicio')
        comando = "echo ${XDG_SESSION_TYPE}"
        #print('[ DEBUG ] funcoes.py->xdg()->subprocess.check_output()')
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
        #print('[ DEBUG ] funcoes.py->root_on()->inicio')
        comando = 'echo belesma | sudo -S id'
        #print('[ DEBUG ] funcoes.py->root_on()->subprocess.check_output()')
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        #print('[ DEBUG ] funcoes.py->root_on()->subprocess.run()')
        var = subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
        #print('[ DEBUG ] funcoes.py->root_on()->return True->var->' + str(var))
        return True
    except:
        #print('[ DEBUG ] funcoes.py->root_on()->return False')
        return False

# THREADS
def phpHost():
    global is_root
    global php
    pid = getPid()
    
    is_root = root_on()
   #print('[ DEBUG ] funcoes.py->phpHost->is_root-> '+str(is_root))
    if is_root:
       #print('[ DEBUG ] funcoes.py->phpHost->php->' + php)
        os.system('sudo '+ php)
       #print('[ DEBUG ] funcoes.py->phpHost->os.system()')
    else:
        #print('[ DEBUG ] funcoes.py->phpHost->exit(1)')
        exit(1)

def startThreadPhpHost():
    global pid
    global is_root
    global php
    
    print('Iniciando servidor Web...')
    p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
    p.start()
    
    i = 0;
    pid = getPid()
    print('[ DEBUG ] funcoes.py->phpHostOff->type(pid)-> '+ str(type(pid)))
    print('[ DEBUG ] funcoes.py->phpHostOff->pid-> '+ str(pid))
    while pid == 0 and i <= 10:
        i += 1
        print('Aguardando inicialização do host...[ ' + str(i) + 's ]')
        pid = getPid()
        time.sleep(1)
        
    print('Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')
    
def phpHostOff():
    global pid_json
    #with open(pid_json) as json_file:
    #    p = json.load(json_file)
    #    pid = p['pid']
    pid = getPid()
    
    if pid > 0:
        print('Iniciando AutoPowerOff do servidor web...')
        
        i = 9
       #print('[ DEBUG ] funcoes.py->phpHostOff->os.path.isfile(pid_json)-> '+ str(os.path.isfile(pid_json)))
        while os.path.isfile(pid_json) and i > 0:
            i -= 1
            print('O servidor web php será desligado em ' + str(i + 1) + ' segundos [ pid-> ' + str(pid) + ' ]')
            time.sleep(1)
            
        print('Desligando servidor Web...')
       #print('[ DEBUG ] funcoes.py->phpHostOff->os.system(sudo kill ' + str(pid) + ')')
        os.system('sudo kill ' + str(pid))
        
        while getPid() > 0:
            time.sleep(1)
        
        print('Servidor Web desligado automaGicamente. =)')
       #print('[ DEBUG ] funcoes.py->phpHostOff->exit(0)')

    else:
        print('Não existe servidor web php ativo.')

    exit(0)
'''
    global is_root
    global pid_json
    global pid
    
    pid = getPid()
    
    i = 10
    while os.path.isfile(pid_json) and i > 0:
        i -= 1
       #print('[ DEBUG ] funcoes.py->O servidor web php será desligado em ' + str(i + 1) + ' segundos [ pid-> ' + str(pid) + ' ]')
        time.sleep(1)
        
    print('Desligando servidor Web...')
   #print('[ DEBUG ] funcoes.py->phpHostOff->os.system(sudo kill ' + str(pid) + ')')
    os.system('sudo kill ' + str(pid))
    print('Servidor Web desligado automaGicamente. =)')
   #print('[ DEBUG ] funcoes.py->phpHostOff->exit(0)')
'''   

# FIM-THREADS


def off():
    # off() é para a chamada interna da instância principal chamar uma nova
    # instância (acima) do mesmo programa (mzphp -o) e deixar o serviço rodando.
    # O site local vai renovar o tempo para desligamento automaGico
    #print('[ DEBUG ] funcoes.py->phpHostOff->off()')
    os.system('sudo /usr/bin/env python3 /opt/mzphp/mzphp -o')
    exit(0)
        
def getPid():
    global is_root
    global pid
    try:           
        comando = "ps -C \"php -S " + hostname + ":9090\" | grep -v PID | sed 's/?\|pts/_/g' | cut -d_ -f1"
        #print('[ DEBUG ] funcoes.py->comando-> ' + comando)
        pid = subprocess.check_output(comando, shell=True)
        #print('[ DEBUG ] funcoes.py->type(pid)-> ' + str(type(pid)))
        #print('[ DEBUG ] funcoes.py->getPid_resultado->' + str(pid.decode('utf-8')).replace('  ',' ') + '---')
        #print('[ DEBUG ] funcoes.py->getPid->len(pid)-> ' + str(len(pid)))
        
        if len(pid) == 0:
            pid = 0
        else:
            pid = int(pid.decode('utf-8').replace('  ',' '))
            
            # Dispensa do login porque já tem servidor web php rodando como root
            is_root = True

        # a Python object (dict):
        p = {
            "pid": pid
        }

        # convert into JSON:
        f = open(pid_json, "w")
        f.write(json.dumps(p, indent=4))
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

   #print('[ DEBUG ] funcoes.py->webBrowser->is_root-> ' + str(is_root))    
 
    print('Abrindo o navegador...') 
    webbrowser.open(index, new=1, autoraise=True)       
    p = threading.Thread(target=off, name='phpHostOff', daemon=True)
    p.start()
    exit(0)
    
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
