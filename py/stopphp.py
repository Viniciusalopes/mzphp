#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import startphp
# THREADS
def phpHost():
    global is_root
    print('[ DEBUG ] phpHost->is_root-> '+str(is_root))
    if is_root:
        os.system('sudo '+ php)
        print('[ DEBUG ] phpHost->os.system()')
    else:
        print('[ DEBUG ] phpHost->exit(1)')
        exit(1)

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
    
startThreadPhpHostOff()
