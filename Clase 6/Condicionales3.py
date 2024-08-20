año = int(input("Ingrese su año de nacimiento: "))

if año >= 1920 and año <= 1940:
    print("Generacion silenciosa")
elif año >= 1946 and año <= 1964:
    print("Baby Boomer")
elif año >= 1965 and año <= 1979:
    print("Generacion X")

elif año >= 1980 and año <= 2000:
    print("Generacion Y")
elif año >= 2001 and año <= 2010:
    print("Generacion Z")
else:
    print("Generacion no matcheada")
