
# ciclos # while # for

"""
for i in range(inicio,fin, paso):
    print(i)  
"""
# fin
print(" ciclo for con fin")  
for i in range(10):
    print(i)  
  
  # inicio - fin  
print(" ciclo for con inicio - fin")  
for i in range(5, 10):
    print(i)     
 
 # inicio - fin - paso
print(" ciclo for con inicio - fin - paso")  
for i in range(10,0,-1):
    print(i)     
    
# while
    
print(" ciclo while")

contador = 0 
condicion = True

while condicion == True:
    print("contador = ", contador)
    ingresar = input("ingrese un numero: ")
    ingresar = int(ingresar)
    if ingresar == 10:
        condicion = False
    contador += 1

    
condicion = True

while condicion == True:
    ingresar = input("ingrese un numero entero: ")
    try:
        ingresar = int(ingresar)
        condicion = False
    except:
        print("El valor no es numero entero, intente de nuevo")
        condicion = True
 
 # Realiza una secuancia de numeros del 0 al 9 utilizando un ciclo while, luego realiza la misma secuencia utilizando un ciclo for.
  
print(" ciclo while del 0 al 9")
  
condicion = True  
i = 0
        
while condicion == True:
    print(i)
    i += 1
    if i >= 10:
        condicion = False
        
print(" ciclo while del 5 al 9")
  
condicion = True  
i = 5
        
while condicion == True:
    print(i)
    i += 1
    if i >= 10:
        condicion = False        
        
print(" ciclo while del 5 al 9 de a 2 en 2")
  
condicion = True  
i = 5
        
while condicion == True:
    print(i)
    i += 2
    if i >= 10:
        condicion = False          
        
print(" ciclo while del 9 al 0")
  
condicion = True  
i = 10
        
while condicion == True:
    print(i)
    i -= 1
    if i <= 0:
        condicion = False                  
        
print(" ciclo while del 0 al 2 con paso de 0.2")
  
condicion = True  
i = 0.0000000000000000000000000

while condicion == True:
    print(f"{i:.2f}")
    i += 0.2000000000000000000000000
    if i >= 2:
        condicion = False            