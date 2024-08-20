persona1 = {"name": "Mauricio", "last_name": "Cuello"}  ## Literalmente un objeto JS

## Si quisiese imprimir el nombre de la persona
print(persona1["name"])
persona2 = {"name": "Tomas", "last_name": "Tissoni"}  ## Literalmente un objeto JS

print(persona2["last_name"])

## Los diccionarios son mutables, no entran en conjuntos,

persona1["last_name"] = "Fabricio"
print(persona1)

## Modificacion del diccionario

persona1["email"] = (
    "tissonitomas5@gmail.com"  ## Si existiese la key "Email" la modificaria, de no existir la agrega.
)

print(persona1)

persona1.update(
    {  ## Update puede agregar mas de una keyvalue
        "email": "tanqueta98@gmail.com",
        "ciudad": "Don Torcuato",
    }
)

print(persona1)

del persona1["ciudad"]
## del elimina la key que le pasemos
print(persona1)

## Valor booleanos

print(
    "email" in persona1
)  ## La clave in diccionario buscara si la clave existe en el diccionario => True

persona1.pop("email")  ## Elimina por clave
print(persona1)

persona1.clear()  ## Limpia el diccionario persona1 y lo vacia
print(persona1)
