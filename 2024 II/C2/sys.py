
print("Condicionales en Python \n")


x = 10
y = 10
res  = x == y

print('Estado = ',x,'==',y,':',res,'Tipo', type(res))

x = 10
y = 20
res  = x != y
print('Estado = ',x,'!=',y,':',res,'Tipo', type(res))

x = 10
y = 20
res  = x > y
print('Estado = ',x,'>',y,':',res,'Tipo', type(res))

x = 10
y = 20
res  = x < y
print('Estado = ',x,'<',y,':',res,'Tipo', type(res))

## Funcion logica AND
##   A    -   B     =   x
## False    False   = False  
## False    True    = False  
## True     False   = False  
## True     True    = True  

## Funcion logica OR
##   A    -   B     =   x
## False    False   = False  
## False    True    = True  
## True     False   = True  
## True     True    = True 

x = True
y = False

res = x and y
print('Estado = ',x,' and ',y,':',res,'Tipo', type(res))

res = x & y
print('Estado = ',x,' and ',y,':',res,'Tipo', type(res))

res = x or y
print('Estado = ',x,' or ',y,':',res,'Tipo', type(res))

res = x | y
print('Estado = ',x,' or ',y,':',res,'Tipo', type(res))

## Entre 15 y 24

edad = 40

res1 = edad >= 15
res2 = edad <= 24

res = res1 and res2

print(' Joven = ',res1,' and ',res2,':',res,'Tipo', type(res))

res = (edad >= 15) and (edad <= 24)

print(' Joven = ',res1,' and ',res2,':',res,'Tipo', type(res))

# Condicionales

dato = input('Ingrese la edad \n')
edad = int(dato)

if edad >= 18:
    print('Es mayor de edad \n')

if edad >= 18:
    print('Es mayor de edad \n')
else:
    print('Es menor de edad \n') 

"""
primera infancia 0 a 5
infancia 6 a 11
adolecentes 12 a 18
juventud 14 a 26
adultez 27 a 59
Persona Mayor >60
"""

if   (edad >= 0) and (edad<=5):
    print('primera infancia 0 a 5 \n')
elif (edad >= 6) and (edad<=11):
    print('infancia 6 a 11 \n')
elif (edad >= 12) and (edad<=13):
    print('adolecentes 12 a 18 \n')
elif (edad >= 14) and (edad<=18):
    print('adolecentes 12 a 18 \n')
    print('juventud 14 a 26 \n')
elif (edad >= 19) and (edad<=26):
    print('juventud 14 a 26 \n')
elif (edad >= 27) and (edad<=59):
    print('adultez 27 a 59 \n')    
else:
    print('Persona Mayor > 60')

## Manejo de excepciones (try, except, else, finally)

dato = input('Ingrese la edad \n')

try:
    edad = int(dato)
except:
    print('El dato ingresado no es un numero entero \n')
else:

    if   (edad >= 0) and (edad<=5):
        print('primera infancia 0 a 5 \n')
    elif (edad >= 6) and (edad<=11):
        print('infancia 6 a 11 \n')
    elif (edad >= 12) and (edad<=13):
        print('adolecentes 12 a 18 \n')
    elif (edad >= 14) and (edad<=18):
        print('adolecentes 12 a 18 \n')
        print('juventud 14 a 26 \n')
    elif (edad >= 19) and (edad<=26):
        print('juventud 14 a 26 \n')
    elif (edad >= 27) and (edad<=59):
        print('adultez 27 a 59 \n')    
    else:
        print('Persona Mayor > 60')
finally:
    print('Fin del programa')
