## Conjuntos o set : Coleccion no ordenada de objetos unicos, es decir que no se repite un elemento en el set.
name = "pepe"
datos1 = ["Mauricio", "Cuello", 33, True, ("Bs as", "Cordoba", "Mendoza", "Gral Pico")]
datos2 = ("Mauricio", "Cuello", 33, True, ("Bs as", "Cordoba", "Mendoza", "Gral Pico"))
datos3 = {"Mauricio", "Cuello", 33, True, ("Bs as", "Cordoba", "Mendoza", "Gral Pico")}

print(datos1)
print(datos2)
print(datos3)  ## El conjunto se imprime de manera aleatoria, ya que no es ordenada.
## El conjunto no puede guardar datos que sean mutables (listas)

datos4 = (
    set()
)  ## La funcion set crea un conjunto, si no le pasamos nada creara un conjunto vacio que es la forma correcta de hacerlo.
datos5 = set(name)
## El set se formara por "p" y "e", en cualquier orden ya que solo guarda unicos valores

## A un set tampoco podriamos indicarle posicion, ya que es una lista NO ordenada. Tampoco slicing
## El conjunto es MUTABLE.

datos3.add(50)
## funcion .add agrega a un set un elemento
print(datos3)
print(len(datos3))

datos3.update(
    {"Tilo", "Flores"}
)  ## Update agregara los elementos del conjunto que se pasen por parentesis.
datos3.discard("Cuello")  ## Discard elimina el elemento que se pase.
# datos3.remove("Tomasito") ## => Esto arrojara un error si el elemento no existe. Si existe trabaja igual que el discard.
print(datos3)
print(len(datos3))

datos3.pop()  ## Pop eliminara un elemento del conjunto "al azar"

print(datos3)

datos3.clear()  ## Vacia el set
print(datos3)
