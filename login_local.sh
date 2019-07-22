#!/usr/bin/env bash
# Autor: Marcos Paulo Ferreira (daemonio)
# undefinido gmail com
# daemoniolabs.wordpress.com
#
# [zensudo.sh]
# Script que simula uma autenticação usando
# o zenity e o sudo.
#
# OBS: Executar o sudo em seu próprio usuário, a senha
# não é verificada. Executar o script mais de uma
# vez em um curto intervalo de tempo, implica no sudo nem
# considerar a senha de entrada.
# Isso porque o sudo tem um tempo que ele fica sem pedir a senha.
#
# Qui Out 20 18:36:37 BRST 2011
#

while true
do
    resp=$(zenity --title='mzPhp - root' --width=160 --password)
    
    if [[ "${resp}" == "" ]]; then
        exit 0
    else
        # Pega a senha do login gráfico
        senha=$(echo "$resp" | cut -f1 -d'|')

        # Passa a senha
        #echo "${senha}" | sudo -S -u root zenity --info --text 'Bem vindo: r00t' 1 2>/dev/null && exit 0
        echo "${senha}" | sudo -S -u root zenity --info --text 'Bem vindo: r00t' 1 2>/dev/null && python /opt/mzphp/startphp.py && exit 0
        
        # Perguntar se quer tentar novamente.
        resp=$(zenity --question --width=160 --height=80 --window-icon='error' --text 'Senha incorreta.\nTentar novamente?')
    fi
    # Sair se pressionou cancelar.
    (( $? )) && exit 0
done
