### FUNCIONES DE LISTA

nombre = "Tomas"
clubes = ["CAVS", "CABJ", "CARP", "RC"]

print(nombre.lower())  ## .lower = Lleva el string a minusculas
print(nombre.upper())  ## .upper = Lleva el string a mayusculas

clubes.append("CASLA")  ##.append = Agrega un elemento a la lista al final (.push en JS)
clubes.append(
    10 + 20
)  # Python trata de resolver primero lo que esta dentro de parentesis para realizar la funcion. Va de adentro hacia afuera
print(clubes)
print(len(clubes))

clubes.pop(
    5
)  ## .pop = Elimina un elemento en el indice indicado => No indicarle indice eliminara el ultimo valor (-1)
print(clubes)

print(
    clubes.count("CASLA")
)  ## .count = Cuenta las veces que aperece en una lista un determinado elemento.

print(clubes.index("CABJ"))  ## .index = Cuenta el indice de un elemento en una lista.
