#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, socket, subprocess, threading, json, webbrowser, time, datetime
from urllib.request import urlopen
from tkinter import *
from PIL import Image, ImageTk

# Para ativar o registro no mzphp.log, substituir "log(" por "log("

#|--- VARIÁVEIS --->

# server
hostname=socket.gethostname()
porta = '9090'
server = hostname + ':' + porta
php = 'php -S ' + server

# locais
index = 'http://'+ server
root_dir_local = '/opt/mzphp/'

# arquivos
log_file = '/var/log/mzphp/mzphp.log'
pid_json = '/tmp/pid.json'

# bool
arg_ok = False
is_root = False

# obj
#ret = None
#frmLogin = None
#tbSenha = None
#frmErro = None

# int
args = 0
pid = 0
timeOff = 5

# dic
argumentos = {
        '-i': 'inicius',
        '-s': 'startThreadPhpHost',
        '--start': 'startThreadPhpHost', 
        '-o': 'startThreadPhpHostOff',
        '--off': 'startThreadPhpHostOff',
        '-p': 'qualPid',
        '--pid': 'qualPid', 
        '-c': 'limpa_log',
        '--clear-log': 'limpa_log', 
        '-l': 'ver_log',
        '--log': 'ver_log',
        '-h': 'socorro',
        '--help': 'socorro' 
    }

# array
arquivos_tmp = [pid_json]


# str
arg = ''
funcao = ''
senha = ''
txtErro = ''
sessao_root_valida = 'O último login como r00t ainda é válido.'
separa = ('-------------------------------------------------------------------------------')    
    
txtHelp = (separa + '''\n\'mzPhp 0.2' é um gerenciador de pacotes que pesquisa e administra programas e
pacotes na distribuição GNU/Linux MazonOs.

Uso:
 mzphp [opções]     gerenciamento de pacotes
    
Opções:
 -s, --start        inicia o servidor web php
                      (o servidor pode ser iniciado manualmente com o comando:
                       $ sudo php -S `hostname`:9090)
 -o, --off          inicia o serviço de desligamento automático do servidor web
 -p, --pid          fornece o pid de servidor web php
 -c, --clear-log    limpa o registro de log (/tmp/mzphp.log)
 -l, --log          ver o registro de log 
 -h, --help         exibe esta ajuda
 
''' + separa + '''
Página do gerenciador online: <https://vovlinux.com.br/vovomazon/packages/>
Página do projeto mzPhp <https://github.com/Viniciusalopes/mzphp/>
Página da distribuição GNU/Linux MazonOs: <http://mazonos.com/>
''' + separa + '\n')

#<--- VARIÁVEIS ---|

#|--- FORMS --->
def login():
    out(False, 'login()-> executando')
    out(True, 'Aguardando autenticação do r00t...')
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
    out(True, 'Cancelado pelo usuário.')
    exit(0)

def erro(txtErro):
    out(False, 'erro(txtErro)-> executando')
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

#<--- FORMS ---|

#|--- FUNÇÕES --->
def socorro():
    sys.stdout.write(txtHelp)
    
def tty():
    comando = "echo ${XDG_SESSION_TYPE}"
    xdg = subprocess.check_output(comando, shell=True).decode('utf-8').replace('\n','')
    if xdg == 'tty':
        return True
        exit(1)
    
    return False

def root_on():
    out(False, 'root_on()-> executando')
    try:
        comando = 'echo '+ senha + ' | sudo -S id'
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        return True
    except:
        return False

def valida_senha():
    out(False, 'valida_senha()-> executando')
    try:
        global is_root
        global tbSenha
        global senha

        senha = tbSenha.get()
        
        if len(senha) == 0:
            txtErro = 'Opa! Senha em branco não vale...'
            out(True, txtErro)
            erro(txtErro.replace('! ', '!\n'))
            exit(1)
        else:
            is_root = root_on()
            
        if is_root:
            frmLogin.destroy
            bora()

        else:
            txtErro = 'Opa! Senha inválida!'
            out(True, txtErro)
            erro(txtErro)
            exit(1)    
            
    except Exception as e:
        txtErro = str(e)
        out(True, txtErro)
        #out(True, 'returncode->(b) ' + str(e.returncode))
        #out(True, e.output.decode('utf-8'))
        erro(txtErro)
        exit(1)    
        
def phpHost():
    out(False, 'phpHost()-> executando')
    global senha
    global php
    try:
        comando = 'echo ' + senha + ' | sudo -S ' + php
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        var = subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
        out(False, 'phpHost->var' + str(var))
    except Exception as e:
        if e.returncode != 143:
            out(False, 'phpHost()->except-> '+ str(e))
            out(True, 'returncode->(c) ' + str(e.returncode))
            out(True, str(e.output))
            exit(e.returncode)
        exit(1)
        
def startThreadPhpHost():
    out(False, 'startThreadPhpHost()-> executando')
    global pid
    pid = getPid()
    if pid == 0:
        out(True, 'Iniciando servidor web...')
        p = threading.Thread(target=phpHost, name='phpHost', daemon=True)
        p.start()
        
        i = 0;
        while pid == 0:
            i += 1
            out(True, 'Aguardando inicialização do host...[ ' + str(i) + 's ]')
            pid = getPid()
            time.sleep(1)

            if i == 5:
                out(True, 'Não foi possível iniciar o servidor web.')
                exit(1)
    
    out(True, 'Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')
        
