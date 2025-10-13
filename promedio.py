materia_1 = input("nombre de la primera materia: ?")
calificacion_1 = float(input("Cual fue la calificacion que obtuviste en { materia_1 }"))

materia_2 = input("Nombre de la segunda materia: ?")
calificacion_2 = float(input("Cual fue la calificacion que obtuviste en { materia_2 }"))

materia_3 = input("Nombre de tu tercera materia: ?")
calificacion_3 = float(input("Cual fue la calificacion que obtuviste en { materia_3}"))

promedio = ( calificacion_1 + calificacion_2 + calificacion_3)/3
print(f"tu promedio es : {promedio:.2f}")
if promedio == 10:
    print("felicidades por tu promedio")
elif promedio >= 9:
    print("excelente trabajo")
elif promedio >= 6:
    print("panzaste")
else:
    print("reprobaste el semestre")
                