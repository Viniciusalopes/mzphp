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

# ------------------- END-FUNCTIONS ------------------------>
