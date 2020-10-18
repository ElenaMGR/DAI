# Ejercicio 1
# Adivina un número entre 1 y 100

import random

r = random.randint(1,100)

print("Mini-juego de adivinar un número entre 1 y 100")
find = False

for i in range(10):
    n = int (input ("Introduzca un número del 1 al 100: "))

    if n > 100 or n < 1:
        print ("El número tiene que estar en el rango [1-100].")
    elif n == r:
        find = True
        print("Valor encontrado!!!!")
        break
    elif n > r:
        print("El número buscado es menor que " + str(n))
    elif n < r:
        print("El número buscado es mayor que " + str(n))

if not find:
    print("¡Lo siento! No has conseguido adivinar el número tras 10 intentos.")
    print("El número era " + str(r) + "!")