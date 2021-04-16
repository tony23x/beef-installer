#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Code by th3_pr3d4t0r
import time,os,sys,datetime,requests,socket
from colorama import Fore,Style,init
from threading import Thread

red = Fore.RED
gr = Fore.GREEN
cy = Fore.CYAN
b = Fore.BLUE
y = Fore.YELLOW
w = Fore.WHITE
m = Fore.MAGENTA
r = Style.RESET_ALL

check = red + '[' + cy + '✔' + red + ']'
wrn = red + '[' + cy + '!'+ red + ']'
sign = red + '[' + cy + '-' + red + ']'
start = (gr + "[" + cy + "+" + gr + "]" + w)


def tecla():
	os.system('clear')
	time.sleep(3)
	frase = "\n\n\n\x1b[1;32m  Bienvenid@, instalame en tu Home!"
	def entrada():
		try:
			for letra in frase:
				print(letra, end="", flush=True)
				time.sleep(0.099)
		finally:
			pass
	escribir = Thread(target=entrada)
	escribir.start()
	escribir.join()
	time.sleep(5)


def banner():
	logo = """\x1b[0;34m
                          ░▓▒▓░
                           █▒ ▓▓▒
                            █▓  ▒▓▒▒
                             ▓█░  ▒▒▒▓▒
                              ░██░░▓▓▒▒▓
                                ▒█▒ ▓██░░▓
                                  █▓  ██▓ ▓
      ░                   ░▒▒▓▓▓███░  ░███░█▒
      ▓█▓░           ▒▓██████▒░      ░███████
      ░▓ █▒       ▒███▓▓▓▒▒█     ▒▓█████████▓
       █  █▒     ██▓▓▓▒▓▒▒▒▓░▓█████████████▓
       █ ▒ █▒  ▓█▓▒▒▓▓▓▒▒▓▓██████████████▓
       █░█▓ ▒▒▒█▓▒▓▓▓▒▒▓██████████████▓
       ░█▓█▓  ▓█▒▓▓▒▒▒███  ██████████
         ▓██████▒▒▓▒▓██▒  ▒█████████▓
           ░▓▓██▒▒▒▓█████████████████░
              █▓▒▒▓███████████████████
             ▓█▒▒▓███████████████████▓
           ██▓▒▒▒▓▒▓▓████████████████
           ▓███████▓▒▓██████████████
           █▓▓████▓██▒████████████▓
          ██ █████  ██████████▓▒
          ▓█  ░▒░  ▒███████▒
           ▓█▓▓▒▒▓██████▓
             ░▒███████▓
\x1b[00m"""
	print(logo)
	os.system('echo -e "             \e[30;48;5;39m\e[1;31m B E E F  I N S T A L L \e[0m"')

def installT():
	os.system('clear')
	print(gr + "Este script instalara BeEF y sus dependencias requeridas (incluidos los paquetes del sistema operativo)")
	install = input(cy + "Esta seguro de que desea continuar" + w + " (s/n)" + cy + "?" + red + " >>  ")
	if install == "s":
		print(start + y + " Empezamos..." + r)
		time.sleep(3)
		os.system("clear")
		depenT()
		repoT()
		arm64()
		gems()
		ivam3()
		finish()
	elif install == "n":
		print(start + y + " Abortando..." + r)
		time.sleep(2)
		sys.exit()

def installK():
	os.system('clear')
	print (start + gr + "Este script instalara BeEF y sus dependencias requeridas (incluidos los paquetes del sistema operativo)")
	install = input(cy + "Esta seguro de que desea continuar" + w + " (s/n)" + cy + "?" + red + " >>  ")
	if install == "s":
		print(start + y + " Empezamos..." + r)
		time.sleep(3)
		depenK()
		repo()
		gems()
		finish()
	elif install == "n":
		print(start + y + " Abortando..." + r)
		time.sleep(2)
		sys.exit()

def menu():
	os.system('clear')
	banner()
	print ()
	print (red + '[' + cy + '1' + red + ']' '\033[1;36m Termux\033[00m' + red + '     [' + cy + '99' + red + ']' + cy + ' Exit')
	print (red + '[' + cy + '2' + red + ']' '\033[1;36m Kali\033[00m\n')

	choice = int(input("\033[1;31mElige un numero: \033[1;36m"))

	if choice == 1:
		print (sign + cy + ' Ok...\n' + r)
		time.sleep(2)
		installT()
	elif choice == 2:
		print (sign + cy + ' Ok...\n' + r)
		time.sleep(2)
		installK()
	elif choice == 99:
		print ("\n" + sign + cy + ' Goodbye :)\n' + r)
		sys.exit()
	else:
		print(cy + start + " Abortando..." + r)
		sys.exit()

def depenT():
	os.system("clear")
	print(start + gr + " Instalando dependencias..." + r) #Paquetes para errores posibles de gems
	os.system("pkg install -y python python2 git wget curl nano gnupg libiconv pkg-config clang make libffi libyaml libxslt bison espeak zlib zlib-static postgresql libpcap libpcap-static libxslt-static libxml2 libxml2-static libcurl libcurl-static libtool liblzma patch lzlib cmake")
	os.system("apt-get install curl git build-essential openssl sqlite autoconf automake bison nodejs -y")
	os.system("clear")


def repo():
	print(start + gr + " Clonando repo de BeEF..." + r)
	time.sleep(3)
	os.system("git clone https://github.com/beefproject/beef.git /root/beef")
	time.sleep(2)
	os.system("clear")

