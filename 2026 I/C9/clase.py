
import cv2  
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

def asimetria(imagen):
    
    media = np.mean(imagen)
    std = np.std(imagen)
    
    asimetria = np.mean((imagen - media)**3) / (std**3)

    return asimetria

def rgb_a_gris(imagen):
    
    filas, columnas = imagen.shape[:2]
    imagen_gris = np.zeros((filas, columnas), dtype=np.uint8)
    
   # Convertir a escala de grises
   
    for i in range(0, filas-1):
             
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
    
    for i in range(0, filas-2):
                
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

# Cargar las imágenes de la base de datos

imagenes_circulos = []

for i in range(1, 101):
    carpeta = Path("Base_datos") / "C"
    ruta = carpeta / f"C ({i}).png"
    imagen = cv2.imread(ruta)
    imagenes_circulos.append(imagen)

imagenes_triangulos = []

for i in range(1, 101):
    carpeta = Path("Base_datos") / "T"
    ruta = carpeta / f"T ({i}).png"
    imagen = cv2.imread(ruta)
    imagenes_triangulos.append(imagen)
    
imagenes_cuadrados = []

for i in range(1, 101):
    carpeta = Path("Base_datos") / "S"
    ruta = carpeta / f"S ({i}).png"
    imagen = cv2.imread(ruta)
    imagenes_cuadrados.append(imagen)

print("Número de imágenes de círculos:", len(imagenes_circulos))
print("Número de imágenes de triángulos:", len(imagenes_triangulos))
print("Número de imágenes de cuadrados:", len(imagenes_cuadrados))        

plt.figure(figsize=(10, 10))

for i in range(1, 101):
    imagen = imagenes_circulos[i-1]
    plt.subplot(10, 10, i)
    plt.imshow(imagen)
    plt.axis("off")

plt.figure(figsize=(10, 10))

for i in range(1, 101):
    imagen = imagenes_triangulos[i-1]
    plt.subplot(10, 10, i)
    plt.imshow(imagen)
    plt.axis("off")

plt.figure(figsize=(10, 10))

for i in range(1, 101):
    imagen = imagenes_cuadrados[i-1]
    plt.subplot(10, 10, i)
    plt.imshow(imagen)
    plt.axis("off")

# Entrenamiento definir el centroide de cada clase.

kernel_sobel = np.array([[ -1, 0, 1],
                         [ -2, 0, 2],
                         [ -1, 0, 1]])

kernel_laplaciano = np.array([[0, -1, 0],   
                              [-1, 4, -1],   
                              [0, -1, 0]])  

kernel_descripcion = np.array([[-1, -1, -1],   
                               [-1, 8, -1],   
                               [-1, -1, -1]])   

cemtroide_circulo = []
centroide_triangulo = []    
centroide_cuadrado = []

avance = 0
    
