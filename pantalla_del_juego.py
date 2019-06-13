import incognita
import animacionahorcado
import tabla_de_letras_utilizadas
from colorama import Fore, init
from os import system
from winsound import *
import random
init(autoreset=True)

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
	return "	"*20+"vidas:	"+Fore.RED+"♥ "*a


def temporizador(t):
	import time
	while t:
		mins, secs = divmod(t,60)
		timeformat = '{:02d}:{:02d}'.format(mins, secs)
		print(timeformat, end='\r')
		time.sleep(1)
		t -= 1
	print('Goodbye!\n\n\n\n\n')

def pantalla(a,puntos):
	posicion = 0
	system("cls")
	palabra,ls = incognita.incognita1()
	print(palabra)
	print(vidas(a))
	animacionahorcado.recorrer(posicion)
	incognita.mostrar_Lista()
	print("\n"+("Puntos:	").rjust(14,"	"),puntos)
	print("	"*21+"Tiempo:	")
	tabla()
	while True:

		letra = incognita.ingresa_Letra()
		# countdown(20)
		


		if len(letra) == 1 and letra.isalpha() == True:

			letra=letra.lower()
			system("cls")
			pass
		#Pista
		elif letra=="?":
			pista = random.choice(palabra)
			letra=pista
			puntos -= 2
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