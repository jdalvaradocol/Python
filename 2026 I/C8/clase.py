
import cv2  
import numpy as np
import matplotlib.pyplot as plt

def asimetria(imagen):
    
    media = np.mean(imagen)
    std = np.std(imagen)
    
    asimetria = np.mean((imagen - media)**3) / (std**3)

    return asimetria

def rgb_a_gris(imagen):
    
    filas, columnas = imagen.shape[:2]
    imagen_gris = np.zeros((filas, columnas), dtype=np.uint8)
    
   # Convertir a escala de grises
    
    avanzando = 0
    visual = 100
    
    for i in range(0, filas-1):
    
        avanzando += 1
    
        if avanzando == visual: 
            print(f'Procesando RGB to GRAY {i+1}/{filas} ({(avanzando/filas)*100:.2f}%)')
            visual += 100
            
        for j in range(0, columnas-1):
        
            rojo  = float(imagen[i, j, 0]) 
            verde = float(imagen[i, j, 1])
            azul  = float(imagen[i, j, 2])
            
            gris = (rojo + verde + azul) / 3  
            imagen_gris[i, j] = np.uint8(gris)
    
    imagen_gris = np.array(imagen_gris)
            
    return imagen_gris        

def convolucion(imagen, kernel):
    
    filas, columnas = imagen.shape
    
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
                
            H1 = imagen[i+0, j+0] * kernel[0, 0]
            H2 = imagen[i+0, j+1] * kernel[0, 1]
            H3 = imagen[i+0, j+2] * kernel[0, 2]
                
            H4 = imagen[i+1, j+0] * kernel[1, 0]
            H5 = imagen[i+1, j+1] * kernel[1, 1]
            H6 = imagen[i+1, j+2] * kernel[1, 2]
                
            H7 = imagen[i+2, j+0] * kernel[2, 0]
            H8 = imagen[i+2, j+1] * kernel[2, 1]
            H9 = imagen[i+2, j+2] * kernel[2, 2]
            
            suma = H1 + H2 + H3 + H4 + H5 + H6 + H7 + H8 + H9
            
            '''    
            if suma > 255:
                suma = 255
            elif suma < 0:
                suma = 0     
            '''
               
            imagen_filtrada[i, j] = np.uint8(suma)
                
    return imagen_filtrada

# Cargar la imagen
imagen_rgb = cv2.imread('imagen1.jpg')
# Convertir de BGR a RGB
imagen_rgb = cv2.cvtColor(imagen_rgb, cv2.COLOR_BGR2RGB)

# Obtener las dimensiones de la imagen
filas, columnas = imagen_rgb.shape[:2]

# Convertir a escala de grises
imagen_gris = rgb_a_gris(imagen_rgb)    

# Aplicar el filtro con convolución

# Filtro de Sobel horizontal.

kernel = np.array([[1, 2, 1],   
                   [0, 0, 0],   
                   [-1, -2, -1]])   

imagen_filtradaA = convolucion(imagen_gris, kernel)  

# Filtro laplaciano.

kernel = np.array([[0, -1, 0],   
                   [-1, 4, -1],   
                   [0, -1, 0]])   

imagen_filtradaB = convolucion(imagen_gris, kernel)  

# Filtro de descripción.

kernel = np.array([[-1, -1, -1],   
                   [-1, 8, -1],   
                   [-1, -1, -1]])   

imagen_filtradaC = convolucion(imagen_gris, kernel)  

media_gris = np.mean(imagen_gris)
media_sobel = np.mean(imagen_filtradaA)
media_laplaciano = np.mean(imagen_filtradaB)
media_descripcion = np.mean(imagen_filtradaC)

print(f'Media de la imagen en escala de grises: {media_gris:.2f}')
print(f'Media de la imagen filtrada con Sobel: {media_sobel:.2f}')    
print(f'Media de la imagen filtrada con Laplaciano: {media_laplaciano:.2f}')
print(f'Media de la imagen filtrada con Descripción: {media_descripcion:.2f}')

std_gris = np.std(imagen_gris)
std_sobel = np.std(imagen_filtradaA)
std_laplaciano = np.std(imagen_filtradaB)
std_descripcion = np.std(imagen_filtradaC)

print(f'desviación estándar de la imagen en escala de grises: {std_gris:.2f}')
print(f'desviación estándar de la imagen filtrada con Sobel: {std_sobel:.2f}')    
print(f'desviación estándar de la imagen filtrada con Laplaciano: {std_laplaciano:.2f}')
print(f'desviación estándar de la imagen filtrada con Descripción: {std_descripcion:.2f}')

corr_gris = asimetria(imagen_gris)
corr_sobel = asimetria(imagen_filtradaA)
corr_laplaciano = asimetria(imagen_filtradaB)
corr_descripcion = asimetria(imagen_filtradaC)

print(f'Asimetria de grayscale image: {corr_gris:.2f}')
print(f'Asimetria de image filtered with Sobel: {corr_sobel:.2f}')    
print(f'Asimetria de image filtered with Laplaciano: {corr_laplaciano:.2f}')
print(f'Asimetria de the image filtered with Descripción: {corr_descripcion:.2f}')

plt.figure(figsize=(8, 6))
plt.subplot(1, 2, 1)
plt.imshow(imagen_rgb)    
plt.axis('off')
plt.title('Imagen a color 24 bits')
plt.subplot(1, 2, 2)
plt.imshow(imagen_gris, cmap='gray')    
plt.axis('off')
plt.title('Imagen en Escala de Grises')

plt.figure(figsize=(8, 6))
plt.subplot(2, 2, 1)
plt.imshow(imagen_rgb)    
plt.axis('off')
plt.title('Imagen a color 24 bits')
plt.subplot(2, 2, 2)
plt.imshow(imagen_filtradaA, cmap='gray')    
plt.axis('off')
plt.title('Imagen filtrada Sobel')
plt.subplot(2, 2, 3)
plt.imshow(imagen_filtradaB, cmap='gray')    
plt.axis('off')
plt.title('Imagen filtrada Laplaciano')
plt.subplot(2, 2, 4)
plt.imshow(imagen_filtradaC, cmap='gray')    
plt.axis('off')
plt.title('Imagen filtrada descripción')
plt.show()
  