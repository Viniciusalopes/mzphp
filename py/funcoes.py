#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, subprocess, threading, time, json, webbrowser, datetime
from variaveis import *


#Para ativar o DEBUG, substituir "#print('[ DEBUG ]" por "print('[ DEBUG ]"

def limpa_log():
    log('limpa log')
    exit(0)

def log(txt):
    global log_file

    #now = datetime.datetime.now()
    now = '[ ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ] '
    
    if txt == 'limpa log':
        linha = '# Registro de log do mzPhp.\n' + now + 'Log reiniciado'
        print(linha)
        p = 'w'
    else:
        linha = now + txt
        p = 'a'

    f = open(log_file, p)
    f.write(linha + '\n')
    f.close()    

def socorro():
    log('funcoes.py-> executando')
    print(txtHelp)
def xdg():
    log('funcoes.py->xdg()-> executando')
    try:
        log('funcoes.py->xdg()->inicio')
        comando = "echo ${XDG_SESSION_TYPE}"
        log('funcoes.py->xdg()->subprocess.check_output()')
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
    log('funcoes.py->root_on()-> executando')
    try:
        log('funcoes.py->root_on()->inicio')
        comando = 'echo belesma | sudo -S id'
        log('funcoes.py->root_on()->subprocess.check_output()')
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        log('funcoes.py->root_on()->subprocess.run()')
        var = subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
        log('funcoes.py->root_on()->return True->var->' + str(var))
        return True
    except:
        log('funcoes.py->root_on()->return False')
        return False

# THREADS
def phpHost():
    log('funcoes.py->phpHost()-> executando')
    global is_root
    global php
    pid = getPid()
    
    is_root = root_on()
    log('funcoes.py->phpHost->is_root-> '+str(is_root))
    if is_root:
        log('funcoes.py->phpHost->php->' + php)
        os.system('sudo '+ php)
        log('funcoes.py->phpHost->os.system()')
    else:
        log('funcoes.py->phpHost->exit(1)')
        exit(1)

def startThreadPhpHost():
    log('funcoes.py->startThreadPhpHost()-> executando')
    global pid
    global is_root
    global php
    
    print('Iniciando servidor Web...')
    p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
    p.start()
    
    i = 0;
    pid = getPid()
    log('funcoes.py->phpHostOff->type(pid)-> '+ str(type(pid)))
    log('funcoes.py->phpHostOff->pid-> '+ str(pid))
    while pid == 0 and i <= 10:
        i += 1
        print('Aguardando inicialização do host...[ ' + str(i) + 's ]')
        pid = getPid()
        time.sleep(1)
        
    print('Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')
    
def phpHostOff():
    log('funcoes.py->phpHostOff()-> executando')
    global pid_json
    #with open(pid_json) as json_file:
    #    p = json.load(json_file)
    #    pid = p['pid']
    pid = getPid()
    
    if pid > 0:
        print('Iniciando AutoPowerOff do servidor web...')
        
        i = 9
        log('funcoes.py->phpHostOff->os.path.isfile(pid_json)-> '+ str(os.path.isfile(pid_json)))
        while os.path.isfile(pid_json) and i > 0:
            i -= 1
            print('O servidor web php será desligado em ' + str(i + 1) + ' segundos [ pid-> ' + str(pid) + ' ]')
            time.sleep(1)
            
        print('Desligando servidor Web...')
        log('funcoes.py->phpHostOff->os.system(sudo kill ' + str(pid) + ')')
        os.system('sudo kill ' + str(pid))
        
        while getPid() > 0:
            time.sleep(1)
        
        print('Servidor Web desligado automaGicamente. =)')
        log('funcoes.py->phpHostOff->exit(0)')

    else:
        print('Não existe servidor web php ativo.')

    exit(0)


# FIM-THREADS


def off():
    log('funcoes.py->off()-> executando')    
    # off() é para a chamada interna da instância principal chamar uma nova
    # instância (acima) do mesmo programa (mzphp -o) e deixar o serviço rodando.
    # O site local vai renovar o tempo para desligamento automaGico
    comando = 'sudo /usr/bin/env python3 /opt/mzphp/mzphp -o'
    log(comando)
    os.system(comando)
    exit(0)
        
def getPid():
    log('funcoes.py->getPid()-> executando')
    global is_root
    global pid
    try:           
        comando = "ps -C \"php -S " + hostname + ":9090\" | grep -v PID | sed 's/?\|pts/_/g' | cut -d_ -f1"
        log('funcoes.py->comando-> ' + comando)
        pid = subprocess.check_output(comando, shell=True)
        log('funcoes.py->type(pid)-> ' + str(type(pid)))
        log('funcoes.py->getPid_resultado->' + str(pid))
        log('funcoes.py->getPid->len(pid)-> ' + str(len(pid)))
        
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
    log('funcoes.py->webBrowser()-> executando')
    log('funcoes.py->webBrowser->is_root-> ' + str(is_root))    
 
    print('Abrindo o navegador...') 
    webbrowser.open(index, new=1, autoraise=True)       
    p = threading.Thread(target=off, name='phpHostOff', daemon=True)
    p.start()
    exit(0)
    
def limpa_tmp():
    log('funcoes.py->limpa_tmp()-> executando')
    for arquivo in arquivos_tmp:
        if os.path.isfile(arquivo):
            os.remove(arquivo)

def php_on():
    log('funcoes.py->php_on()-> executando')
    try:
        response = urlopen(index, timeout=10)
        return True
    except:
        return False
        
def opa():
    log('funcoes.py->opa()-> executando')
    print('Opa!\nEm desenvolvimento. Vovolinux workando...')
    socorro()
    exit(0)