def phpHostOff():
    out(False, 'phpHostOff()-> executando')
    global senha
    global pid
    global pid_json
    global timeOff
    
    if pid == 0:
        out(True, 'Não existe servidor web php ativo.')
        exit(1)
    else:
        out(True, 'Iniciando AutoPowerOff do servidor web...')
        
        i = timeOff
        while i > 1:
            out(True, 'O servidor web php será desligado em ' + str(i) + ' segundos [ pid-> ' + str(pid) + ' ]')
            i -= 1
            time.sleep(1)
            
        out(True, 'Desligando servidor Web...')
        os.system('echo '+ senha + ' | sudo -S kill ' + str(pid))
        
        while getPid() > 0:
            time.sleep(1)

        os.remove(pid_json)        
        out(True, 'Servidor Web desligado automaGicamente. =)')
        exit(0)    
    
def startThreadPhpHostOff():
    out(False, 'startThreadPhpHostOff()-> executando')
    global senha
    global pid
    global pid_json
    global timeOff
    
    if os.path.isfile(pid_json):
        with open(pid_json) as json_file:
            p = json.load(json_file)
            pid = p['pid']
            timeOff = p['timeOff']
    else:
        pid = getPid()

    if pid == 0:
        out(True, 'Não foi possível identificar o servidor web.')
        exit(1)
    else:
        po = threading.Thread(target=phpHostOff, name='phpHostOff')
        po.start()
        exit(0)

def qualPid():
    out(False, 'qualPid()-> executando')
    pid = getPid()
    if pid == 0:
        out(True, 'Servidor web php não encontrado.')
    else:
        out(True, 'O pid do servidor atual é: ' + str(pid))
    exit(0)
        
def getPid():
    out(False, 'getPid()-> executando')
    global is_root
    global pid
    global timeOff
    try:           
        comando = "ps -C \"php -S " + hostname + ":9090\" | grep -v PID | sed 's/?\|pts/_/g' | cut -d_ -f1"
        pid = subprocess.check_output(comando, shell=True)
        
        if len(pid) == 0:
            pid = 0
        else:
            pid = int(pid.decode('utf-8').replace('  ',' '))
           
        # a Python object (dict):
        p = {
            'pid': pid,
            'timeOff': timeOff
        }

        # convert into JSON:
        f = open(pid_json, "w")
        f.write(json.dumps(p, indent=4))
        f.close()

        return int(pid)

    except Exception as e:
        out(True, 'Opa!\nPid muito estranho... Oô')
        out(True, separa)
        out(True, 'returncode->(a) ' + str(e.returncode))
        out(True, str(e.output))
        out(True, separa)
        exit(1)

def webBrowser():
    out(False, 'webBrowser()-> executando')
    out(True, 'Abrindo o navegador...') 
    webbrowser.open(index, new=1, autoraise=True)       
    exit(0)
                
#|--- LOG --->

def limpa_log():
    out(False, 'limpa_log()-> executando')
    out(True, 'limpa log')
    exit(0)

def ver_log():
    out(False, 'ver log')

def out(saidaPadrao, txt):
    
    now = '[ ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ] '
    
    if txt == 'limpa log':
        texto = '# Registro de log do mzPhp.\n' + now + 'Log reiniciado.'
        p = 'w'
    elif txt == 'ver log':
        os.system('cat ' + log_file)
        exit(0)
    else:
        texto = txt
        p = 'a'
        
    f = open(log_file, p)
    f.write(now + texto + '\n')
    f.close()    

    if saidaPadrao:
        print(texto)

#<--- LOG ---|    

    
#<--- FUNÇÕES ---|


def inicius():
    out(False, 'inicius()-> executando')
    global pid
    
    if pid == 0:
        startThreadPhpHost()
                
    webBrowser()    

def bora():
    out(False, 'bora()-> executando')
    global funcao

    if funcao == 'inicius':
        inicius()
    elif funcao == 'startThreadPhpHost':
        startThreadPhpHost() 
    elif funcao == 'startThreadPhpHostOff':
        startThreadPhpHostOff()
    elif funcao == 'qualPid':
        qualPid() 
    elif funcao == 'limpa_log':
        limpa_log() 
    elif funcao == 'ver_log':
        ver_log()
    else:
        out(True, 'Não deu.')
        exit(1)

    out(True, 'The Fim! ;)')
    out(False, separa)
    exit(0)

try:
    out(False, separa)
    out(False, str(sys.argv).replace('[\'', '').replace('\', \'',' ').replace('\']',''))
    # Não executa sem X
    if tty():
        out(True, 'Opa! Este programa está disponível somente para ambiente gráfico.')
        exit(1)
        
    args = len(sys.argv)

    if args == 1:
        arg_ok = True
        
    elif args == 2:
        arg = sys.argv[1]
        if arg in argumentos:
            arg_ok = True
        else:
            txtErro = 'A opção \"' + arg + '\" é inválida!'
            
    else: # args > 2
        txtErro = 'Excesso de argumentos! [ '
        for a in sys.argv:
            txtErro += '\'' + a + '\' '
        
        txtErro += ']'
        
    if not arg_ok:
        out(True, txtErro)
        time.sleep(1.5)
        socorro()
        exit(1)

    if args == 1:
        arg = '-i'
    else:
        arg = str(sys.argv[1])

    if arg in argumentos:
        funcao = argumentos[arg]
        
    os.chdir(root_dir_local)

    if funcao == 'socorro':
        socorro()
    else:
        is_root = root_on()

        if is_root:
            bora()
        else:
            login()
    
except KeyboardInterrupt:
        out(True, 'Processo cancelado.')
        limpa_tmp()
        exit(1)
            
except IndexError:
    print(txtHelp)
    out(True, 'A opção \"' + arg + '\" é inválida!')
    exit(1)
    
except Exception as e:
    out(True, str(e))
    exit(1)

