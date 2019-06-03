import incognita
import animacionahorcado
import tabla_de_letras_utilizadas
from colorama import Fore, init
init(autoreset=True)

def pantalla():

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
		else:
			posicion+=1
			tabla_de_letras_utilizadas.letras_utilizadas(Fore.RED + letra)
			animacionahorcado.recorrer(posicion)
	
		print("\n\n+++++++++++++++++++++++++++++++++++++++++++")
		print("Letras usadas:")
		tabla_de_letras_utilizadas.mostar_Letras_Usadas()
		print("\n+++++++++++++++++++++++++++++++++++++++++++")