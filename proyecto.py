#!/usr/bin/python
# *-* coding: utf-8 *-*

import subprocess
import sys
import os
import commands

def recupera():	
	"""Lista los dispositivos USB"""
	os.system("lsblk | grep sdb")
	nombreusb=raw_input("Escriba el nombre del dispositivo a examinar \t")
	USB= '/dev/'+nombreusb
	"""Creamos una Imagen """
	os.system('dd if='+USB+' '+'of=recuperacion.dd')
	os.system("lsblk | grep sdb")
	rutarecuperacion=raw_input("Escriba la ruta del dispositivo para guardar los archivos  \t")
	rutaimagen=commands.getoutput("pwd")
	invocar="photorec /debug /d"+" "+rutarecuperacion+"/"+" "+ "/log /cmd"+" " + rutaimagen +"/recuperacion.dd" +" "+ "options,mode_ext2,5,search" 
	os.system(invocar)

	


def esterilizar():
	"""Lista los dispositivos USB"""
	os.system("lsblk | grep sdb")
	devname=raw_input("Escriba el nombre del dispositivo  \t")
	USB= '/dev/'+devname

	for i in range(3):
		os.system("dd if=/dev/zero of="+USB+" bs=1024")
		os.system("dd if=/dev/urandom of="+USB+" bs=1024")

	os.system("umount "+USB)
	os.system("mkfs.vfat "+USB)
	#imgname=raw_input("Escriba el nombre de la imagen \n")
	#os.system("dd if="+USB+" of=imagenEsterilizada.dd")


while 1: # Bucle infinito
	subprocess.call("clear")
	print("Elige una opcion")
	print("***********************************")
	print(" 1) - Esterilizar")
	print(" 2) - Recuperar archivos")
	print(" 0) - Salir del programa")
	print("***********************************")
	opcion=int(input("¿Que opcion deseas escoger? "))
	
	subprocess.call("clear")
	
	if opcion == 0:
		sys.exit(0)
	elif opcion == 1:
		esterilizar()
	elif opcion == 2:
		recupera()
	
