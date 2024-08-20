ingreso = 4500
edad = 20
antiguedad = 0

if edad >= 18:
    pass
    if antiguedad >= 3 and ingreso >= 2500:
        print("Credito aprobado")
    elif ingreso > 4000:
        print("Credito aprobado")
    else:
        print("Credito NO aprobado")
else:
    print("Credito NO aprobado")
