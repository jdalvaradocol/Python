
print("Bienvenido a Python \n")

## Tipos de variables en Python

print("Variables tipo int \n")

variable1 = 456
print("Variable =",variable1,"Tipo",type(variable1),"\n")

print("Variables tipo float \n")

variable1 = 456.78
print("Variable =",variable1,"Tipo",type(variable1),"\n")

print("Variables tipo str \n")

variable1 = 'Hola mundo'
print("Variable =",variable1,"Tipo",type(variable1),"\n")

## Operaciones en Python

variable1 = 123
variable2 = 100

salida = variable1 + variable2
print("Resultado de la operacion = ",salida,"Tipo",type(salida),"\n")

salida = variable1 - variable2
print("Resultado de la operacion = ",salida,"Tipo",type(salida),"\n")

salida = variable1 * variable2
print("Resultado de la operacion = ",salida,"Tipo",type(salida),"\n")

salida = variable1 / variable2
print("Resultado de la operacion = ",salida,"Tipo",type(salida),"\n")

salida = variable1 // variable2
print("Resultado de la operacion = ",salida,"Tipo",type(salida),"\n")

salida = variable1 % variable2
print("Resultado de la operacion = ",salida,"Tipo",type(salida),"\n")

## Jerarquia de las operaciones

## y = mx + b --> m -> 4.5, b -> 3

print(" Ecuacion de la recta \n")

m = 4.5 
b = 3

x = 4

y = (m * x) + b

print("El resultado es =",y,"\n")


## Divisor de voltaje 

## Vout = (R1 * Vcc) / (R1 + R2)

print(" Divisor de voltaje \n")

R1 = 100
R2 = 200

Vcc = 50

Vout = (R1 * Vcc) / (R1 + R2)

print("El resultado es =",Vout,"\n")

## Ingreso de datos en Python

input1 = input("Digite el valor de la R1 \n")
input2 = input("Digite el valor de la R2 \n")
input3 = input("Digite el valor del Voltaje de la fuente \n")

R1  = float(input1)
R2  = float(input2)
Vcc = float(input3)

Vout = (R1 * Vcc) / (R1 + R2)
print("El resultado es =",Vout,"\n")

