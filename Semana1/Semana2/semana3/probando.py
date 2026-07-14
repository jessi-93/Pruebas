import math

def calcular_maletas():
    print("--- CÁLCULO DE MALETAS EN BODEGA DE AUTOBÚS ---\n")
    
    try:
        # 1. Recibir los inputs del usuario
        volumen_total = float(input("Ingrese el volumen total de la bodega (en m³): "))
        largo = float(input("Ingrese el largo de la maleta (en m): "))
        ancho = float(input("Ingrese el ancho de la maleta (en m): "))
        alto = float(input("Ingrese el alto de la maleta (en m): "))
        
        # Validación básica para evitar divisiones por cero o números negativos
        if volumen_total <= 0 or largo <= 0 or ancho <= 0 or alto <= 0:
            print("\nError: Todos los valores deben ser mayores a cero.")
            return

        # 2. Calcular el volumen de una sola maleta
        volumen_maleta = largo * ancho * alto
        
        # 3. Calcular el volumen útil (solo el 70% de la bodega)
        volumen_util = volumen_total * 0.70
        
        # 4. Calcular la cantidad máxima de maletas
        # Usamos math.floor para redondear hacia abajo (no se puede llevar una fracción de maleta)
        cantidad_maxima = math.floor(volumen_util / volumen_maleta)
        
        # 5. Mostrar el output
        print("\n--- RESULTADO ---")
        print(f"Volumen de una maleta: {volumen_maleta:.2f} m³")
        print(f"Volumen útil de la bodega (70%): {volumen_util:.2f} m³")
        print(f"Cantidad máxima de maletas: {cantidad_maxima}")

    except ValueError:
        print("\nError: Por favor, ingrese solo valores numéricos válidos.")

# Ejecutar la función

calcular_maletas()
input("\nPresiona Enter para salir...")