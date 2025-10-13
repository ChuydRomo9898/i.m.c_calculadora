
import random

secreto = random.randint(1, 100)
intentos = 0

print(" Adivina el número secreto (entre 1 y 100)")
print("--------------------------------------------")

while True:
    try:
        numero = int(input(" Ingresa un número: "))
        intentos += 1
        
        if numero < 1 or numero > 100:
            print(" El número debe estar entre 1 y 100")
            continue
            
        if numero < secreto:
            print(" El número es MÁS GRANDE")
        elif numero > secreto:
            print("El número es MÁS CHICO")
        else:
            print(f" ¡CORRECTO! El número era {secreto}")
            print(f" Lo adivinaste en {intentos} intentos")
            break
    
    except ValueError:
        print("Error: Ingresa solo números enteros")