def repoT():
	print(start + gr + " Clonando repo de BeEF..." + r)
	time.sleep(3)
	os.system("mkdir $PREFIX/opt/ > /dev/null 2>&1")
	os.system("git clone https://github.com/beefproject/beef.git $PREFIX/opt/beef")
	time.sleep(2)
	os.system("clear")

def gems():
	print(start + gr + " Instalando Gemas de Ruby requeridas..." + r)
	os.system('gem install bundler')
	os.system("gem install eventmachine")
	os.system("gem install nokogiri -- --use-system-libraries --with-xml2-config=/data/data/com.termux/files/usr/bin/xml2-config --with-xml2-include=/data/data/com.termux/files/usr/include/libxml2")
	if os.path.exists("$PREFIX/opt/beef/Gemfile"):
		os.system("cd $PREFIX/opt/beef;bundle install")
	if os.path.exists("beef/Gemfile"):
		os.system("cd beef;bundle install")

def arm64():
	os.system("clear")
	time.sleep(2)
	print(start + y + "Tu arquitectura:")
	os.system("dpkg --print-architecture")
	arm = input(cy + "Tu arquitectura es aarch64 o i686" + r + " (s/n)" + cy + "?" + red + " >>  " + r)
	if arm == "s":
		print(start + gr + " Ok" + r)
		os.system("chmod +x depen/aarch64/ruby.deb")
		os.system("cd depen/aarch64/;apt install ./ruby.deb")
		os.system("ruby -v")
		print(y + "Ejecuta:" + w + "  unset LD_PRELOAD" + gr + " pero si ya lo ejecutaste en la siguiente pregunta responde con n" + r)
		time.sleep(10)
		checkArm()
	elif arm == "n":
		print(start + gr + " Ok" + r)
		os.system("chmod +x depen/arm/ruby.deb")
		os.system("cd depen/arm/;apt install ./ruby.deb")
		os.system("ruby -v")
		time.sleep(3)
def checkArm():
	os.system("clear")
	check = input(start + cy + "Lo tienes que ejecutar" + r + " (s/n)" + cy + "?" + red + " >>  " + r)
	if check == "s":
		print(start + gr + " Ponlo y ejecutame de nuevo..." + r)
		os.system("rm -rf beef &> /dev/null")
		time.sleep(2)
		sys.exit()
	elif check == "n":
		print(start + gr + " Ok" + r)
		time.sleep(2)

def ivam3():
	os.system("chmod +x depen/beef")
	os.system("cd depen;./beef")

def depenK():
	os.system("clear")
	print(start + gr + " Instalando dependencias..." + r) #Paquetes para errores posibles de gems
	os.system("apt-get install nano wget curl build-essential openssl sqlite3 libruby -y")
	os.system("apt-get install autoconf libc6-dev libncurses5-dev automake libtool bison nodejs libcurl4-openssl-dev libcurl3-dev libsqlite3-dev libpcap-dev libpq-dev zlib1g-dev libssl-dev libreadline-dev libyaml-dev libxml2-dev libxslt-dev ruby-eventmachine libgmp-dev libgmp3-dev libev-dev ruby-nio4r ruby-nokogiri liblzma-dev patch -y")
	os.system("apt-get install libreadline6-dev zlib1g zlib1g-dev libssl-dev libyaml-dev libsqlite3-0 libsqlite3-dev libxml2-dev libxslt1-dev libc6-dev libncurses5-dev gcc-9-base libgcc-9-dev ruby-em-websocket ruby-em-http-request libc-ares2 libnode64 libuv1 nodejs-doc libgmpxx4ldbl ruby2.7-dev ruby2.7-doc thin ruby-sinatra ruby-curb -y")

def finish():
	time.sleep(2)
	os.system("clear")
	print("")
	print(red + "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#" + r )
	print("")
	print(w + "Instalacion completada exitosamente!" + r)
	print(w + "Entre al directorio de beef en su home o en Termux en $PREFIX/opt/beef y ejecute" + r)
	print(gr + " ./beef " + w +  "para lanzar BeEF" + r)
	print("")
	print(w + "Proximos pasos:" + r)
	print("")
	print(w + "* Cambie la clave por defecto en config.yaml" + r)
	print(w + "* Ejecuta ./update-geoipdb para instalar el Maxmind GeoIP database" + r)
	print(w + "* Revise la wiki para obtener informacion importante de configuracion:" + r)
	print(w + "https://github.com/beefproject/beef/wiki/Configuration" + r)
	print("")
	print(red + "#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#" + r)
	print("")

def wifi():
	try:
		socket.gethostbyname("google.com")
		conexion = socket.create_connection(("google.com", 80), 1)
		conexion.close()
		print (check + red + ' [' + cy + 'Internet Connection' + red + ']' + cy + '............' + red + '[' + cy + ' OK ' + red + ']')
		time.sleep(4)
	except socket.error:
		print (wrn + red + ' [' + cy + 'Internet Connection' + red + ']' + cy + '............' + red + '[' + cy + ' NOT FOUND  ' + red + ']')
		time.sleep(2)
		sys.exit()

try:
	conexion = wifi()
	print(conexion)
	tecla()
	menu()
except KeyboardInterrupt:
	print ("\n" + wrn + y + " Proceso interumpido por el usuario!")
