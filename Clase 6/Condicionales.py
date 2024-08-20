name = input("Ingrese su nombre :")

if len(name) > 5:  # Las respuestas de un condicional siempre seran TRUE o FALSE
    print("Su nombre es muy largo")
    if name[0] == ("T" or "t"):
        print("Su nombre empieza con T")
if name == name.capitalize():
    print("Su nombre esta bien escrito")

print("Ya no estoy en el IF")
