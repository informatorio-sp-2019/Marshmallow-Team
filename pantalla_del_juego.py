import incognita
import animacionahorcado
import tabla_de_letras_utilizadas
from colorama import Fore, init
from os import system
init(autoreset=True)

def pantalla():
	system("cls")
	palabra = incognita.incognita1()
	print(palabra)

	posicion=0
	animacionahorcado.recorrer(posicion)
	incognita.mostrar_Lista()
	while True:

		letra = incognita.ingresa_Letra()
		letra2=letra.lower()
		incognita.buscar_y_Remplazar(letra,palabra)
		incognita.mostrar_Lista()
	
		if letra in palabra:
			tabla_de_letras_utilizadas.letras_utilizadas(Fore.GREEN + letra)
			animacionahorcado.recorrer(posicion)
		else:
			posicion+=1
			tabla_de_letras_utilizadas.letras_utilizadas(Fore.RED + letra)
			animacionahorcado.recorrer(posicion)

		tt="Letras usadas"
		print(tt.center(60,"+"))
		tabla_de_letras_utilizadas.mostar_Letras_Usadas()
		print("\n+"+"+"*60)

		if posicion == 6:
			system("cls")
			print("perdiste")
			break