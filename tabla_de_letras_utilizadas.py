
lista = []
def letras_utilizadas(letra):
	lista.append(letra)
	return lista
	
def mostar_Letras_Usadas():
	for i in lista:
		print(i,end='-')