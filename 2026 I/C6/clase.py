
import cv2  
import matplotlib.pyplot as plt
import numpy as np

f = 5 
w = 2*np.pi*f
t = np.linspace(0, 2*np.pi, 5000)
ys = np.sin(w*t)

f = 10 
w = 2*np.pi*f
t = np.linspace(0, 2*np.pi, 5000)
yc = np.cos(w*t)

plt.figure(figsize=(10, 5))
plt.plot(t, ys, label='f = 5 Hz', color='blue')
plt.xlim(0, 1)
plt.xlabel('Tiempo (s)')   
plt.ylabel('Amplitud')
plt.title('Onda Senoidal')
plt.legend()
plt.grid()

plt.figure(figsize=(10, 5))
plt.plot(t, ys, label='f = 5 Hz', color='blue')
plt.plot(t, yc, label='f = 10 Hz', color='red' )
plt.xlim(0, 1)
plt.xlabel('Tiempo (s)')   
plt.ylabel('Amplitud')
plt.title('Onda Senoidal y Cosenoidal')
plt.legend()
plt.grid()

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, ys, label='f = 5 Hz', color='blue')
plt.xlim(0, 1)
plt.ylabel('Amplitud')
plt.title('Onda Senoidal')
plt.legend()
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, yc, label='f = 10 Hz', color='red' )
plt.xlim(0, 1)
plt.xlabel('Tiempo (s)')   
plt.ylabel('Amplitud')
plt.title('Onda Cosenoidal')
plt.legend()
plt.grid()
plt.show()

imagen = cv2.imread('imagen.jpg')
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.figure(figsize=(8, 6))
plt.imshow(imagen)      
plt.axis('off')
plt.title('Imagen Cargada')

plt.figure(figsize=(8, 6))
plt.imshow(imagen_rgb)      
plt.axis('off')
plt.title('Imagen Cargada')

filas, columnas, canales = imagen_rgb.shape
print(f"Dimensiones de la imagen: {filas} x {columnas} x {canales}")

# Modificar la imagen a color.
capa_zeros = np.zeros((filas, columnas), dtype=np.uint8) 

imagen_rgb[:, :, 0] = capa_zeros # Eliminar la capa roja
#imagen_rgb[:, :, 1] = capa_zeros # Eliminar la capa verde
imagen_rgb[:, :, 2] = capa_zeros # Eliminar la capa azul

plt.figure(figsize=(8, 6))    
plt.imshow(imagen_rgb)
plt.axis('off') 

# Nuevo Rojo = (Rojo * 0.393) + (Verde * 0.769) + (Azul * 0.189)
# Nuevo Verde = (Rojo * 0.349) + (Verde * 0.686) + (Azul * 0.168)
# Nuevo Azul = (Rojo * 0.272) + (Verde * 0.534) + (Azul * 0.131) 



imagen = cv2.imread('imagen.jpg')
imagen_rgb = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
imagen_sepia = np.zeros_like(imagen_rgb)

avance = 0

print(imagen_sepia.shape)

for i in range(filas):
    
    print(f"Procesando fila {i+1} de {filas}... Avance: {avance:.2f}%")
    avance = ((i + 1) / filas) * 100

    for j in range(columnas):
        rojo = imagen_rgb[i, j, 0]
        verde = imagen_rgb[i, j, 1]
        azul = imagen_rgb[i, j, 2]

        nuevo_rojo  = min(255, (rojo * 0.393) + (verde * 0.769) + (azul * 0.189))
        nuevo_verde = min(255, (rojo * 0.349) + (verde * 0.686) + (azul * 0.168))
        nuevo_azul  = min(255, (rojo * 0.272) + (verde * 0.534) + (azul * 0.131))

        imagen_sepia[i, j, 0] = nuevo_rojo
        imagen_sepia[i, j, 1] = nuevo_verde
        imagen_sepia[i, j, 2] = nuevo_azul

plt.figure(figsize=(8, 6))
plt.imshow(imagen_sepia)
plt.axis('off')    
plt.show()
    