# Datos de entrada
volumen_bodega = 100 
largo_maleta = 1 
ancho_maleta = 1
alto_maleta = 1
volumen_bodega = float(input("Ingrese el volumen total de la bodega (en m3): "))
largo_maleta = float(input("Ingrese el largo de la maleta (en m): "))
ancho_maleta = float(input("Ingrese el ancho de la maleta (en m): "))
alto_maleta = float(input("Ingrese el alto de la maleta (en m): "))

# 1. Calcular el volumen disponible de la bodega (solo el 70%)
volumen_disponible = volumen_bodega * 0.70

# 2. Calcular el volumen de una sola maleta
volumen_maleta = largo_maleta * ancho_maleta * alto_maleta

# 3. Calcular la cantidad máxima de maletas (usando división entera //)

cantidad_maletas = int(volumen_disponible // volumen_maleta)

# Resultado
print(f"La cantidad máxima de maletas que pueden transportarse es: {cantidad_maletas}")
