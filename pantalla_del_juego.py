import incognita
import animacionahorcado
import tabla_de_letras_utilizadas
from colorama import Fore, init
from os import system
from winsound import *
import random
import time
import threading
init(autoreset=True)
posicion=0
def gana(a):
	r=""
	for i in a:
		r += i
	return r



def tabla():
	
	tt="Letras usadas"
	print(  tt.center(60,"▄")+"\n")
	if tabla_de_letras_utilizadas.mostar_Letras_Usadas() == None:
		pass
	else:
		tabla_de_letras_utilizadas.mostar_Letras_Usadas()
	print("\n\n▄" + "▄"*59)

def vidas(a):
	return ("\n"+("Vidas:	").rjust(13,"	")+Fore.RED+"♥ "*a)


def temporizador():
	global posicion
	t=15
	while t:
		time.sleep(1)
		t -= 1
		if t == 0:
			posicion+=1
		elif t <= 5:
			Beep(1500,200)
			Beep(1500,200)

def pantalla(a,puntos,musica):
	global posicion
	posicion = 0
	system("cls")
	palabra,ls = incognita.incognita1()
	print(palabra)
	print(vidas(a))
	animacionahorcado.recorrer(posicion)
	incognita.mostrar_Lista()
	print("\n"+("Puntos:	").rjust(14,"	"),puntos)
	print("\n"+("Tiempo:	").rjust(14,"	"))
	tabla()
	if musica=="on":
		PlaySound('prueba.wav',SND_LOOP | SND_ASYNC)
		pass
	while True:

		threading.Thread(target=temporizador).start()
		letra = incognita.ingresa_Letra()
		
		if len(letra) == 1 and letra.isalpha() == True:

			letra=letra.lower()
			system("cls")
			pass
		#Pista
		elif letra=="?":
			pista = random.choice(palabra)
			letra=pista
			puntos -= 2
		
		elif letra == "on":
			musica = "on"
			PlaySound('prueba.wav',SND_LOOP | SND_ASYNC)
			system("cls")
			pass
		
		elif letra == "off":
			musica="off"
			PlaySound('*',SND_ALIAS | SND_ASYNC)
			system("cls")
			pass
		else:

			continue

		lista2=incognita.buscar_y_Remplazar(letra,palabra) 
		print(vidas(a))
	
		if letra in palabra:

			lista_de_tablas =tabla_de_letras_utilizadas.letras_utilizadas(Fore.GREEN + letra)
			animacionahorcado.recorrer(posicion)
			if palabra == gana(ls):
				puntos = puntos + 5
				lista_de_tablas = lista_de_tablas.clear()
				lista2 = lista2.clear()
				PlaySound("ganaste.wav",SND_ASYNC)
				pantalla(a,puntos)
		else:
			posicion+=1
			lista_de_tablas = tabla_de_letras_utilizadas.letras_utilizadas(Fore.RED + letra)
			animacionahorcado.recorrer(posicion)

		incognita.mostrar_Lista()
		print("\n"+("Puntos:	").rjust(14,"	"),puntos)
		print("	"*21+"Tiempo:	")
		tabla()

		if posicion == 5:
			a -= 1
			posicion = -1
			continue

		if a == 0:
			system("cls")

			print(""".______    _______ .______       _______   __       _______..___________. _______ 
|   _  \  |   ____||   _  \     |       \ |  |     /       ||           ||   ____|
|  |_)  | |  |__   |  |_)  |    |  .--.  ||  |    |   (----``---|  |----`|  |__   
|   ___/  |   __|  |      /     |  |  |  ||  |     \   \        |  |     |   __|  
|  |      |  |____ |  |\  \----.|  '--'  ||  | .----)   |       |  |     |  |____ 
| _|      |_______|| _| `._____||_______/ |__| |_______/        |__|     |_______|""")
			PlaySound("perdiste.wav",SND_ASYNC)
			lista_de_tablas = lista_de_tablas.clear()
			lista2 = lista2.clear()
			while True:
				salir=input("\n	1-Salir:  \n	2- Reiniciar: ")
				if salir =="1":
					break
				elif salir =="2":
					pantalla(3,0)
			break		
	import H1_menu_principal
	H1_menu_principal.iniciar()