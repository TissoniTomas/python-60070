datos1 = ["Tomas", "Tissoni", 26, 1.81]
datos2 = ("Tomas", "Tissoni", 26, 1.81)

print(datos2[2])
print(len(datos2))
### LAS TUPLAS SON INMUTABLES => Nos aseguramos que nuestra lista no se modifique a lo largo del tiempo.

# datos2[2] = "German"

datos2 = ("German", "Perez", 26)
print(
    datos2
)  ## Las tuplas pueden reasignarse si estas se crean en otro espacio en memoria, eliminando la anterior y creando una nueva.

datos3 = (
    "Juan Manuel ",
)  ## Las tuplas de un unico elemento deben llevar una coma al final, de lo contrario sera un STRING
