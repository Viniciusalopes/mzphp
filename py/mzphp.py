#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from urllib.request import urlopen
from tkinter import *
from PIL import Image, ImageTk

from variaveis import *
from funcoes import *

#Para ativar o registro no mzphp.log, substituir "#log(" por "log("

#---inicius()--->
def main():
    log('mzphp.py->main()-> executando')
    global arg
    try:
        sys.argv[1]
    except IndexError:
        inicius()
        exit(0)
    else:
        global arg
        arg = str(sys.argv[1])
        
def inicius():
    log('mzphp.py->inicius()-> executando')
    try:
        global pid
        pid = getPid()
        if xdg() == 'tty':
            log('mzphp.py->xdg()->'+ xdg())
            txt = 'Opa!\nEste programa está disponível somente para ambiente gráfico.'
            log(txt)
            print(txt)
            exit(1)
        else:
            global is_root
            is_root = root_on()
            log('mzphp.py->inicius()->is_root->' + str(is_root))
            log('mzphp.py->pid-> ' + str(pid))

            if is_root:
                txt = sessao_root_valida
                log(txt)
                print(txt)

                if pid == 0:
                    startThreadPhpHost()
                else:
                    txt = 'Servidor web já está inicializado. [ pid-> ' + str(pid) + ' ]')
                    log(txt)
                    print(txt)
            else:
                login() # [ ROTA ] login()-> valida_senha()-> startThreadPhpHost()-> webBrowser()
            # Já tem php -S rodando como root... espero eu :|
            webBrowser()              
        exit(0)
            
    except KeyboardInterrupt:
        txt = '\nProcesso cancelado.'
        log(txt)
        print(txt)
        limpa_tmp()
        exit(1)
        
    except Exception as e:
        print('Erro->inicius()-> ' + str(e))
        exit(1)
        
def login():
    log('mzphp.py->login()-> executando')
    try:
        print('Aguardando autenticação do root...')
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
        print('Cancelado pelo usuário.')
        exit(0)
    except Exception as e:
        print('Erro->login()-> ' + e)
        exit(1)

def valida_senha():
    log('mzphp.py->valida_senha()-> executando')
    try:
        global txtErro
        global tbSenha
        global is_root
        global pid
        pid = getPid()
        
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
            
            if pid == 0:
                startThreadPhpHost()

        webBrowser()
        frmLogin.destroy
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
    log('mzphp.py->erro()-> executando')
    try:
        global txtErro
        
        frmErro = Tk()
        frmErro.title('mzPhp v0.2')
        frmErro.geometry('210x120')
        frmErro.resizable(False, False)

        texto = txtErro
        lbTexto = Label(frmErro, text=texto, justify=LEFT)
        lbTexto.grid(row=0, column=0, stick=N+W, padx=10, ipady=3.5, pady=10)

        btOk = Button(frmErro, text="OK", width=10, command=frmErro.destroy)
        btOk.grid(row=1, column=0, padx=10, pady=10)

        frmErro.mainloop()
        exit(1)
    except Exception as e:
        print('Erro->erro()-> ' + e)
        exit(1)


try:
    log(linha)
    log('mzphp.py-> executando')
    os.chdir(root_dir_local)
    main()
    log('mzphp.py->arg->'+ arg)
    if arg in argumentos:
        funcao = argumentos[arg]
        functions = locals()
        functions[funcao]()
    else:
        socorro()
        print('A opção \"' + arg + '\" é inválida!')
    log('The Fim! ;)')
except KeyboardInterrupt:
    print('\n')
    exit(0)        
    
