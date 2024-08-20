clubes = {"velez": "CAVS", "boca": "CABJ", "river": "CARP", "san lorenzo": "CASLA"}
print(
    clubes.get("huracan", "tu club no es grande")
)  ## get: Si la clave enviada como primer parametro existe, devuelve su valor, de no existir, devuelve el segundo parametro.

print(clubes.keys())  ## Devuelve una lista con las claves del dicc
print(clubes.values())  ## Analogamente, values devuelve los valores del dicc
print(clubes.items())  ## Devuelve una lista de TUPLAS con cada tupla las claves valores
