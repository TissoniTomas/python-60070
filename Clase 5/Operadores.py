lista = [1, 2, 3, 4, True, [True, 10]]
print(
    lista.count(True)
)  ## Imprime 2 no por el True dentro del array, si no que para PY True == 1 y False == 0;
print(1 == True)

print(5 > True)
print(
    10 != 5 + 5
)  ## Operadores basicos = == (igual), != (distinto), > (mayor que), >= (mayor o igual que), < (menor que), <= (menor o igual que)
print("hola" != "Hola")

## NOT , OR, AND
resultado = 5 * 2 == 10
print(resultado)
print(
    not resultado
)  ## El operador NOT funciona como ! en JS, dara el opuesto del resultado esperado (booleano en teoria).

resultado1 = 2 == 1 + 1
resultado2 = 2 == 1 + 2

print(
    resultado1 and resultado2
)  ## AND funciona como && en JS, valdra si ambas cosas son verdades => FALSE

print(
    resultado1 or resultado2
)  ## OR funciona como la doble barra en JS, valdra si una de ambas cosas son verdaderas => TRUE

""" Orden de precedencia frente a multiples operadores logicos
1) NOT
2) AND
3) OR

False or False and Not False or True
False or False and True or True
False or False or True
False or True
True

Los parentesis pueden afectar el orden de precedencia de operadores logicos


"""
