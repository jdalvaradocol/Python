
print("Bienvenido a python \n")
print(' 27/08/2024 \n')

# Tipos de variable

# Variables tipo int 32 -2.147.483.648 a 2.147.483.647

variable = 123
print('Variable =', variable,'Tipo',type(variable),'\n')

# Variables tipo float 

variable = 123.123
print('Variable =', variable,'Tipo',type(variable),'\n')

# Variables tipo string 

mensaje = 'Hola mundo'
print('Variable =', mensaje,'Tipo',type(mensaje),'\n')

# Variables tipo bool (True - False)  

estado = True
print('Variable =', estado,'Tipo',type(estado),'\n')

# Operaciones de variables en python.

var1 = 123
var2 = 100

salida = var1 + var2
print('salida =', var1 ,'+',var2,'=',salida,'\n')
print('Tipo',type(salida),'\n')

salida = var1 - var2
print('salida =', var1 ,'-',var2,'=',salida,'\n')
print('Tipo',type(salida),'\n')

salida = var1 * var2
print('salida =', var1 ,'*',var2,'=',salida,'\n')
print('Tipo',type(salida),'\n')

salida = var1 / var2
print('salida =', var1 ,'/',var2,'=',salida,'\n')
print('Tipo',type(salida),'\n')

salida = var1 // var2
print('salida =', var1 ,'//',var2,'=',salida,'\n')
print('Tipo',type(salida),'\n')

salida = var1 % var2
print('salida =', var1 ,'%',var2,'=',salida,'\n')
print('Tipo',type(salida),'\n')

# Jerarquia de las operaaciones.

m = 5
x = 4
b = 2

y = (m * x) + b

print('y = ',y)

# Divisor de voltaje

# V = (Vcc * R1) / (R1 + R2)

Vcc = 50
R1 = 100
R2 = 100

Vd = (Vcc * R1) / (R1 + R2)

print('El voltaje del divisor es igual a = ',Vd)

# Ingreso de datos en python

input_a = input('Digite el valor de R1 \n')
input_b = input('Digite el valor de R2 \n')
input_c = input('Digite el valor de Vcc \n')

Vcc = float(input_c)
R1  = float(input_a)
R2  = float(input_b)

Vd = (Vcc * R1) / (R1 + R2)

print('El voltaje del divisor es igual a = ',Vd)