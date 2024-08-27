
## Array - Tuplas - Listas - Dicionarios.

## Listas.

Variable = 1

Arreglo = [1, 2, 1, 4, 5, 6, 7, 8, 9, 10]

print("Arreglo de entrada = ",Arreglo)

## append() agrega un dato adicional en el la lista(array)
Arreglo.append(20)

print("append()",Arreglo)

## copy() copia todos los elementos de la lista(array)

Arreglo_cpy = Arreglo.copy()

print("copy()",Arreglo_cpy)

## count() cuenta los elementos de la lista definidos en la consulta(array)

Arreglo_count =  Arreglo.count(1)

print("count()",Arreglo_count)

## extend() concatenar los elementos de dos listas

Arreglo.extend(Arreglo_cpy)

print("extend()",Arreglo)

## index() buscar el valor indicado en la lista y retorna la posicion

index = Arreglo.index(7)

print("index()",index)

## insert() reemplaza el valor del argumento en la posicion indicado en la lista

Arreglo.insert(7, 50)

print("insert()",Arreglo)

## pop() elimina el dato de la posicion indicada en la lista

Arreglo.pop(7)

print("pop()",Arreglo)

## remove() elimina el dato de la posicion indicada en la lista

Arreglo.remove(10)

print("remove()",Arreglo)

## remove() invierte los datos en la lista

Arreglo.reverse()

print("reverse()",Arreglo)

## sort() realiza el ordenamiento de mayor a menor 
## Se puede cambiar el contexto de la funcion con los argumentos sort(argumento)

Arreglo.sort()

print("sort()",Arreglo)

## clear() borra todos los elementos de la lista(array)

Arreglo.clear()

print("clear()",Arreglo)


Arreglo = [10, 22, 13, 4, 50, 67, 47, 28, 29, 15]
Arreglo.reverse()

## Leer el arreglo

## Funcion len --> Me retorna el nuemro de datos de la lista
size = len(Arreglo)
## print(len(Arreglo))

for i in range(size):
    print("Arreglo[",i,"] = ", Arreglo[i])

max = None

for i in range(size):
    if (max == None) or (max < Arreglo[i]):
        max = Arreglo[i]

print("El valor maximo del arreglo es igual = ", max)

min = None

for i in range(size):
    if (min == None) or (min > Arreglo[i]):
        min = Arreglo[i]

print("El valor minimo del arreglo es igual = ", min)

Arreglo_ordenamiento = []

for i in range(size):

    min = None

    for j in range(len(Arreglo)):

        if (min == None) or (min > Arreglo[j]):
            min = Arreglo[j]
            
    Arreglo.remove(min)
    Arreglo_ordenamiento.append(min) 

print(Arreglo_ordenamiento)

Arreglo = [10, 22, 13, 4, 50, 67, 47, 28, 29, 15]
Arreglo.reverse()

Arreglo_ordenamiento = []

for i in range(size):

    max = None

    for j in range(len(Arreglo)):

        if (max == None) or (max < Arreglo[j]):
            max = Arreglo[j]

    Arreglo.remove(max)
    Arreglo_ordenamiento.append(max) 

print(Arreglo_ordenamiento)