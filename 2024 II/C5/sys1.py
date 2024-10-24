
## Array - Tuplas - Listas - Diccionarios 

"""
 int Arreglo[10]

Arreglo[0] = 5;
Arreglo[5] = 10;

"""

## Listas

print(" Listas \n")

variable = 1
arreglo = [ 1 , 2, 3, 4, 5, 6, 7, 8, 9]

print(" Arreglo = ",  arreglo)

## append() agrega un dato adicional en la lista

arreglo.append(15)
print(" append() Arreglo = ",  arreglo)

## copy() copia todos los elementos de la lista

arreglo_copy = arreglo.copy()
print(" copy() Arreglo = ",  arreglo_copy)

## count() Cuenta los elementos de la lista definidos en la consulta 

arreglo = [ 1 , 1, 2, 2, 3, 4, 4, 4, 4, 20]

arreglo_count = arreglo.count(4)
print(" count() Arreglo = ",  arreglo_count)

## extend() concatenar los elementos de dos listas.

arreglo.extend(arreglo_copy)
print(" extend() Arreglo = ",  arreglo)

## index() buscar el valro indicado en la lista y retorna la posicion.

arreglo_index = arreglo.index(20)
print(" index() Arreglo = ",  arreglo_index)

## insert() reemplaza el valor del arguento en la posicion indicada en la lista

arreglo.insert(10, 50)
print(" insert() Arreglo = ",  arreglo)

## pop() elimina el dato de la posicion inidcada en la lista

arreglo.pop(11)
print(" pop() Arreglo = ",  arreglo)

## remove() elimina el dato de la posicion indicada de la lista 

arreglo.remove(4)
print(" remove() Arreglo = ",  arreglo)

## reverse() invierte los datos en la lista

arreglo.reverse()
print(" reverse() Arreglo = ",  arreglo)

## sort() relizar el ordenamiento de menor a mayor. 
## Se puede cambiar el contexto de la fucnion con los argumentos sort(argumentos)

A = arreglo.copy() 
B = arreglo.copy()

A.sort()
print(" sort() Arreglo = ",  A)

B.sort(reverse=True)
print(" sort() Arreglo = ",  B)

## Funcion len --> Retoamr el numero de elementos de la lista

size = len(arreglo)
print(" len() size = ",  size)

## clear() borra todos los elementos de la lista

arreglo.clear()
print(" clear() Arreglo = ",  arreglo)

## ejemplos.

print(" \n\n ")

arreglo = []

for i in range(10):
    arreglo.append(i*2)

print(" Arreglo = ",  arreglo)

arreglo.clear()

arreglo = [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(10):
    arreglo[i] = 2 * i

print(" Arreglo = ",  arreglo)

## Encontrar el numero maximo o minimo de un lista

from random import *

for i in range(10):
    arreglo[i] = randint(0,100)

print(" Arreglo = ",  arreglo)

size = len(arreglo)

max = None

for i in range(size):
    if (max == None) or (max < arreglo[i]):
        max = arreglo[i]

print(" El valor maximo de la lista es igual = ",  max)

min = None

for i in range(size):
    if (min == None) or (min > arreglo[i]):
        min = arreglo[i]

print(" El valor minimo de la lista es igual = ",  min)


