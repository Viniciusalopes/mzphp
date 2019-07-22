#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, webbrowser, socket, threading, time, subprocess

hostname=socket.gethostname()
porta = '9090'
php = 'php -S ' + hostname + ':' + porta
nav = 'exo-open --launch WebBrowser --new-window http://'+ hostname + ':' + porta
killphp = 'sudo kill `ps -C \"' + php + '\" | cut -d \' \' -f1`'
parar = False
threadPhp = False
mzphp_on = '/tmp/mzphp.on'

def phpHost():
    print('Iniciando servidor Web...')
    os.system('sudo '+ php)

    # Colocar teste da saida do sudo com subprocess e encerrar se não for root
    time.sleep(2)
    while True: 
        global parar
        time.sleep(1)
        
        # NOTA:
        #   Se o usuário teclar CTRL+C uma vez no terminal, o servidor Web é
        #   encerrado com o comando 'killphp' porém a thread 'phpHost' continua
        #   executando em concorrência com a thread 'MainThread'.
        #
        #   Para não solicitar outro CTRL+C do usuário, mudo a flag 'threadPhp'
        #   dentro de 'if threading.current_thread().name == p.name:' para True,
        #   indicando a concorrência e encerrando assim todas as threads.
        #                       
        #   Para visualizar esse comportamento basta descomentar as duas 
        #   linhas com o comando:
        #   #print('Executando-> ' + str(threading.current_thread().name))    
        #
        
        # DESCOMENTE A LINHA ABAIXO PARA VISUALIZAR A CONCORRÊNCIA DE THREADS.
        #print('Executando-> ' + str(threading.current_thread().name))    

        # Testa se a thread 'phpHost' está em concorrência com a 'MainThread'.
        if threading.current_thread().name == p.name:
            print('\nCancelado pelo usuário.(CTRL+C)')
            threadPhp = True
            exit(1)
            
        if parar:
            break
        
        
def navegador():
    webbrowser.open_new_tab('http://' + hostname + ':' + porta)

try:
    os.system('touch ' + mzphp_on)
    p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
    p.start()
        
    time.sleep(3)
    webbrowser.open_new_tab('http://' + hostname + ':' + porta)

    while p.isAlive():
        # VIDE NOTA ACIMA.
        # DESCOMENTE A LINHA ABAIXO PARA VISUALIZAR A CONCORRÊNCIA DE THREADS.
        #print('Executando-> ' + str(threading.current_thread().name))
        
        if not os.path.isfile(mzphp_on):
            parar = True
            break
            
        time.sleep(1)
        
        if threadPhp:
            os.system(killphp)
            exit(0)

except KeyboardInterrupt:
    print('\nCancelado pelo usuário.(CTRL+C, 2x)')
    exit(1)

exit(0)

