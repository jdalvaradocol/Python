
print(" Funciones ciclos \n")

"""
Ciclos en python
"""
# Ciclos for 

num = input('Ingrese el numero de la tabla que desea realizar \n')
tabla = int(num)

for i in range(10):
    print(tabla,'x',i,'=',tabla*i)

print('\n')

for i in range(1,11):
    print(tabla,'x',i,'=',tabla*i)

print('\n')

for i in range(1,20,2):
    print(tabla,'x',i,'=',tabla*i)

print('\n')

# Ciclos while

index = 0

print('while')

while (index < 10):
    print(tabla,'x',index,'=',tabla*index)
    index+=1

print('\n')

index = 1
while (index < 11):
    print(tabla,'x',index,'=',tabla*index)
    index+=1

print('\n')

index = 1
while (index < 20):
    print(tabla,'x',index,'=',tabla*index)
    index+=2


# Ejemplos de for y while 

estado = False

while(estado == False): 
    
    num = input('Ingrese el numero de la tabla que desea realizar \n')
    
    try:
        tabla = int(num)
    except:
        print('El dato ingresado no es correcto ingrese el numero nuevamente')
        estado = False
    else:
        estado = True        

for i in range(1,11):
    print(tabla,'x',i,'=',tabla*i)

print('\n')
