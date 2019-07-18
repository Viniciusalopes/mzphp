#!/usr/bin/env python
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
import os

#------------------- END IMPORTS ---------------------->



#------------------- FUNCTIONS ------------------------>

def internet_on():
    path = print(os.path.dirname(os.path.realpath(__file__)))
    print(path)

# ------------------- FUNCTIONS ------------------------>

# def update():
#     if internet_on():
#         global textAnimate
#         global done
#
#         textAnimate = 'Updating '
#
#         t = threading.Thread(target=animate)
#         t.start()
#
#         ### UPDATE WEB
#         r = requests.get(url)
#
#         soup = BeautifulSoup(r.content, 'html.parser')
#         links = soup.find_all('a')
#
#         if os.path.isfile(filecsv):
#             os.system('rm ' + filecsv)
#
#         for link in links:
#             if '/' in link.text:
#                 urls = url + link.text
#                 r = requests.get(urls)
#
#                 soups = BeautifulSoup(r.content, 'html.parser')
#                 linkss = soups.find_all('a')
#
#                 folder = link.text
#                 mz = ''
#                 desc = ''
#                 sha256 = ''
#
#                 for l in linkss:
#                     if '.mz' in l.text:
#                         if l.text.endswith(('.mz')):
#                             mz = l.text
#
#                         if l.text.endswith(('.desc')):
#                             desc = l.text
#
#                         if l.text.endswith(('.sha256')):
#                             sha256 = l.text
#
#                         if mz != '' and sha256 != '':
#                             with open(filecsv, 'a') as new_file:
#                                 csv_writer = csv.writer(new_file)
#                                 csv_writer.writerow([folder, mz, desc, sha256])
#                                 mz = ''
#                                 desc = ''
#                                 sha256 = ''
#         done = True
#     else:
#         print(please_connect)

# ------------------- FUNCTIONS ------------------------>

internet_on()
print(os.path.dirname(os.path.realpath(__file__)))