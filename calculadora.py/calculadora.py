def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre 0"
    return a / b

while True:
    print("---MENU---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")
    
    if opcion == "5":
        print("Saliendo del programa...")
        break
    
    if opcion in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Solo se permiten números válidos.")
            continue
        
        if opcion == "1":
            print("Resultado:", sumar(num1, num2))
        elif opcion == "2":
            print("Resultado:", restar(num1, num2))
        elif opcion == "3":
            print("Resultado:", multiplicar(num1, num2))
        elif opcion == "4":
            print("Resultado:", dividir(num1, num2))
    else:
        print("Opción no válida. Por favor, elige una opción del 1 al 5.")
