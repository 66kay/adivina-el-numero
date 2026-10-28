# Adivina el numero
# El computador elige un numero del 1 al 100 y tu debes adivinarlo.

import random

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("=== Adivina el numero ===")
print("Estoy pensando en un numero del 1 al 100.")

while adivinado == False:
    numero = int(input("Tu numero: "))
    intentos = intentos + 1

    if numero < secreto:
        print("Mas alto")
    elif numero > secreto:
        print("Mas bajo")
    else:
        adivinado = True

print("Correcto! Era el", secreto)
print("Lo lograste en", intentos, "intentos")