for i in range(1, 71):
    
    avance += 1
    print(f"Avance: {avance}/70")

    imagen_circulo = imagenes_circulos[i-1]
    imagen_triangulo = imagenes_triangulos[i-1]
    imagen_cuadrado = imagenes_cuadrados[i-1]
    
    # Convertir a escala de grises
    imagen_circulo_gris   = rgb_a_gris(imagen_circulo)
    imagen_triangulo_gris = rgb_a_gris(imagen_triangulo)
    imagen_cuadrado_gris  = rgb_a_gris(imagen_cuadrado)
    
    # Aplicar el filtro de Sobel
    imagen_circulo_sobel = convolucion(imagen_circulo_gris, kernel_sobel)
    imagen_circulo_laplaciano = convolucion(imagen_circulo_gris, kernel_laplaciano)
    imagen_circulo_descripcion = convolucion(imagen_circulo_gris, kernel_descripcion)

    imagen_triangulo_sobel = convolucion(imagen_triangulo_gris, kernel_sobel)
    imagen_triangulo_laplaciano = convolucion(imagen_triangulo_gris, kernel_laplaciano)
    imagen_triangulo_descripcion = convolucion(imagen_triangulo_gris, kernel_descripcion)

    imagen_cuadrado_sobel = convolucion(imagen_cuadrado_gris, kernel_sobel)
    imagen_cuadrado_laplaciano = convolucion(imagen_cuadrado_gris, kernel_laplaciano)
    imagen_cuadrado_descripcion = convolucion(imagen_cuadrado_gris, kernel_descripcion)
        
    # Calcular los descriptores de cada imagen
    
    ### Descriptores de la imagen de círculos ###
    
    media_circulo1 = np.mean(imagen_circulo_sobel)
    std_circulo1 = np.std(imagen_circulo_sobel)
    asimetria_circulo1 = asimetria(imagen_circulo_sobel)

    media_circulo2 = np.mean(imagen_circulo_laplaciano)
    std_circulo2 = np.std(imagen_circulo_laplaciano)
    asimetria_circulo2 = asimetria(imagen_circulo_laplaciano)
    
    media_circulo3 = np.mean(imagen_circulo_descripcion)
    std_circulo3 = np.std(imagen_circulo_descripcion)
    asimetria_circulo3 = asimetria(imagen_circulo_descripcion)
    
    cemtroide_circulo.append([media_circulo1, std_circulo1, asimetria_circulo1,
                              media_circulo2, std_circulo2, asimetria_circulo2,
                              media_circulo3, std_circulo3, asimetria_circulo3])
    
    ### Descriptores de la imagen de triángulos ###

    media_triangulo1 = np.mean(imagen_triangulo_sobel)
    std_triangulo1 = np.std(imagen_triangulo_sobel) 
    asimetria_triangulo1 = asimetria(imagen_triangulo_sobel)
    
    media_triangulo2 = np.mean(imagen_triangulo_laplaciano)
    std_triangulo2 = np.std(imagen_triangulo_laplaciano)
    asimetria_triangulo2 = asimetria(imagen_triangulo_laplaciano)

    media_triangulo3 = np.mean(imagen_triangulo_descripcion)
    std_triangulo3 = np.std(imagen_triangulo_descripcion)
    asimetria_triangulo3 = asimetria(imagen_triangulo_descripcion)

    centroide_triangulo.append([media_triangulo1, std_triangulo1, asimetria_triangulo1,
                                media_triangulo2, std_triangulo2, asimetria_triangulo2,
                                media_triangulo3, std_triangulo3, asimetria_triangulo3])
    
    ### Descriptores de la imagen de cuadrados ###

    media_cuadrado1 = np.mean(imagen_cuadrado_sobel)
    std_cuadrado1 = np.std(imagen_cuadrado_sobel)   
    asimetria_cuadrado1 = asimetria(imagen_cuadrado_sobel)
    
    media_cuadrado2 = np.mean(imagen_cuadrado_laplaciano)   
    std_cuadrado2 = np.std(imagen_cuadrado_laplaciano)
    asimetria_cuadrado2 = asimetria(imagen_cuadrado_laplaciano)
    
    media_cuadrado3 = np.mean(imagen_cuadrado_descripcion)      
    std_cuadrado3 = np.std(imagen_cuadrado_descripcion)
    asimetria_cuadrado3 = asimetria(imagen_cuadrado_descripcion)    
    
    centroide_cuadrado.append([media_cuadrado1, std_cuadrado1, asimetria_cuadrado1,
                              media_cuadrado2, std_cuadrado2, asimetria_cuadrado2,
                              media_cuadrado3, std_cuadrado3, asimetria_cuadrado3]) 
        

centroide_cuadrado = np.array(centroide_cuadrado)
centroide_triangulo = np.array(centroide_triangulo) 
centroide_circulo = np.array(cemtroide_circulo) 

print(centroide_cuadrado.shape)
print(centroide_triangulo.shape)
print(centroide_circulo.shape)

centroide_cuadrado_ref = np.mean(centroide_cuadrado, axis=0)
centroide_triangulo_ref = np.mean(centroide_triangulo, axis=0)
centroide_circulo_ref = np.mean(centroide_circulo, axis=0)

print(centroide_cuadrado_ref.shape)
print(centroide_triangulo_ref.shape)
print(centroide_circulo_ref.shape)

print(centroide_cuadrado_ref)
print(centroide_triangulo_ref)
print(centroide_circulo_ref)

# Se recomineda a los centroides de cada categoria relizar la normalizacion 
# de los datos, es decir, restar la media y dividir por la desviacion estandar 
# de cada descriptor. Esto se hace para que los descriptores tengan la misma 
# escala y no haya uno que domine sobre los otros.

