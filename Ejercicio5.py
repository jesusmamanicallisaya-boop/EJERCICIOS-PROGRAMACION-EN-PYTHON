nota = int(input("Ingresa la nota final del 0 a 100: "))
if nota < 0:
    print("Nota inválida, ingrese un número del 0 al 100")
elif nota > 100:
    print("Nota inválida, ingrese un número del 0 al 100")
elif nota <= 50:
    print("REPROBADO")
else:
    print("APROBADO")