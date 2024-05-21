
from skimage import io # pip install scikit-image
import numpy as np
import matplotlib.pyplot as plt

y = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
x = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
 
plt.plot(x,y,'r',linewidth = 3.0)   # Grafica
plt.title('Señal')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo')
plt.axis((0.0,0.5,0.0,5.0))
plt.grid(True)  # Grilla activada
plt.show()      # Figura 1    

Amplitud    =  3.0
frecuencia  = 10.0

# tiempo = t
t = np.arange(0.0,1,0.001)
# omega = w
w = 2 * np.pi * frecuencia
y = Amplitud * np.sin(w*t)
y = Amplitud * np.cos(w*t)

plt.plot(t,y,'b',linewidth = 3.0)   # Grafica
plt.title('Señal')
plt.ylabel('Amplitud')
plt.xlabel('Tiempo')
plt.axis((0.0,1.0,-5.0,5.0))
plt.grid(True)  # Grilla activada
plt.show()      # Figura 1    

# tiempo = t
t = np.arange(-1.0,1.0,0.001)
# omega = w
w = 2 * np.pi * frecuencia
y_sin = Amplitud * np.sin(w*t)
y_cos = Amplitud * np.cos(w*t)
y_line = 4.0 * t + 2.0
y_cuadrado = t ** 2

plt.subplot(2,1,1)
plt.plot(t,y_sin,'b',linewidth = 3.0)   # Grafica
plt.subplot(2,1,2)
plt.plot(t,y_cos,'b',linewidth = 3.0)   # Grafica
plt.show()      # Figura 1   

plt.subplot(1,2,1)
plt.plot(t,y_sin,'b',linewidth = 3.0)   # Grafica
plt.subplot(1,2,2)
plt.plot(t,y_cos,'b',linewidth = 3.0)   # Grafica
plt.show()      # Figura 1    

plt.subplot(2,2,1)
plt.plot(t,y_sin,'b',linewidth = 3.0)   # Grafica
plt.grid(True)  # Grilla activada
plt.title(' seno ')
plt.subplot(2,2,2)
plt.plot(t,y_cos,'r',linewidth = 3.0)   # Grafica
plt.grid(True)  # Grilla activada
plt.title('coseno')
plt.subplot(2,2,3)
plt.plot(t,y_line,'g',linewidth = 3.0)   # Grafica
plt.grid(True)  # Grilla activada
plt.title('Lineal')
plt.subplot(2,2,4)
plt.plot(t,y_cuadrado,'c',linewidth = 3.0)   # Grafica
plt.grid(True)  # Grilla activada
plt.title('Cuadrada')
plt.show()      # Figura 1  

## Imagenes

image = io.imread("imagen.jpg")

plt.imshow(image)
plt.axis("off")
plt.show()      # Figura 1    

size = image.shape

filas    = size[0]
columnas = size[1]
capas    = size[2]

image_gray = np.zeros((filas,columnas), dtype=int)

for i in range(filas):
    for j in range(columnas):
        R = float(image[i][j][0])
        G = float(image[i][j][1])
        B = float(image[i][j][2])
        image_gray[i][j] = int((R + G + B) / 3.0) 

print(image_gray)

plt.imshow(image_gray, cmap='gray', vmin=0, vmax=255)
plt.axis("off")
plt.show()      # Figura 1    