# Prueba de los centroides con las imágenes de prueba.

centroide_circulo = np.zeros(9)
centroide_triangulo = np.zeros(9)
centroide_cuadrado = np.zeros(9)

avance = 0
matriz_confusion = np.zeros((3, 3), dtype=int)  
    
for i in range(71, 101):
    
    avance += 1
    print(f"Avance: {avance}/30")

    imagen_circulo = imagenes_circulos[i-1]
    imagen_triangulo = imagenes_triangulos[i-1]
    imagen_cuadrado = imagenes_cuadrados[i-1]
    
    # Convertir a escala de grises
    imagen_circulo_gris   = rgb_a_gris(imagen_circulo)
    imagen_triangulo_gris = rgb_a_gris(imagen_triangulo)
    imagen_cuadrado_gris  = rgb_a_gris(imagen_cuadrado)
    
    # Aplicar el filtro de Sobel
    imagen_circulo_sobel = convolucion(imagen_circulo_gris, kernel_sobel)
    imagen_circulo_laplaciano = convolucion(imagen_circulo_gris, kernel_laplaciano)
    imagen_circulo_descripcion = convolucion(imagen_circulo_gris, kernel_descripcion)

    imagen_triangulo_sobel = convolucion(imagen_triangulo_gris, kernel_sobel)
    imagen_triangulo_laplaciano = convolucion(imagen_triangulo_gris, kernel_laplaciano)
    imagen_triangulo_descripcion = convolucion(imagen_triangulo_gris, kernel_descripcion)

    imagen_cuadrado_sobel = convolucion(imagen_cuadrado_gris, kernel_sobel)
    imagen_cuadrado_laplaciano = convolucion(imagen_cuadrado_gris, kernel_laplaciano)
    imagen_cuadrado_descripcion = convolucion(imagen_cuadrado_gris, kernel_descripcion)
        
    # Calcular los descriptores de cada imagen
    
    ### Descriptores de la imagen de círculos ###
    
    media_circulo1 = np.mean(imagen_circulo_sobel)
    std_circulo1 = np.std(imagen_circulo_sobel)
    asimetria_circulo1 = asimetria(imagen_circulo_sobel)

    media_circulo2 = np.mean(imagen_circulo_laplaciano)
    std_circulo2 = np.std(imagen_circulo_laplaciano)
    asimetria_circulo2 = asimetria(imagen_circulo_laplaciano)
    
    media_circulo3 = np.mean(imagen_circulo_descripcion)
    std_circulo3 = np.std(imagen_circulo_descripcion)
    asimetria_circulo3 = asimetria(imagen_circulo_descripcion)
    
    centroide_circulo = np.array([media_circulo1, std_circulo1, asimetria_circulo1,
                       media_circulo2, std_circulo2, asimetria_circulo2,
                       media_circulo3, std_circulo3, asimetria_circulo3])
    
    ### Descriptores de la imagen de triángulos ###

    media_triangulo1 = np.mean(imagen_triangulo_sobel)
    std_triangulo1 = np.std(imagen_triangulo_sobel) 
    asimetria_triangulo1 = asimetria(imagen_triangulo_sobel)
    
    media_triangulo2 = np.mean(imagen_triangulo_laplaciano)
    std_triangulo2 = np.std(imagen_triangulo_laplaciano)
    asimetria_triangulo2 = asimetria(imagen_triangulo_laplaciano)

    media_triangulo3 = np.mean(imagen_triangulo_descripcion)
    std_triangulo3 = np.std(imagen_triangulo_descripcion)
    asimetria_triangulo3 = asimetria(imagen_triangulo_descripcion)

    centroide_triangulo = np.array([media_triangulo1, std_triangulo1, asimetria_triangulo1,
                                    media_triangulo2, std_triangulo2, asimetria_triangulo2,
                                    media_triangulo3, std_triangulo3, asimetria_triangulo3])
    
    ### Descriptores de la imagen de cuadrados ###

    media_cuadrado1 = np.mean(imagen_cuadrado_sobel)
    std_cuadrado1 = np.std(imagen_cuadrado_sobel)   
    asimetria_cuadrado1 = asimetria(imagen_cuadrado_sobel)
    
    media_cuadrado2 = np.mean(imagen_cuadrado_laplaciano)   
    std_cuadrado2 = np.std(imagen_cuadrado_laplaciano)
    asimetria_cuadrado2 = asimetria(imagen_cuadrado_laplaciano)
    
    media_cuadrado3 = np.mean(imagen_cuadrado_descripcion)      
    std_cuadrado3 = np.std(imagen_cuadrado_descripcion)
    asimetria_cuadrado3 = asimetria(imagen_cuadrado_descripcion)    
    
    centroide_cuadrado = np.array([media_cuadrado1, std_cuadrado1, asimetria_cuadrado1,
                        media_cuadrado2, std_cuadrado2, asimetria_cuadrado2,
                        media_cuadrado3, std_cuadrado3, asimetria_cuadrado3]) 
    
    
    distancia_circulo1 = np.linalg.norm(centroide_circulo_ref - centroide_circulo)
    distancia_circulo2 = np.linalg.norm(centroide_circulo_ref - centroide_triangulo)
    distancia_circulo3 = np.linalg.norm(centroide_circulo_ref - centroide_cuadrado)
    
    distancia_circulo = [distancia_circulo1, distancia_circulo2, distancia_circulo3]
    categoria_circulo = np.argmin(distancia_circulo)    
    
    distancia_triangulo1 = np.linalg.norm(centroide_triangulo_ref - centroide_circulo)
    distancia_triangulo2 = np.linalg.norm(centroide_triangulo_ref - centroide_triangulo)
    distancia_triangulo3 = np.linalg.norm(centroide_triangulo_ref - centroide_cuadrado)
    
    distancia_triangulo = [distancia_triangulo1, distancia_triangulo2, distancia_triangulo3]
    categoria_triangulo = np.argmin(distancia_triangulo)
    
    distancia_cuadrado1 = np.linalg.norm(centroide_cuadrado_ref - centroide_circulo)
    distancia_cuadrado2 = np.linalg.norm(centroide_cuadrado_ref - centroide_triangulo)
    distancia_cuadrado3 = np.linalg.norm(centroide_cuadrado_ref - centroide_cuadrado)

    distancia_cuadrado = [distancia_cuadrado1, distancia_cuadrado2, distancia_cuadrado3]
    categoria_cuadrado = np.argmin(distancia_cuadrado)
    
    # matriz de confusión
    # TP = True Positives. 
    # FP = False Positives. 
    # TN = True Negatives. 
    # FN = False Negatives.
        
    if categoria_circulo == 0:
        matriz_confusion[0, 0] += 1  # TP para círculos
        print("Círculo clasificado correctamente como círculo")
    elif categoria_circulo == 1:    
        matriz_confusion[0, 1] += 1  # FP para círculos
        print("Círculo clasificado incorrectamente como triángulo")
    elif categoria_circulo == 2:    
        matriz_confusion[0, 2] += 1  # FP para círculos
        print("Círculo clasificado incorrectamente como cuadrado")

    if categoria_triangulo == 0:
        matriz_confusion[1, 0] += 1  # FP para triángulos
        print("Triángulo clasificado incorrectamente como círculo")
    elif categoria_triangulo == 1:
        matriz_confusion[1, 1] += 1  # TP para triángulos
        print("Triángulo clasificado correctamente como triángulo")
    elif categoria_triangulo == 2:
        matriz_confusion[1, 2] += 1  # FP para triángulos
        print("Triángulo clasificado incorrectamente como cuadrado")

    if categoria_cuadrado == 0:
        matriz_confusion[2, 0] += 1  # FP para cuadrados
        print("Cuadrado clasificado incorrectamente como círculo")
    elif categoria_cuadrado == 1:
        matriz_confusion[2, 1] += 1  # FP para cuadrados
        print("Cuadrado clasificado incorrectamente como triángulo")
    elif categoria_cuadrado == 2:
        matriz_confusion[2, 2] += 1  # TP para cuadrados
        print("Cuadrado clasificado correctamente como cuadrado")

print("Matriz de confusión:")
print((matriz_confusion/len(imagenes_circulos[71:101]))*100)  # Normalizar la matriz de confusión por el número de imágenes de prueba

plt.show()  


