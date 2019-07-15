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

def search():
    try:
        sys.argv[2]
    except IndexError:
        menu()
        exit(0)
    else:
        global found
        package = str(sys.argv[2])

        ### OPEN CSV
        with open(filecsv, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            count = 0
            for line in csv_reader:
                if package in line[1]:
                    count += 1
                    print(line[1].replace('.mz', ''))
                    found = True
            print(str(count) + ' package(s) found.')

            if not found:
                print(package_not_found)

# ------------------- FUNCTIONS ------------------------>
