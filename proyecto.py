#!/usr/bin/python
# *-* coding: utf-8 *-*

import subprocess
import sys
import os
import os.path
import commands
import shutil

def ordenar():
	#source = sys.argv[1]
	#destination = sys.argv[2]
	source = raw_input("ruta de archivos origen  \t")
	destination = raw_input("ruta de archivos destino  \t")

	while not os.path.exists(source):
	    source = raw_input('Ingrese un directorio fuente valida: \n')
	while not os.path.exists(destination):
	    destination = raw_input('Ingrese un directorio de destino valido: \n')

	for root, dirs, files in os.walk(source, topdown=False):
	    for file in files:
		extension = os.path.splitext(file)[1][1:].upper()
		destinationPath = os.path.join(destination,extension)
	  	
		if not os.path.exists(destinationPath):
		    os.mkdir(destinationPath)
		if os.path.exists(os.path.join(destinationPath,file)):
		    print 'advertencia: este archivo no fue copiado :' + os.path.join(root,file)
		else:
		    shutil.copy2(os.path.join(root,file), destinationPath)
#Agradecimientos a la pagina https://www.cgsecurity.org/wiki/Luego_De_Usar_PhotoRec

def recupera():	
	"""Lista los dispositivos USB"""
	os.system("lsblk | grep sdb")
	os.system("lsblk | grep sdc")
	nombreusb=raw_input("Escriba el nombre del dispositivo a examinar \t")
	USB= '/dev/'+nombreusb
	print ("\033[1;32m"+"USB elegida  "+ USB)
	print ("\033[1;32m"+"Sacando imagen del dispositivo")
	print ("\033[1;37m")
	"""Creamos una Imagen """
	os.system('dd if='+USB+' '+'of=recuperacion.dd')
	os.system("lsblk | grep sdb")
	rutarecuperacion=raw_input("Escriba la ruta del dispositivo para guardar los archivos  \t")
	rutaimagen=commands.getoutput("pwd")
	print(rutaimagen)
	invocar="photorec /debug /d"+" "+rutarecuperacion+"/"+" "+ "/log /cmd"+" " + rutaimagen +"/recuperacion.dd" +" "+ "options,mode_ext2,5,search" 
	os.system(invocar)
	print(invocar)
	
	
def mostrar():
	os.system("lsblk")
	usuario = raw_input("Escriba el dispositivo \t")
	rutamem="/dev/"+ usuario
	os.system("xxd"+" " +rutamem + " "+"/root/Escritorio/Interior.txt")

def esterilizacion():
	#os.system("gnome-terminal -- sh -c 'python proyecto.py -e' & disown")
	cantidad=int(input("Digite el numero de usb a esterilizar (1 o 2) \t"))
	if cantidad == 1:
		"""Lista los dispositivos USB"""
		os.system("lsblk | grep sdb")
		os.system("lsblk | grep sdc")
		devname=raw_input("Escriba el nombre del dispositivo  \t")
		USB= '/dev/'+devname
		
		for i in range(3):
			print ("\033[1;32m"+"Ceros y aleatorios "+ str(i+1)  +" vez")
			print ("\033[1;37m")
			os.system("dd if=/dev/urandom of="+USB+" bs=1024")
			os.system("dd if=/dev/zero of="+USB+" bs=1024")
			
		os.system("umount "+USB)
		os.system("mkfs.vfat "+USB)
		#os.system("mount "+USB)
		
	if cantidad == 2:
		"""Lista los dispositivos USB"""
		os.system("lsblk | grep sdb")
		os.system("lsblk | grep sdc")
		devname=raw_input("Escriba el nombre del primer dispositivo  \t")
		devname1=raw_input("Escriba el nombre del segundo dispositivo  \t")
		USB= '/dev/'+devname
		USB1= '/dev/'+devname1

		for i in range(3):
			print ("\033[1;32m"+"Ceros y aleatorios "+ str(i+1)  +" vez")
			print ("\033[1;37m")
			os.system("dd if=/dev/zero of="+USB+" bs=1024")
			os.system("dd if=/dev/urandom of="+USB+" bs=1024")
			os.system("dd if=/dev/zero of="+USB1+" bs=1024")
			os.system("dd if=/dev/urandom of="+USB1+" bs=1024")

		os.system("umount "+USB)
		os.system("mkfs.vfat "+USB)
		os.system("umount "+USB1)
		os.system("mkfs.vfat "+USB1)

def metadatos():	
	"""Invocar el comando para ver metadatos"""
	rutaAnalisis=raw_input("Escriba la ruta del archivo a analizar  \t")
	invocar="exiftool"+" "+rutaAnalisis
	md5 ="md5sum"+" "+rutaAnalisis
	md5Imagen = commands.getoutput(md5)
	#os.system(invocar)
	rutaReporte=commands.getoutput(invocar)
	#print(rutaReporte)
	Investigador=raw_input("Escriba el nombre del investigador:   \t")
	f=open("InformeMD.txt","a")
	f.write("\nInvestigador: "+Investigador+"\n")
	f.write("\nmd5: "+md5Imagen+"\n")
	f.write(rutaReporte)
	f.close()
	programaPausa=raw_input("presione enter para continuar")

def bandera(tamanoban):
	if tamanoban == 1:
		return "Consulte la bandera -h para mas informacion"
	if tamanoban == 2:
		var=ayuda(sys.argv[1])
		return var

def ayuda(band):

	print("Aplicacion que se encarga de la recuperacion y esterilizacion de los archivos de una memoria USB")
	if band=="-h":
		mensaje= '-h: Contiene la informacion de como usar el script' +"\n"+ "-r: Recuperacion de Archivos" + '\n' + "-e: Esterilizacion del medio"+ '\n' + "-o: Ordenar archivos recuperados"'\n' + "-md: Mostrar metadatos de un Archivo"+ '\n' + "-m: Mostrar contenido hexadecimal de la USB"
		return mensaje
	if band=="-r":
		print("Recuperacion de archivos")
		recupera()
	if band=="-e":
		print("Esterilizacion del Medio")
		esterilizacion()
	if band=="-o":
		print("Ordenar archivos recuperados")
		ordenar()
	if band=="-md":
		print("Ver metadatos de un arhivo")
		metadatos()
	if band=="-m":
		print("Ver contenido hexadecimal de USB")
		mostrar()
	
tamanoban= len(sys.argv)
mensaje= bandera(tamanoban)
print mensaje


#while 1: # Bucle infinito
#	subprocess.call("clear")
#	print("Elige una opcion")
#	print("***********************************")
#	print(" 1) - Esterilizar")
#	print(" 2) - Recuperar archivos")
#	print(" 0) - Salir del programa")
#	print("***********************************")
#	opcion=int(input("¿Que opcion deseas escoger? "))
	
#	subprocess.call("clear")
	
#	if opcion == 0:
#		sys.exit(0)
#	elif opcion == 1:
		#esterilizar()
	#elif opcion == 2:
		#recupera()
	
