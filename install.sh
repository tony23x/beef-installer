#!/bin/bash

banner1() {
clear
sleep 1
echo -e """\033[1;35m
########  ######## ######## ########
##     ## ##       ##       ##
##     ## ##       ##       ##
########  ######   ######   ######
##     ## ##       ##       ##
##     ## ##       ##       ##
########  ######## ######## ##
"""
}

if [ ! -d ~/storage ]; then
        termux-setup-storage
fi


wifi(){
ping -c 1 google.com > /dev/null 2>&1
if [[ "$?" -le 1 ]]; then
echo -e "\n\033[1;36m[✔]\033[00m \033[1;31m[\033[1;36mInternet Connection\033[1;31m]\033[1;36m............\033[1;31m[\033[1;36m OK \033[1;31m]\n"
echo
sleep 7
else
echo -e "\n\033[1;36m[✔]\033[00m \033[1;31m[\033[1;36mInternet Connection\033[1;31m]\033[1;36m............\033[1;31m[\033[1;36m NOT FOUND \033[1;31m]\n"
echo
sleep 1
exit
fi
}


if [ -e /data/data/com.termux/files/usr/bin ]; then
wifi
banner1
echo -e "\033[1;35mActualizando Termux :3\033[00m\n"
pkg update && pkg upgrade -y
echo -e "\033[1;35mInstalando paquetes...\033[00m"
pkg install -y python
echo -e "\033[1;35mInstalando modulos de python3...\033[00m"
pip install --upgrade pip
pip install -r requirements.txt
echo -e "\033[1;35mListo!, ejecuta \033[1;32mpython3 beef-installer.py\033[00m"
sleep 1
else
apt install iputils-ping -y &> /dev/null
sleep 1
wifi
banner1
echo -e "\033[1;36mActualizando :3\033[00m\n"
apt update && sudo apt upgrade -y
echo -e "\033[1;35mInstalando paquetes...\033[00m"
apt install python3 python3-pip -y
echo -e "\033[1;35mInstalando modulos de python3...\033[00m"
python3 -m pip install -r requirements.txt
echo -e "\033[1;35mListo!, ejecuta: \033[1;32mpython3 beef-install.py\033[00m\n\n"
sleep 1
fi
