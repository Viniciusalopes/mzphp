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

def check():
    # Checks if the folder exists
    if not os.path.isdir(dircsv):
        os.mkdir(dircsv)
        print('Created folder ' + dircsv + '.')

    # Checks if the file exists
    if not os.path.isfile(filecsv):
        os.system('touch ' + filecsv)
        print('Created file ' + filecsv + '.')
        os.system('clear')
        update()


# ------------------- END-FUNCTIONS -------------------->
