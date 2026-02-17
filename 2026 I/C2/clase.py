
# Condicionales en python

## Operadores de comparación.
"""
| Operador   |      | Descripcion               |
|------------|:----:|:------:                   |
| x == y     | -->  | x es igual que y          |
| x != y     | -->  | x es distinto de y        |
| x > y      | -->  | x es mayor que y          |
| x < y      | -->  | x es menor que y          |   
| x >= y     | -->  | x es mayor o igual que y  |   
| x <= y     | -->  | x es menor o igual que y  |
| x is y     | -->  | x es lo mismo que y       |
| x is not y | -->  | x no es lo mismo que y    |
"""
varable_A = 50
variable_B = 50

booleno = (varable_A != variable_B)
print('estado = ', booleno)

# if, elif, else

if varable_A > variable_B:
    print   ('variable A es mayor que variable B')
    
if varable_A > variable_B:
    print   ('variable A es mayor que variable B')
elif varable_A < variable_B:
    print   ('variable A es menor que variable B')
 
if varable_A > variable_B:
    print   ('variable A es mayor que variable B')
else:
    print   ('variable A es igual a variable B')  

if varable_A > variable_B:
    print   ('variable A es mayor que variable B')
elif varable_A < variable_B:
    print   ('variable A es menor que variable B')
else:
    print   ('variable A es igual a variable B')               

## Operadores de logicos. 
"""
| Operador      |          | Descripcion                    |
|----------     |:--------:|:------:                        |
| x and y       | -->      | operacion logica and entre x,y |
| x or y        | -->      | operacion logica or entre x,y  |
| not x         | -->      | operacion logica not para x   |
"""
""""
Primera Infancia (0-5 años): Fases iniciales del desarrollo.
Infancia (6-11 años): Niñez media.
Adolescencia (12-18 años): Transición a la juventud.
Juventud (14-26 años): Etapa enfocada en participación y fortalecimiento social, cultural y político.
Adultez (27-59 años): Población activa y mayoritaria.
Vejez (60 años y más): Incluye a la población adulta mayor. 
"""

# input = input('Ingrese su edad: ')
# edad = int(input)   

edad = int(-10)

if edad >= 0 and edad <= 5:
    print('Primera Infancia')
elif edad >= 6 and edad <= 11:
    print('Infancia')
elif edad >= 12 and edad <= 26:
    if edad >= 12 and edad <= 18:
        print('Adolescencia')
    if edad >= 14 and edad <= 26:
        print('Juventud')
elif edad >= 27 and edad <= 59:
    print('Adultez')      
elif edad >= 60:                  
    print('Vejez')  

# Captura de excepciones usando try y except
"""
try:
	# Codigo a ejecutar
	# Pero podria haber errores en este bloque
except <tipo de error>:
	# Haz esto para manejar la excepcion
	# El bloque except se ejecutara si el bloque try lanza un erro
else:
	# Esto se ejecutara si el bloque try se ejecuta sin errores
finally:
	# Este bloque se ejecutara siempre
"""

try:
    input = input('Ingrese su edad : ')
    edad = int(input)
except ValueError:
    print('Error: Debe ingresar un numero entero para la edad')
else: 
    if edad >= 0 and edad <= 5:
        print('Primera Infancia')
    elif edad >= 6 and edad <= 11:
        print('Infancia')
    elif edad >= 12 and edad <= 26:
        if edad >= 12 and edad <= 18:
            print('Adolescencia')
        if edad >= 14 and edad <= 26:
            print('Juventud')
    elif edad >= 27 and edad <= 59:
        print('Adultez')      
    elif edad >= 60:                  
        print('Vejez')
finally:
    print('Programa finalizado')
