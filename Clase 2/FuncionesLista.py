frase = "Hola Mundo"
datos = [
    "Mauricio",
    "Cuello",
    33,
    True,
    ["Buenos aires", "Mendoza", "Tucuman"],
]  # Nada nuevo => Coleccion de datos homogonea, puede recibir lo que sea

print(
    frase[2]
)  # Funciona como en JS, busca el indice del string o un arreglo => Imprime l
print(
    frase[1:4]
)  # El : trabaja como un slicing: Va desde la posicion 1 hasta la 4 => Imprime ola => El segundo parametro NO es incluido en el slicing
print(
    frase[1:7:2]
)  # Lo mismo que lo anterior,  el tercer parametro define la cantidad de caracteres que ira agarrando, es decir que va de 2 en 2
print(frase[-1])  # Indices negativos empiezan por el ultimo elemento a partir del -1

print(frase[2:])  # Omitir el segundo parametro ira hasta el final del string

print(frase[:4])  # Omitir el primer parametro empezara por la posicion [0]

print(frase[::-1])  # Slicing acepta valores negativos: Muestra el string dado vuelta.


print(len(frase))  # Len = algo.length

### Los strings no permiten la mutacion de su contenido, pero si es posible reasignar el valor de una variable

############## LISTAS (arrays) #####################

print(datos)

print(datos[3])
# Resuelve TRUE
print(datos[1][2])  # datos[1] = Cuello[2] = e
print(datos[4][1])  # ==> MENDOZA


dataSlice = datos[1:4]  # dataSlice recibira el slice de datos desde posicion 1 a 3
print(dataSlice)

# Concatenacion de listas
datos2 = ["CAVS", "CAI", "CARP", "CABJ"]

datos_totales = datos + datos2
print(datos_totales[::-1])

# Mutablidad de las listas ( en contraparte de los strings que NO lo son)

datos2[3] = "CASLA"  # ['CAVS', 'CAI', 'CARP', 'CASLA']
print(datos2)  # Elimina a CABJ y lo reemplaza por CASLA

# Mutabilidad por Slicing: Es posible modificar de a varios elementos en una lista. A su vez es posible eliminar elementos de la lista con este metodo

datos2[0:3] = ["CAB", "CAT", "CANCH"]  # ['CAB', 'CAT', 'CANCH', 'CASLA']
print(datos2)

datos2[0:2] = []
print(datos2)  # ['CANCH', 'CASLA']
