import cv2

print("Hecho por Jaquez Andres 0074")

# 2. Leer y mostrar imagen
image = cv2.imread('carrorojo.jpg')

cv2.imshow('Jaquez Andres 0074 - Imagen Original', image)


# 3. Convertir imagen a escala de grises
image = cv2.imread('carrorojo.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('gray_image.jpg', gray_image)

cv2.imshow('Jaquez Andres 0074 - Imagen a Grises', gray_image)


# 4. Redimensionar imagen
image = cv2.imread('carrorojo.jpg')

resized_image = cv2.resize(image, (300, 200))

cv2.imwrite('resized_image.jpg', resized_image)

cv2.imshow('Jaquez Andres 0074 - Imagen Redimensionada', resized_image)


# 5. Rotar imagen
image = cv2.imread('carrorojo.jpg')

(h, w) = image.shape[:2]

center = (w // 2, h // 2)

matrix = cv2.getRotationMatrix2D(center, 90, 1.0)

rotated_image = cv2.warpAffine(image, matrix, (w, h))

cv2.imwrite('rotated_image.jpg', rotated_image)

cv2.imshow('Jaquez Andres 0074 - Imagen Rotada', rotated_image)


# 6. Aplicar desenfoque Gaussiano
image = cv2.imread('carrorojo.jpg')

blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

cv2.imwrite('blurred_image.jpg', blurred_image)

cv2.imshow('Jaquez Andres 0074 - Imagen con Desenfoque', blurred_image)


# 7. Detección de bordes Canny
image = cv2.imread('carrorojo.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, 100, 200)

cv2.imwrite('edges.jpg', edges)

cv2.imshow('Jaquez Andres 0074 - Deteccion de Bordes', edges)


# 8. Dibujar rectángulo y agregar texto
image = cv2.imread('carrorojo.jpg')

cv2.rectangle(image, (50, 50), (200, 200), (255, 0, 0), 3)

cv2.putText(image, 'OpenCV', (60, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

cv2.imwrite('output_image.jpg', image)

cv2.imshow('Jaquez Andres 0074 - Dibujar Figuras y Texto', image)


# 9. Aplicar umbralización
image = cv2.imread('carrorojo.jpg', 0)

_, thresh_image = cv2.threshold(
    image, 127, 255, cv2.THRESH_BINARY
)

cv2.imwrite('threshold_image.jpg', thresh_image)

cv2.imshow('Jaquez Andres 0074 - Umbralizacion', thresh_image)


# 10. Detección de contornos
image = cv2.imread('carrorojo.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray_image, 100, 200)

contours, _ = cv2.findContours(
    edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

cv2.imwrite('contours_image.jpg', image)

cv2.imshow('Jaquez Andres 0074 - Deteccion de Contornos', image)


# Esperar tecla y cerrar ventanas
cv2.waitKey(0)

cv2.destroyAllWindows()

print("Hecho por Jaquez Andres 0074")