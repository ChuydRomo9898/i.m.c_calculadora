nombre = input("cual es tu nombre?:")
apellido_paterno = input("cual es tu apellido paterno?:")
apellido_materno = input("cual es tu apellido materno?:")
edad = int(input("cual es tu edad?:"))
peso = float(input("cual es tu peso en kg?:"))
estatura = float(input("cual es tu estatura?:"))

imc = (peso/estatura**2)

print(f"hola {nombre} {apellido_paterno} {apellido_materno} tu edad es de {edad} y tu estatura es de {estatura}")

print(f"tu imc es :{imc:.2f}")

if imc <18.5:
    print("estas bajo en peso.")
elif 18.5 <= imc <25:
    print("tienes peso normal.")
elif 25<= imc <30:
    print("tienes sobre peso.")
else:
    print("tienes obesidad.")

    
