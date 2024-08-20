## LISTAS

numeros = [1, 2, 3, 4, 5]

numeros.extend(
    [6, 7, 8, 9]
)  ## Extend agrega la nueva lista a la lista original, la muta

print(numeros)

numeros.insert(0, 0)  ## Inserta un elemento en la posicion indicada (posicion,elemento)
print(numeros)

numeros.insert(len(numeros) + 1, 10)
print(numeros)

## SORT

numerosDesorden = [2, 40, 32, -20, 11]
numerosDesorden.sort(reverse=True)
print(numerosDesorden)
