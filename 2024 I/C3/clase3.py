
# Ejemplo rangos de edad.

# Primera Infancia  ( 0 -  5 años)
# Infancia          ( 6 - 11 años)
# Adolescencia      (12 - 18 años)
# Juventud          (14 - 26 años)
# Adultez           (27 - 59 años)
# Persona Mayor     (     60 años o mas)

input1 = input("Ingrese la edad \n")

try:
    edad  = int(input1)
except:
    print("El numero ingresado no es entero \n")
else:
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
finally:
        print("Fin del programa \n\n") 

## Ciclos while o for 

iteracion = 0

while (iteracion < 10):
    print("iteracion =  \n", iteracion)
    iteracion += 1;

for  iteracion in range(10):
    print("iteracion =  \n", iteracion)


## Ciclos while try except 

correcto = 0

while correcto == 0:

    input1 = input("Ingrese el numero de la tabla que desea relizar\n")

    try:
        tabla  = int(input1)
        correcto = 1
    except:
        print("El numero ingresado no es entero \n")
        correcto = 0

for i in range(10):
    print(tabla, "x", i+1, "=", tabla*(i+1), "\n" )

for i in range(-5, 5):
    print(tabla, "x", i+1, "=", tabla*(i+1), "\n" )

for i in range(10, 100):
    print(tabla, "x", ((i+1)/10), "=", tabla*(((i+1)/10)), "\n" )   
