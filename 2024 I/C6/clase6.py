
import numpy as np

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

def imprimir_matriz(X):
    for i in range(len(X)):
        for j in range(len(X)):
            print(X[i][j],'\t',end=" ")
        print('\n')

A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]

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

print("Matriz C")
imprimir_matriz(C)

C = [[0, 0],[0, 0]];

for i in range(len(C)):
        for j in range(len(C)):
            print("[",i,"]","[",j,"]")
        print('\n')


print("Matriz C")
C = suma_matriz(A,B)
imprimir_matriz(C)

A = [[1, 2, 3],[3, 4, 5],[3, 4, 5]]
B = [[5, 6, 7],[7, 8, 9],[1, 2, 3]]

print("Matriz C")
C = suma_matriz(A,B)
imprimir_matriz(C)

A = [[1, 2],[3, 4]]
B = [[5, 6],[7, 8]]
C = [[0, 0],[0, 0]];

# A_((0,0))*B_((0,0))+A_((0,1))*B_((1,0))
# A_((0,0))*B_((0,1))+A_((0,1))*B_((1,1))
# A_((1,0))*B_((0,0))+A_((1,1))*B_((1,0))
# A_((1,0))*B_((0,1))+A_((1,1))*B_((1,1))

for i in range(len(C)):
        for j in range(len(C)):
            # print('[',i,'][',0,']-[',0,'][',j,']-[',i,'][',1,']-[',1,'][',j,']')
            C[i][j] = (A[i][0] * B [0][j]) + (A[i][1] * B [1][j])      

        #print('\n')

print("Matriz C")
imprimir_matriz(C)

R = np.dot(A,B)
imprimir_matriz(R)
