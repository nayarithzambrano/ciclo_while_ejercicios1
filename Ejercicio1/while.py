# Bucle While

import math

numero = int(input("Digite un numero: "))

while numero<0:
    print("Error -> deberia ser un numero positivo")
    numero = int(input("Digite un numero: "))


print(f"\nSu raiz cuadrada es: {(math.sqrt(numero)):2f}")