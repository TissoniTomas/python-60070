set1 = {1, 2, 3, 4}

set2 = (
    set1.copy()
)  ### .copy = Copia los elementos del conjunto original a una nueva variable. No se reasigna como set2 = set1 ya que estariamos referenciado a set1

set3 = {4, 5, 6}

print(
    set1.isdisjoint(set2)
)  ## Devuelve FALSE ya que set 1 y set 4 tienen interseccion en el elemento 4, si fueran completamente distintos devolveria TRUE

print(
    set3.issubset(set1)
)  ## Issubset pregunta si set1 es subconjunto de set3, lo cual es FALSE: los elementos de set3 no viven en set1

print(
    set3.issuperset(set1)
)  ## Inverso de issubset, pregunta si set3 tiene todos los elementos de set1

setUnion = set1.union(set3)
## union es una especie de concat en conjuntos: Junta los elementos no comunes de ambas listas, los comunes los coloca una unica vez.
print(setUnion)  ##

print(set3.difference(set1))  ## Muestra los elementos del set3 que no viven en set1
## difference_update en cambio MUTARA a set3, difference a secas no muta a set3

print(
    set3.intersection(set1)
)  ## Imprime los elementos en comun entre ambos, tambien tiene una version UPDATE
