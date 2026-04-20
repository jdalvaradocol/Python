
import cv2  
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen
imagen_rgb = cv2.imread('imagen1.jpg')
# Convertir de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2RGB)

# Obtener las dimensiones de la imagen
filas, columnas = imagen_rgb.shape[:2]

# Convertir a escala de grises

imagen_gris = np.zeros((filas, columnas), dtype=np.uint8)

avanzando = 0
visual = 100
for i in range(0, filas-1):
    
    avanzando += 1
    
    if avanzando == visual: 
        print(f'Procesando RGB to GRAY {i+1}/{filas} ({(avanzando/filas)*100:.2f}%)')
        visual += 100
        
    for j in range(0, columnas-1):
        
            rojo  = float(imagen_rgb[i, j, 0]) 
            verde = float(imagen_rgb[i, j, 1])
            azul  = float(imagen_rgb[i, j, 2])
            
            gris = (rojo + verde + azul) / 3  
            imagen_gris[i, j] = np.uint8(gris)


imagen_gris = np.array(imagen_gris)

plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.imshow(imagen_rgb)    
plt.axis('off')
plt.title('Imagen a color 24 bits')
plt.subplot(1, 2, 2)
plt.imshow(imagen_gris, cmap='gray')    
plt.axis('off')
plt.title('Imagen en Escala de Grises')

# Filtro con convolución
kernel = np.array([[1, 2, 1],   
                   [0, 0, 0],   
                   [-1, -2, -1]]) 

imagen_filtrada = np.zeros((filas, columnas), dtype=np.uint8)

avanzando = 0
visual = 100
for i in range(0, filas-2):
    
    avanzando += 1
    
    if avanzando == visual: 
        print(f'Procesando FILTRO {i+1}/{filas} ({(avanzando/filas)*100:.2f}%)')
        visual += 100
        
    for j in range(0, columnas-2):
            
            suma = 0
            
            H1 = imagen_gris[i+0, j+0] * kernel[0, 0]
            H2 = imagen_gris[i+0, j+1] * kernel[0, 1]
            H3 = imagen_gris[i+0, j+2] * kernel[0, 2]
            
            H4 = imagen_gris[i+1, j+0] * kernel[1, 0]
            H5 = imagen_gris[i+1, j+1] * kernel[1, 1]
            H6 = imagen_gris[i+1, j+2] * kernel[1, 2]
            
            H7 = imagen_gris[i+2, j+0] * kernel[2, 0]
            H8 = imagen_gris[i+2, j+1] * kernel[2, 1]
            H9 = imagen_gris[i+2, j+2] * kernel[2, 2]
        
            suma = H1 + H2 + H3 + H4 + H5 + H6 + H7 + H8 + H9
            
            if suma > 255:
                suma = 255
            elif suma < 0:
                suma = 0     
            
            imagen_filtrada[i, j] = np.uint8(suma)

plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.imshow(imagen_rgb)    
plt.axis('off')
plt.title('Imagen a color 24 bits')
plt.subplot(1, 2, 2)
plt.imshow(imagen_filtrada, cmap='gray')    
plt.axis('off')
plt.title('Imagen filtrada')
plt.show()
  