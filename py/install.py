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

# ------------------- FUNCTIONS ------------------------>

def install():
    if internet_on():
        try:
            sys.argv[2]
        except IndexError:
            menu()
            exit(0)
        else:
            global found
            package = str(sys.argv[2])
            links = []
            packages = []
            ### OPEN CSV
            with open(filecsv, 'r') as csvfile:
                csv_reader = csv.reader(csvfile)

                for line in csv_reader:
                    if package in line[1]:
                        found = True
                        links.append(url + line[0] + line[1])  # Links for download
                        packages.append(line[1])  # Package names

                if found:
                    pkgcount = packages.__len__()
                    pkglist = ''

                    if pkgcount == 1:
                        install = input('You like install ' + packages[0].replace('.mz', '') + ' ? [Y/n] : ')
                        if install == 'Y' or install == 'y':
                            os.system('wget -O /tmp/' + packages[0] + ' ' + url + links[0])
                            os.system('banana install ' + '/tmp/' + packages[0])
                            os.system('rm ' + '/tmp/' + packages[0])
                        else:
                            exit(0)
                    else:
                        # Make pkglist
                        if pkgcount == 2:
                            pkglist = "'" + packages[0].replace('.mz', '') + "' and '" + packages[1].replace('.mz',
                                                                                                             '') + "'."
                        else:
                            for p in packages:
                                pkglist += (p + ', ')

                            pkglist = pkglist[:-2] + '.'

                        print(str(pkgcount) + ' packages found: ' + pkglist.replace('.mz', ''))

                        install = input('Do you like install ALL packages ? [Y/n] : ')
                        if install == 'Y' or install == 'y':
                            for p in range(pkgcount):
                                os.system('wget -O /tmp/' + packages[p] + ' ' + links[p])
                                os.system('banana install ' + '/tmp/' + packages[p])
                                os.system('rm ' + '/tmp/' + packages[p])
                            else:
                                exit(0)

                else:  # if not found
                    print(package_not_found)

    else:
        print(please_connect)
        exit(0)

# ------------------- FUNCTIONS ------------------------>
