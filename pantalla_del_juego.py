import incognita
import animacionahorcado
import tabla_de_letras_utilizadas
from colorama import Fore, init
from os import system
init(autoreset=True)

def gana(a):
	r=""
	for i in a:
		r += i
	return r


def tabla():
	tt="Letras usadas"
	print("\n\n" + tt.center(60,"▄")+"\n")
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

def pantalla(a):
	posicion = 0
	system("cls")
	palabra,ls = incognita.incognita1()
	print(palabra)
	print(vidas(a))

	animacionahorcado.recorrer(posicion)
	incognita.mostrar_Lista()
	tabla()

	while True:

		letra = incognita.ingresa_Letra()
		# countdown(20)
		if len(letra) == 1 and letra.isalpha() == True:

			letra=letra.lower()
			system("cls")
			pass
		else:

			continue

		incognita.buscar_y_Remplazar(letra,palabra)
		print(vidas(a))
	
		if letra in palabra:

			tabla_de_letras_utilizadas.letras_utilizadas(Fore.GREEN + letra)
			animacionahorcado.recorrer(posicion)
			if palabra == gana(ls):
				print("ganaste")
		else:
			posicion+=1
			tabla_de_letras_utilizadas.letras_utilizadas(Fore.RED + letra)
			animacionahorcado.recorrer(posicion)

		incognita.mostrar_Lista()
		tabla()

		if posicion == 5:
			a -= 1
			posicion = -1
			continue

		if a == 0:
			print("\n\n\n\n\n			perdiste")
			input()
			break
	import H1_menu_principal
	H1_menu_principal.iniciar()