# Ejercicio 2
# Ordena matrices de números aleatorios con distintas funciones de ordenación 
# y compara el tiempo que tardan en ejecutarse

import random
import time

def burbuja(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz)-i-1):
			if matriz[j] > matriz[j+1]:
				aux = matriz[j]
				matriz[j] = matriz[j+1]
				matriz[j+1] = aux
	return matriz

def seleccion(matriz):
	for i in range(len(matriz)):
		mini = min(matriz[i:]) #find minimum element
		min_index = matriz[i:].index(mini) #find index of minimum element
		matriz[i + min_index] = matriz[i] #replace element at min_index with first element
		matriz[i] = mini                  #replace first element with min element
	return matriz


# Generamos un vector de enteros de tamaño 100
lista = [int(100*random.random()) for i in range(100)]

print ("Lista:")
print (lista)
print ("")

# Mostramos los resultados
print("Ordenando...")


inicio = time.time()
listaBurbuja=burbuja(lista[:])
fin = time.time()
print ("Burbuja - Ha tardado: " + str(fin - inicio) + " segundos")

print ("Lista ordenada mediante Burbuja:")
print (listaBurbuja)
print ("")

inicio = time.time()
listaSeleccion=seleccion(lista[:])
fin = time.time()
print ("Selección - Ha tardado: " + str(fin - inicio) + " segundos")

print ("Lista ordenada mediante Selección:")
print (listaSeleccion)
print ("")