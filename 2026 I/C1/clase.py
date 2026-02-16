
print("Bienvenido a la clase de Python A \n")
print('Bienvenido a la clase de Python B\n')

## Tipos de variables en Python

# Variables de tipo entero

# Declaración de una variable entera

variable = 10
print("La variable entera es:", variable)
print("El tipo de variable_entera es:", type(variable))

# Declaración de una variable flotante   

variable = 10.5
print("La variable flotante es:", variable)
print("El tipo de variable_flotante es:", type(variable))

# Declaración de una variable cadena de texto  

variable = 'Hola Mundo'
print("La variable cadena de texto es:", variable)
print("El tipo de variable_cadena es:", type(variable))

## Operacaiones en Python.

# Suma

a = 80
b = 50
suma = a + b
print("La suma de a y b es:", suma)
print("El tipo de variable:", type(suma))
    
# Resta

a = 80
b = 50
resta = a - b
print("La resta de a y b es:", resta)
print("El tipo de variable:", type(resta))

# multiplicación

a = 80
b = 50
multiplicacion = a * b
print("La multiplicación de a y b es:", multiplicacion)
print("El tipo de variable:", type(multiplicacion))

# División
a = 80
b = 50          
division = a / b
print("La división de a y b es:", division)
print("El tipo de variable:", type(division))

a = 80
b = 50          
division = int(a / b)
print("La división de a y b es:", division)
print("El tipo de variable:", type(division))

a = 80
b = 50          
division = a // b
print("La división de a y b es:", division)
print("El tipo de variable:", type(division))

# Modulo.
a = 80
b = 50          

modulo = a % b
print("El módulo de a y b es:", modulo) 
print("El tipo de variable:", type(modulo))

## Jerarquia de las operaciones.

## y = mx + b
## y = (10)(2) + 5

m = 10
x = 2
b = 5 

y =  (m * x) + b

print('Pendiente = ', m,'variable = ', x, 'Punto de corte = ', b)
print ('y = mx + b =','(', m,'*',x,')','+',b,'=', y )

## Ingreso de datos en python.

variable_A = input('Digite el valor de la variable A = ') 
variable_B = input('Digite el valor de la variable B = ')

A = int(variable_A)
B = int(variable_B)

print('El resultado de la suma es =', A + B)

## Realizar un algortimo que ingrese Vcc, R1 y R2.
## Calcule un divisor de voltaje.