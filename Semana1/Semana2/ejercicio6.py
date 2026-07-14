import math

def ejercicio6():
    #datos entrada
    hora = 4.1
    pagoXhora = 10
    
    #proceso
    #math.ceil() funcion mayor entero
    costoTotal = math.ceil(hora) * pagoXhora
    
    #salida
    print("El pago total es", costoTotal)

ejercicio6()