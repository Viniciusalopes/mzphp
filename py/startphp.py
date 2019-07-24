#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, webbrowser, socket, time, threading, subprocess, json
from urllib.request import urlopen
from tkinter import *
from PIL import Image, ImageTk

import funcoes

#Para ativar o DEBUG, substituir "#print('[ DEBUG ]" por "print('[ DEBUG ]"


hostname=socket.gethostname()
porta = '9090'
index = 'http://'+ hostname + ':' + porta
nav = 'exo-open --launch WebBrowser '+ index
pid = 0
php = 'php -S ' + hostname + ':' + porta

is_root = False

root_dir_local = '/opt/mzphp/'
pid_json = '/tmp/pid.json'
frmLogin = None
tbSenha = None
frmErro = None
ret = None

txtErro = ''
sessao_root_valida = 'A última sessão como root ainda é válida.'

def root_on():
    try:
        #print('[ DEBUG ] root_on()->inicio')
        comando = 'echo belesma | sudo -S id'
        #print('[ DEBUG ] root_on()->subprocess.check_output()')
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        #print('[ DEBUG ] root_on()->subprocess.run()')
        var = subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
        #print('[ DEBUG ] root_on()->return True->var' + str(var))
        return True
    except:
        #print('[ DEBUG ] root_on()->return False')
        return False

def login():
    try:
        print('Aguardando autenticação do root...')
        global frmLogin
        global tbSenha

        frmLogin = Tk()
        frmLogin.title('mzPhp v0.2')
        frmLogin.geometry('420x150')
        frmLogin.resizable(False, False)

        texto = 'Opa! Belesma?\nSeja bem vindo ao mzPhp!\nDigite a senha para iniciar.'
        lbTexto = Label(frmLogin, text=texto, justify=LEFT)
        lbTexto.grid(row=0, stick=N+W, padx=10, ipady=3.5, pady=10, columnspan=2)

        image = Image.open(root_dir_local + '/img/mzphp-logo-icon.png')
        photo = ImageTk.PhotoImage(image)
        lbIcon = Label(image=photo)
        lbIcon.image = photo
        lbIcon.grid(row=0, column=3)
        
        lbSenha = Label(frmLogin, text='Senha de r00t:', width=13)
        lbSenha.grid(row=1, column=0, stick=N+W, padx=5, ipady=3.5, pady=10)

        tbSenha = Entry(frmLogin, show='*', width=20)
        tbSenha.focus_set()
        tbSenha.grid(row=1, column=1, ipady=3.3, pady=10)

        btOk = Button(frmLogin, text="OK", width=10, command=valida_senha)
        btOk.grid(row=1, column=3, padx=10, pady=10)
        '''
        text = content.get()
        content.set(text)
        '''
        frmLogin.wait_window()
        print('Cancelado pelo usuário.')
        exit(0)
    except Exception as e:
        print('Erro-> ' + e)
        exit(1)


def valida_senha():
    try:
        global txtErro
        global tbSenha
        global is_root
        
        senha = tbSenha.get()
        if len(senha) == 0:
            txtErro = 'Opa!\nSenha em branco não vale...'
            print(txtErro)
            erro()
            exit(1)
        else:
            comando = 'echo '+ senha + ' | sudo -S id'
            subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
            subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
            is_root = True
            startThreadPhpHost()
            print('[ DEBUG ] valida_senha()->startThreadPhpHostOff()')
            startThreadPhpHostOff()
            webBrowser()
            print('The Fim! :)')
            exit(0)
    except Exception as e:
        txtErro = 'Opa!\nSenha inválida!'
        print(txtErro)
        print('---------------------------------------------------------------------')
        print('returncode-> ' + str(e.returncode))
        print(e.output.decode('utf-8'))
        print('---------------------------------------------------------------------')        
        erro()
        exit(1)
    
def erro():
    try:
        global txtErro
        
        frmErro = Tk()
        frmErro.title('mzPhp v0.2')
        frmErro.geometry('210x120')
        frmErro.resizable(False, False)

        texto = txtErro
        lbTexto = Label(frmErro, text=texto, justify=LEFT)
        lbTexto.grid(row=0, column=0, stick=N+W, padx=10, ipady=3.5, pady=10)

        btOk = Button(frmErro, text="OK", width=10, command=frmErro.quit)
        btOk.grid(row=1, column=0, padx=10, pady=10)

        frmErro.mainloop()
        exit(1)
    except Exception as e:
        print('Erro-> ' + e)
        exit(1)


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

#def phpHostOff():
#    global is_root
#    global pid_json
#    global pid
#    
#    pid = getPid()
#    
#    i = 10
#    while os.path.isfile(pid_json) and i > 0:
#        i -= 1
#        print('[ DEBUG ] O servidor web php será desligado em ' + str(i + 1) + ' segundos [ pid-> ' + str(pid) + ' ]')
#        time.sleep(1)
#        
#    print('Desligando servidor Web...')
#    print('[ DEBUG ] phpHostOff->os.system(sudo kill ' + str(pid) + ')')
#    os.system('sudo kill ' + str(pid))
#    print('Servidor Web desligado automaGicamente. =)')
#    print('[ DEBUG ] phpHostOff->exit(0)')
   

# FIM-THREADS

def startThreadPhpHost():
    global pid
    print('Iniciando servidor Web...')
    p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
    p.start()
    
    i = 0;
    pid = getPid()
    
    while pid == 0:
        i += 1
        print('Aguardando inicialização do host...[ ' + str(i) + 's ]')
        pid = getPid()
        time.sleep(1)
        
    print('Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')

def startThreadPhpHostOff():
    #global pid_json
    #global frmLogin
    
    print('Iniciando AutoPowerOff do servidor web...')
    #p = threading.Thread(target=phpHostOff, name='phpHostOff')
    #p.start()
    os.system('sudo /usr/bin/env python3 /opt/mzphp/stopphp')
    exit(0)
    
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
    #print('[ DEBUG ] webBrowser->is_root-> ' + str(is_root))    
    print(sessao_root_valida)
    print('Abrindo o navegador...')        
    #getPid()

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

#---inicius-->
try:
    pid = getPid()
    #print('[ DEBUG ] pid-> ' + str(pid))
    if pid == 0:
        #print('[ DEBUG ] if pid:')
        if root_on():
            print(sessao_root_valida)
            is_root = True
            startThreadPhpHost()
        else:
            is_root = False
            login() # [ ROTA ] login()-> valida_senha()-> startThreadPhpHost()-> webBrowser()
    else:
        pid = getPid()
        
    print('Servidor web já está inicializado. [ pid-> ' + str(pid) + ' ]')
    startThreadPhpHostOff()
    # Já tem php -S rodando como root
    webBrowser()            
    exit(0)
    
except KeyboardInterrupt:
    print('\nProcesso cancelado.')
    limpa_tmp()
    exit(1)
    
except Exception as e:
    print('Erro-> ' + e)
    exit(1)
    
print('The Fim! ;)')
