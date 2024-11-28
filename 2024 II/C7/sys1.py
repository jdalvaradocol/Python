
import numpy as np
import matplotlib.pyplot as plt
from skimage import io              # pip install scikit-image

imagen = io.imread("imagen1.jpg")

size = imagen.shape

print(imagen[0][0])
print(size)

filas = size[0]
columnas = size[1]
capas = size[2]

image_gray = np.zeros((filas,columnas), dtype = int)

for i in range(filas):
    for j in range(columnas):

        R = float(imagen[i][j][0])
        G = float(imagen[i][j][1])
        B = float(imagen[i][j][2])

        image_gray[i][j] = int((R + B + G) / 3.0)


media = int(np.mean(image_gray))
print(media)

image_bin = np.zeros((filas,columnas), dtype = int)

for i in range(filas):
    for j in range(columnas):

        if (media > image_gray[i][j]):
            image_bin[i][j] = 255
        else:
            image_bin[i][j] = 0    

image_min = np.ones((filas,columnas), dtype = int)*255

for i in range(0,filas,2):
    for j in range(0,columnas,2):

        med = 0

        for x in range(i+0,i+2):
            for y in range(j+0,j+2):

                med = med + image_gray[x][y]

        image_min[int(i/2)][int(j/2)] = int(med / 4.0)        

plt.figure(1)
plt.imshow(imagen)
plt.axis("off")

plt.figure(2)
plt.imshow(image_gray, cmap='gray',vmin=0, vmax=255)
plt.axis("off")

plt.figure(3)
plt.imshow(image_bin, cmap='binary',vmin=0, vmax=255)
plt.axis("off")

plt.figure(4)
plt.imshow(image_min, cmap='gray',vmin=0, vmax=255)
plt.axis("off")
plt.show()

