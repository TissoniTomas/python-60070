datos = ["Tomas", "Tissoni", 26, "Buenos Aires"]
# datos2 = ("Tomas", "Tissoni", 26, "Buenos Aires");

print(type(datos))
datos2 = tuple(datos)  ## La funcion "tuple" convierte una lista a una tupla

print(type(datos2))

datos3 = list(datos2)  ## Analogamente a "tuple", "list" pasa de tupla a lista.
print(type(datos3))
