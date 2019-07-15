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

def checkdesc():
    if internet_on():
        update()

        global textAnimate
        global done

        found = False
        nodescs = []

        textAnimate = 'Searching '
        t = threading.Thread(target=animate)
        t.start()

        ### OPEN CSV
        with open(filecsv, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)

            for line in csv_reader:
                if line[2] == '':
                    found = True
                    nodescs.append(' ' + line[0] + line[1] + '.desc -> not found!')
            done = True

        if found:
            print('The following packages do not have the .desc file:')
            for n in nodescs:
                print(n)
        else:
            print('All packages are OK!')

    else:
        print(please_connect)
        exit(0)

##------------------ END-FUNCTIONS -------------------->
