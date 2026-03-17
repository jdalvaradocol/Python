
import numpy as np

def ingresar_matriz(Filas, Columnas, nombre_matriz = "Matriz"):
    
    M = []

    for i in range(int(Filas)):
        M.append([0]*int(Columnas))

    for i in range(int(Filas)):
        for j in range(int(Columnas)):
            dato = input("Ingrese el dato para: " + nombre_matriz + "[" + str(i) + "][" + str(j) + "] = ")
            M[i][j] = float(dato)

    return M

def resta_matriz(A, B):

    R=[]

    for i in range(len(A)):
        R.append([0]*len(A))

    for i in range(len(A)):
        for j in range(len(A)):
            R[i][j] = A[i][j] - B[i][j]

    return R

def suma_matriz(A, B):

    R=[]

    for i in range(len(A)):
        R.append([0]*len(A))

    for i in range(len(A)):
        for j in range(len(A)):
            R[i][j] = A[i][j] + B[i][j]

    return R

def imprimir_matriz(matriz):
    
    filas, columnas = len(matriz), len(matriz[0])
        
    for i in range(filas):
        for j in range(columnas):
            print(matriz[i][j],'\t',end=" ")
        print('\n')

A = []
B = []

parametro_i = input("Ingrese el numero de filas i: ")
parametro_j = input("Ingrese el numero de columnas j: ")

# Ingresar los datos para la matriz A por el usuario.
A = ingresar_matriz(parametro_i, parametro_j, "A")

# Ingresar los datos para la matriz B por el usuario.
B = ingresar_matriz(parametro_i, parametro_j, "B")

# print(A)

print("Matriz A")
imprimir_matriz(A)
print("Matriz B")
imprimir_matriz(B)

C = [[0, 0],[0, 0]];

C[0][0] = A[0][0] + B[0][0]
C[0][1] = A[0][1] + B[0][1]
C[1][0] = A[1][0] + B[1][0]
C[1][1] = A[1][1] + B[1][1]

print(" Suma de dos matrices 2x2 ")
imprimir_matriz(C)

print("Suma de dos matrices 2x2 con funciones")
C = suma_matriz(A,B)
imprimir_matriz(C)

print("Suma de dos matrices 2x2 con librería numpy")
R = np.add(A,B)
imprimir_matriz(R)

A = [[1, 2, 3],[3, 4, 5],[3, 4, 5]]
B = [[5, 6, 7],[7, 8, 9],[1, 2, 3]]

print("Suma de dos matrices 3x3 con funciones")
respuesta = suma_matriz(A,B)
imprimir_matriz(respuesta)

A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]
C = [[0, 0],[0, 0]];

# A_((0,0))*B_((0,0)) + A_((0,1))*B_((1,0))
# A_((0,0))*B_((0,1)) + A_((0,1))*B_((1,1))
# A_((1,0))*B_((0,0)) + A_((1,1))*B_((1,0))
# A_((1,0))*B_((0,1)) + A_((1,1))*B_((1,1))

for i in range(len(C)):
        for j in range(len(C)):
            # print('[',i,'][',0,']-[',0,'][',j,']-[',i,'][',1,']-[',1,'][',j,']')
            C[i][j] = (A[i][0] * B [0][j]) + (A[i][1] * B [1][j])      

print("Multiplicación de dos matrices 2x2")
imprimir_matriz(C)

print("Multiplicación de dos matrices 2x2 con librería numpy")
R = np.dot(A,B)
imprimir_matriz(R)
