name = "tOMAS"

print(
    name.capitalize()
)  ## Capitalize pone en mayuscula la inicial, o corrije la palabra de forma que quede asi

name2 = "tOMAS tissoNI"

print(name2.title())  ## Lo mismo que capitalize pero con mas palabras.

print(
    name2.find("t")
)  ## .find devuelve el indice donde se encuentra lo que buscamos como parametro => A diferencia del index, este si no encuentra nada devuelve -1, index devuelve error

print(name2.rfind("t"))  ## Analogo al find pero devuelve el ultimo match

frase = "Hola mundo como va"

print(
    frase.split("como")
)  ## spli parte el string y devuelve una lista, el parametro enviado sera el "separador" si no le ponemos parametro partira todo el string por comas.

frase2 = "------- Quiero eliminar los guiones -----"

print(frase2.strip("-"))  ## Elimina los caracteres explicados en el argumento
