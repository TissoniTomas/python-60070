name = input("Nombre: ")
edad = int(input("Edad: "))

cumple_condiciones = (
    name != "****"
    and (edad > 5 and edad < 20)
    and (len(name) >= 4 and len(name) <= 8)
    and edad * 3 > 35
)
print(cumple_condiciones)
