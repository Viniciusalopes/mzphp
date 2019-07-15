#!/usr/bin/env python3
'''
Autor  : Vovolinux <suporte@vovolinux.com.br>
Data   : 15/07/2019
Projeto: mzphp

Contém reaproveitamento de código do projeto mz python3 - v1.0.0.1,
Originalmente criado por Diego Sarzi sob a licença MIT
(https://github.com/mazonos/mz)
'''
#------------------- VARIABLES ------------------------>

# Paths

# Flags

# Strings

# Arrays

#------------------- END VARIABLES -------------------->


#------------------- IMPORTS -------------------------->
#------------------- END IMPORTS ---------------------->



#------------------- FUNCTIONS ------------------------>

def main():
    try:
        sys.argv[1]
    except IndexError:
        menu()
        exit(0)
    else:
        global choose
        choose = str(sys.argv[1])

# ------------------- FUNCTIONS ------------------------>

def remove():
    try:
        sys.argv[2]
    except IndexError:
        menu()
        exit(0)
    else:
        global found
        onlyfiles = [f for f in os.listdir(dirlist) if os.path.isfile(os.path.join(dirlist, f))]
        r = re.compile(sys.argv[2] + '.*')
        newlist = list(filter(r.match, onlyfiles))

        if newlist:
            found = True
            for pack in newlist:
                package = pack.replace('.list', '')
                remove = input('You like remove ' + package + '? [Y/n] : ')
                if remove == 'y' or remove == 'Y':
                    os.system('banana remove ' + package + ' -y')
                else:
                    exit(0)

        if not found:
            print(package_not_found)

# ------------------- FUNCTIONS ------------------------>
