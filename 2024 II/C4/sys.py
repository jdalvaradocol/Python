
print(" Funciones \n")

"""
Funciones
"""
# Funciones 

def suma(numeroA,numeroB):
    salida = numeroA + numeroB
    return salida

def resta(numeroA,numeroB):
    salida = numeroA - numeroB
    return salida

def sumaresta(numeroA,numeroB):
    salidaA = numeroA + numeroB
    salidaB = numeroA - numeroB
    return salidaA, salidaB  

dato = suma(3,4)
print(dato)
dato = resta(3,4)
print(dato)
dato = sumaresta(3,4)
print(dato)
print(dato[0])
print(dato[1])

print('\n')

def datos_entrada():

    estado = False

    while(estado == False): 
    
        num = input('Ingrese un numero entero \n')
    
        try:
            numero = int(num)
        except:
            print('El dato ingresado no es entero ingrese el numero nuevamente')
            estado = False
        else:
            estado = True        

    return numero

def tabla_multiplicar(min, max, tabla):
    for i in range(min,max+1):
        print(tabla,'x',i,'=',tabla*i)    

print(' Ingrese el valor minimo del multiplicador')
min = datos_entrada()
print(' Ingrese el valor maximo del multiplicador')
max = datos_entrada()
print(' Ingrese el valor de la tabla')
tabla = datos_entrada()

tabla_multiplicar(min,max,tabla)
tabla_multiplicar(tabla=tabla,min=min,max=max)
                  


print('\n')
