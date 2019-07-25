#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, webbrowser, json
from urllib.request import urlopen
from tkinter import *
from PIL import Image, ImageTk

from variaveis import *
from funcoes import *

#Para ativar o DEBUG, substituir "#print('[ DEBUG ]" por "print('[ DEBUG ]"

#---inicius()--->
def main():
    try:
        sys.argv[1]
    except IndexError:
        inicius()
        exit(0)
    else:
        global arg
        arg = str(sys.argv[1])
        
def inicius():
    try:
        global pid
        
        if xdg() == 'tty':
            print('[ DEBUG ] xdg()->'+ xdg())
            print('Opa!\nEste programa está disponível somente para ambiente gráfico.')
            exit(1)
        else:
            global is_root
            is_root = root_on()
            #print('[ DEBUG ] inicius->is_root'+str(is_root))
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
            
            #startThreadPhpHostOff()
            # Já tem php -S rodando como root
            webBrowser()            
        
    except KeyboardInterrupt:
        print('\nProcesso cancelado.')
        limpa_tmp()
        exit(1)
        
    except Exception as e:
        print('Erro-> ' + str(e))
        exit(1)
        
    print('The Fim! ;)')
    

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
            frmLogin.destroy
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

        btOk = Button(frmErro, text="OK", width=10, command=frmErro.destroy)
        btOk.grid(row=1, column=0, padx=10, pady=10)

        frmErro.mainloop()
        exit(1)
    except Exception as e:
        print('Erro-> ' + e)
        exit(1)


try:
    main()
    #print('[ DEBUG ] arg->'+ arg)
    if arg in argumentos:
        funcao = argumentos[arg]
        functions = locals()
        functions[funcao]()
    else:
        socorro()
        print('A opção \"' + arg + '\" é inválida!')

except KeyboardInterrupt:
    print('\n')
    exit(0)        

