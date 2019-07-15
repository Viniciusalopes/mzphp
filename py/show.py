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

def show():
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

            for line in csv_reader:
                if package in line[1]:
                    found = True

                    pkgname = line[1].split('-')[0]
                    version = line[1].replace(pkgname + '-', '').replace('.mz', '')

                    # Trying obtains .desc
                    internet = internet_on()
                    nodesc = True
                    if not line[2] == '':
                        if internet:
                            r = requests.get(url + line[0] + line[2])
                            if not r.status_code == 404:
                                # File not found (404 error) - pkgname-version.desc
                                nodesc = False
                                text = r.text

                    # Set maintainer and desc
                    if nodesc:
                        maintainer = '(unknown)'
                        desc = 'Description not available for this package!'

                        if not internet:
                            desc += '\n' + please_connect
                    else:
                        maintainer = (re.findall('maintainer.*', text)[0]).replace("'", '').replace('maintainer=',
                                                                                                    '').replace('"', '')
                        desc = ((text.split('|')[2]).replace('#', '').replace('=', '').replace('desc"', ''))[:-2]

                    print('Package Name: ' + pkgname)
                    print('Version.....: ' + version)
                    print('Maintainer..: ' + maintainer)
                    print(desc)
                    print('-------------------------------------------------------------------------\n')

            if not found:
                print(package_not_found)

# ------------------- FUNCTIONS ------------------------>

