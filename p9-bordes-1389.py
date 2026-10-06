# Oscar Flores NC = 1389
# Problema 2   NL = 22
# ----- EJEMPLO 2 -----
print("------ EJEMPLO 2 ------")
import cv2

# Cargar imagen
imagen = cv2.imread("imagenes/mapache.jpg")

# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Convertir a imagen binaria mediante umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Detectar contornos
contornos, jerarquia = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Dibujar los contornos
resultado = imagen.copy()

cv2.drawContours(
    resultado,
    contornos,
    -1,
    (0, 255, 0),
    2
)

# Mostrar resultados
cv2.imshow("Imagen original 1389", imagen)
cv2.imshow("Imagen binaria 1389", binaria)
cv2.imshow("Contornos detectados 1389", resultado)

# Guardar resultado
cv2.imwrite(
    "resultados/ejemplo2_mapache-1389.jpg",
    resultado
)

print("Cantidad de contornos encontrados:", len(contornos))
print("Resultado guardado en resultados/ejemplo2_mapache-1389.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()

print("Programa realizado por Oscar Flores NC = 1389")

# Problema 3
# ----- EJEMPLO 3 -----
print("------ EJEMPLO 3 ------")

import cv2

# Cargar imagen
imagen = cv2.imread("imagenes/mapache.jpg")

# Comprobar imagen
if imagen is None:
    print("Error: no se pudo cargar la imagen.")
    exit()

# Convertir a escala de grises
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Aplicar umbral
_, binaria = cv2.threshold(
    gris,
    127,
    255,
    cv2.THRESH_BINARY
)

# Encontrar contornos externos
contornos, _ = cv2.findContours(
    binaria,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Crear copia
resultado = imagen.copy()

# Contador
cantidad = 0

# Analizar cada contorno
for contorno in contornos:

    # Calcular área
    area = cv2.contourArea(contorno)

    # Ignorar objetos demasiado pequeños
    if area > 500:

        cantidad += 1

        # Dibujar contorno
        cv2.drawContours(
            resultado,
            [contorno],
            -1,
            (0, 255, 0),
            2
        )

        # Obtener rectángulo
        x, y, ancho, alto = cv2.boundingRect(contorno)

        # Dibujar rectángulo
        cv2.rectangle(
            resultado,
            (x, y),
            (x + ancho, y + alto),
            (255, 0, 0),
            2
        )

        # Mostrar número del objeto
        cv2.putText(
            resultado,
            f"Objeto {cantidad}",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 0, 255),
            2
        )

# Mostrar resultado
cv2.imshow("Objetos identificados-1389", resultado)

# Guardar
cv2.imwrite(
    "resultados/ejemplo3_mapache-1389.jpg",
    resultado
)

print("Objetos identificados:", cantidad)
print("Resultado guardado en resultados/ejemplo3_mapache-1389.jpg")

# Esperar
cv2.waitKey(0)

# Cerrar
cv2.destroyAllWindows()
print("Programa realizado por Oscar Flores NC = 1389")