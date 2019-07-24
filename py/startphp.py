#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, webbrowser, socket, time, threading, subprocess
from urllib.request import urlopen
from tkinter import *
from PIL import Image, ImageTk

hostname=socket.gethostname()
porta = '9090'
php = 'php -S ' + hostname + ':' + porta
index = 'http://'+ hostname + ':' + porta
nav = 'exo-open --launch WebBrowser '+ index


is_root = False

root_dir_local = '/opt/mzphp/'

frmLogin = None
tbSenha = None
frmErro = None
ret = None
txtErro = ''
    
def login():
    try:
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
        frmLogin.mainloop()
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
            pid = getPid()
            print('pidPhp-> ' + str(pid))
            comando = 'echo '+ senha + ' | sudo -S id'
            subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
            subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)

            is_root = True
            
            print('Iniciando servidor Web...')
            p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
            p.start()
            webBrowser()
            exit(0)

    except Exception as e:
        txtErro = 'Opa!\nSenha inválida!'
        print(txtErro)
        erro()
        print('---------------------------------------------------------------------')
        print('returncode-> ' + str(e.returncode))
        print(e.output.decode('utf-8'))
        print('---------------------------------------------------------------------')        
        exit(1)
    
def erro():
    try:
        global txtErro
        
        frmErro = Tk()
        frmErro.title('mzPhp v0.2')
        frmErro.geometry('200x120')
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

def phpHost():
    print(str(is_root))
    if is_root:
        os.system('sudo '+ php)
    else:
        exit(1)

def getPid():
    try:           
        comando = "ps -C \"php \\-S studio-nb:9090\" | grep \\-v PID | cut \\-d \' \' \\-f1"
        print('comando: ' + comando)
        pid = subprocess.check_output(comando, shell=True).decode('utf-8')
        if len(pid) == 0:
            return '0'
        else:
            return pid
    except Exception as e:
            txtErro = 'Opa!\nPid muito estranho... Oô'
            print(txtErro)
            print('---------------------------------------------------------------------')
            print('returncode-> ' + str(e.returncode))
            print(str(e.output))
            print('---------------------------------------------------------------------')        
            exit(1)    
        
def webBrowser():
    print(str(is_root))    
    print('Servidor php inicializado.\nAbrindo o navegador...')        
    getPid()

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
    print('Aguardando autenticação do root...')
    print(str(is_root))    

    pid = getPid()
    print('pidPhp-> ' + pid)

    #login()
    
    print('Saindo.')
    exit(0)
    
except KeyboardInterrupt:
    print('\nProcesso cancelado.')
    limpa_tmp()
    exit(1)
    
except Exception as e:
    print('Erro-> ' + e)
    exit(1)
