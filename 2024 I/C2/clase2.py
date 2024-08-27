
print("Condicionales en python")

var_1 = 20
var_2 = 50

print(var_1 == var_2)
print(type(var_1 == var_2))

print(var_1 > var_2)
print(type(var_1 == var_2))

print(var_1 < var_2)
print(type(var_1 == var_2))

# Ejemplo 1 if

var_1 = 10
var_2 = 10

if var_1 == var_2:
    print("Variable 1 es igual a la variable 2")

# Ejemplo 2 if else
    
var_1 = 10
var_2 = 20

if (var_1 == var_2):
    print("Variable 1 es igual a la variable 2") 
else:
    print("Variable 1 es diferente de la variable 2")

# Ejemplo 3 if elif else
    
var_1 = 40
var_2 = 20

if (var_1 == var_2):
    print("Variable 1 es igual a la variable 2")
elif (var_1 > var_2):
    print("Variable 1 es mayor que la variable 2")        
else:
    print("Variable 1 es menor que la variable 2")

# Ejemplo rangos de edad.

# Primera Infancia  ( 0 -  5 años)
# Infancia          ( 6 - 11 años)
# Adolescencia      (12 - 18 años)
# Juventud          (14 - 26 años)
# Adultez           (27 - 59 años)
# Persona Mayor     (     60 años o mas)

print("\n \n \n") 

input1 = input("Ingrese la edad, debe ser un numero entero \n")

edad  = int(input1)

if (edad > 0) and (edad <= 5):    #  if (edad > 0) & (edad <= 5):
    print("Primera Infancia \n")
elif (edad >= 6) & (edad <= 11):    
    print("Infancia \n")     
elif (edad >= 12) & (edad <= 26):    
    
    if (edad >= 12) & (edad <= 18):
        print(" Adolescencia ") 
    if (edad >= 14) & (edad <= 26):
        print(" Juventud ") 

    print("\n")     
elif (edad >= 27) & (edad <= 59):    
    print("Adultez \n")   
else:
    print("Persona Mayor \n") 
