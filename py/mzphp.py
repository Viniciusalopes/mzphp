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
arquivos_tmp = [pid_json]

# bool
is_root = False

# obj
#ret = None
#frmLogin = None
#tbSenha = None
#frmErro = None

# int
pid = 0
timeOff = 15

# dic
argumentos = {
        '-s': 'startThreadPhpHost',
        '--start': 'startThreadPhpHost', 
        '-o': 'phpHostOff',
        '--off': 'phpHostOff',
        '-p': 'qualPid',
        '--pid': 'qualPid', 
        '-c': 'limpa_log',
        '--clear-log': 'limpa_log', 
        '-l': 'ver_log',
        '--log': 'ver_log',
        '-h': 'socorro',
        '--help': 'socorro' 
    }

# str
arg = ''
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
    out(False, 'tty()-> executando')
    comando = "echo ${XDG_SESSION_TYPE}"
    xdg = subprocess.check_output(comando, shell=True).decode('utf-8').replace('\n','')
    if xdg == 'tty':
        return True
        exit(1)
    
    return False

def inicius():
    out(False, 'inicius()-> executando')
    if tty():
        out(True, 'Opa! Este programa está disponível somente para ambiente gráfico.')
        exit(1)
    else:
        global is_root
        global pid
        is_root = root_on()
        pid = getPid()

        if is_root:
            out(True, 'Usuário r00t autenticado.')
            if pid == 0:
                startThreadPhpHost()
            else:
                out(True, 'Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')

            # Encerra se a chamada foi 'mzphp -s'
            if len(sys.argv) == 2:
                if sys.argv[1] == '-s' or sys.argv[1] == '--start':
                    exit(0)
                            
            webBrowser()                
        else:
            login()
            frmLogin.quit
            inicius()
    
def root_on():
    out(False, 'root_on()-> executando')
    global is_root
    
    try:
        comando = 'echo '+ senha + ' | sudo -S id'
        subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
        return True
    except:
        return False

def valida_senha():
    out(False, 'valida_senha()-> executando')
    try:
        global tbSenha
        global senha
        senha = tbSenha.get()
        
        if len(senha) == 0:
            txtErro = 'Opa! Senha em branco não vale...'
            out(True, txtErro)
            erro(txtErro.replace('! ', '!\n'))
            exit(1)
        else:
            comando = 'echo '+ senha + ' | sudo -S id'
            ret = subprocess.check_output(comando, stderr=subprocess.STDOUT, shell=True)
            #subprocess.run(comando.split(), stderr=subprocess.STDOUT, shell=True)
            is_root = True
            inicius()
            
    except Exception as e:
        txtErro = 'Opa! Senha inválida!'
        out(True, txtErro)
        out(True, 'returncode->(b) ' + str(e.returncode))
        out(True, e.output.decode('utf-8'))
        erro(txtErro)
        exit(1)    
        
def phpHost():
    out(False, 'phpHost()-> executando')
    global pid
    global senha
    global is_root

    if pid == 0:
        if is_root:
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
        else:
            login()
    else:
        out(True, 'Servidor web inicializado. [ pid-> ' + str(pid) + ' ]')
        
def startThreadPhpHost():
    out(False, 'startThreadPhpHost()-> executando')
    global is_root
    global pid
    out(False, 'pid: ' + str(pid))    
    if pid == 0:
        if is_root:
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
        else:
            login()

def phpHostOff():
    out(False, 'phpHostOff()-> executando')
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
        
        
    if pid > 0:
        out(True, 'Iniciando AutoPowerOff do servidor web...')
        
        i = timeOff
        while os.path.isfile(pid_json) and i > 1:
            i -= 1
            time.sleep(1)
            out(True, 'O servidor web php será desligado em ' + str(i) + ' segundos [ pid-> ' + str(pid) + ' ]')
            
        out(True, 'Desligando servidor Web...')
        os.system('echo '+ senha + ' | sudo -S kill ' + str(pid))
        
        while getPid() > 0:
            time.sleep(1)
        
        out(True, 'Servidor Web desligado automaGicamente. =)')
        exit(0)    
    else:
        out(True, 'Não existe servidor web php ativo.')
        exit(1)
    
def startThreadPhpHostOff():
    out(False, 'startThreadPhpHostOff()-> executando')
    # startThreadPhpHostOff() é para a chamada interna da
    # instância principal chamar uma nova
    # instância (acima) do mesmo programa (mzphp -o) e deixar o serviço rodando.
    # O site local vai renovar o tempo para desligamento automaGico
    comando = 'sudo /usr/bin/env python3 /opt/mzphp/mzphp -o'
    out(False, comando)
    os.system(comando)        
    exit(0)

def qualPid():
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
    startThreadPhpHostOff()
    exit(0)
                
#|--- LOG --->

def limpa_log():
    out(False, 'limpa_log()-> executando')
    out(True, 'limpa log')
    exit(0)

def ver_log():
    #out(False, 'ver_log()-> executando')
    os.system('cat ' + log_file)
    exit(0)

def out(saidaPadrao, txt):
    now = '[ ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' ] '
    
    if txt == 'limpa log':
        texto = '# Registro de log do mzPhp.\n' + now + 'Log reiniciado.'
        p = 'w'
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

#out(False, ' executando')
try:
    os.chdir(root_dir_local)
    if len(sys.argv) == 1:
        inicius()
    elif len(sys.argv) == 2:
        arg = sys.argv[1]

        if arg in argumentos:
            funcao = argumentos[arg]
            functions = locals()
            functions[funcao]()
        else:
            out(True, 'A opção \"' + arg + '\" é inválida!')
            time.sleep(2)
            print(txtHelp)
            exit(1)
    else:
        txt = 'Excesso de argumentos! [ '
        for a in sys.argv:
            txt += '\'' + a + '\' '
            
        out(True, txt + ']')
        time.sleep(2)
        print(txtHelp)
        exit(1)

    out(True, 'The Fim! ;)')
    out(False, separa)
    exit(0)

except KeyboardInterrupt:
        out(True, '\nProcesso cancelado.')
        limpa_tmp()
        exit(1)
            
except IndexError:
    print(txtHelp)
    out(True, 'A opção \"' + arg + '\" é inválida!')
    exit(1)
    
except Exception as e:
    out(True, str(e))
    exit(1)

