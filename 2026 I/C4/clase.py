
# Funciones.
"""
def nombre_de_la_funcion (Datos de entrada de la funcion):
    
    Algortimo de la funcion
    
    return los datos de salida de la funcion
"""

def suma (operador_A, operador_B):
    resultado = operador_A + operador_B
    return resultado

def resta (operador_A, operador_B):
    resultado = operador_A - operador_B
    return resultado

def multiplicacion (operador_A, operador_B):
    resultado = operador_A * operador_B
    return resultado

def division (operador_A, operador_B):
    resultado = operador_A / operador_B
    return resultado

def operaciones (operador_A, operador_B):
    suma = operador_A + operador_B
    resta = operador_A - operador_B
    multiplicacion = operador_A * operador_B
    division = operador_A / operador_B
    return (suma, resta, multiplicacion, division)  

A = input("ingrese una variable numerica decimal A = ")
B = input("ingrese una variable numerica decimal B = ")

A = float(A)
B = float(B)

print("La operacion entre ", A ,'+', B,'=', suma(A,B) )
print("La operacion entre ", A ,'-', B,'=', resta(A,B) )
print("La operacion entre ", A ,'*', B,'=', multiplicacion(A,B) )
print("La operacion entre ", A ,'/', B,'=', division(A,B) )

s,r,m,d = operaciones(A,B)

print("La operacion entre ", A ,'+', B,'=', s )
print("La operacion entre ", A ,'-', B,'=', r )
print("La operacion entre ", A ,'*', B,'=', m )
print("La operacion entre ", A ,'/', B,'=', d )

