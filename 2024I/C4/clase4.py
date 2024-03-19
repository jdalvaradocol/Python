## Funciones 

def multiplicacion(dato_entrada,inicio, fin):

    for i in range(inicio, fin+1):
        print(dato_entrada, "x", i, "=", dato_entrada*(i), "\n" )

    return 0;

def par_impar(dato_entrada):

    resultado = dato_entrada % 2;

    if(resultado == 0):
        salida =  "PAR"
    else:
        salida = "IMPAR"    

    return salida;

## IPV = tasa de interes periodica vencida 
## EA Interes Efectivo Anual
## Días = Número de días de la tasa en la que se quiere convertir o de la que se convierte:
 
def IPV(EA,dias):

    salida = ((1 + EA) ** (dias/360)) - 1 ;  
    
    print("IPV =  \n", "{:.2f}".format(salida*100), "%")

    return salida;

def Credito(deuda,IPV,cuota):

    salida = deuda + (deuda*IPV) - cuota;  
    
    return salida;

correcto = 0

while correcto == 0:

    input1 = input("Ingrese el numero de la tabla que desea relizar\n")

    try:
        tabla  = int(input1)
        correcto = 1
    except:
        print("El numero ingresado no es entero \n")
        correcto = 0


multiplicacion(2,1,10)

correcto = 0

while correcto == 0:

    input1 = input("Ingrese un numero \n")

    try:
        numero  = int(input1)
        correcto = 1
    except:
        print("El numero ingresado no es entero \n")
        correcto = 0

respuesta = par_impar(numero)

print("el numero ingresado es ",respuesta)

## Interes de un credito

correcto = 0

while correcto == 0:

    input1 = input("Ingrese el valor del credito \n")

    try:
        credito  = int(input1)
        correcto = 1
    except:
        print("El numero ingresado no es entero \n")
        correcto = 0

correcto = 0

while correcto == 0:

    input1 = input("Ingrese el interes efectivo anual (EA) \n")

    try:
        EA  = float(input1)
        correcto = 1
    except:
        print("El numero ingresado no es float \n")
        correcto = 0

correcto = 0

while correcto == 0:

    input1 = input("Ingrese el valor de la cuota \n")

    try:
        cuota  = int(input1)
        correcto = 1
    except:
        print("El numero ingresado no es entero \n")
        correcto = 0

IPV_NUM = IPV(EA/100, 30)

print("Deuda = \n ", credito)

item = 0
while (cuota < credito):
    item += 1
    credito = Credito(credito,IPV_NUM,cuota)
    interes = credito * IPV_NUM
    print(item,"\t Deuda = ","{:.2f}".format(credito), " \t interes =","{:6.2f}".format(interes))
