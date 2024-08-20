edad = int(input("Ingrese su edad: "))

if edad <= 18:
    print("Tienes una larga vida por delante")
elif (
    edad <= 30
):  # elif solo trabaja cuando el if anterior es falso y la condicion del propio elif es verdadera.
    print("Adulto Joven")
elif edad <= 60:
    print("Adulto anciano")
elif edad <= 100:
    print("Sobreviviente")
else:
    print("Como estas vivo???")
