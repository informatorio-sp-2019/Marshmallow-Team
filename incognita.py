#importamos la libreria random para poder elegir utilizar una funcion que eliga una palabra aleatoriamente
import random
lista = []
#funcion incognita
def incognita1():
	#lista de palabras
	lista_de_palabras=['alberto','albina','alejandro','alejo','alfonso','alfredo','alicia','alipio','almudena','alonso']
	#funcion que elige una palabra de la lista aleatoriamente
	palabra = random.choice(lista_de_palabras)
	#se calcula la longitud de la palabra
	longitud = len(palabra)
	#agregamos guiones bajos a una lista vacia(la cantidad de guiones que se agregan corresponde a la longitud de la palabra)
	for x in palabra:
		lista.append("_")
	return palabra
#muestra la lista que generamos con la cantidad de guiones que corresponde a la longitud de la palabra 
def mostrar_Lista():
	for i in lista:
		print(i,end=' ')
#pide al usuario ingresar una letra
def ingresa_Letra():
	letra = input("\n\nIngresar una letra: ")
	#devolvemosla letra que ingreso el usuario
	return letra
	
#busca y reemplaza los giones bajos por la letra en el lugar que corresponde
def buscar_y_Remplazar(letra,palabra):
	#contador para guardar la posicion
	posicion = 0
	#recorremos la palabra
	for l in palabra:
		#si l es igual a letra 
		if l == letra:
			#se reemplaza en la lista el guion por la letra en la posicion que corresponde
			lista[posicion]=letra
		#incrementamos el contador
		posicion+=1

lista = []

	
