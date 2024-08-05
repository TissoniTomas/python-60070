# Clase 1 - Numeros y cadenas de caracteres

# print('Hola Mundo')

'''
# En Javascript = typeof
print(type(123)) # Tipo Entero
print(type(123.5)) # Tipo Flotante (Decimal)
print(type(5j)) # Tipo Complejo se utiliza J
'''

# Calculos basicos

'''
print ( 5 + 4)
print ( 10 * 2)
print( 10 / 3)
print( 10 // 3) Division entera, sin decimales redondeando
print(10 % 3) Resto de la division = 1 
'''

# Cadena de caracteres

# print(type('Hola Perrito')) 
# print('Mauricio\nMacri\nTHE CHAD')

# print('Latinoamerica es un continente "muy rico" ')

# print("""Este es un parrafo
# de varias lineas
# con sintaxis correcta""")

# Concatenacion 
# print('Hola ' + 'perrito malvado')
# print ('2' + '2') # Concatenara en forma de string, no en forma numerica

### VARIABLES ###

edad = 33;
# Las variables en PY al parecer no tienen categoria como JS (let, const)
# El tipo de dato de una variable esta definido por el contenido, no por el contenedor ==> La variable estara definida por la informacion que le de a la variable, si es numerico o de tipo texto string lo que fuese 
print(type(edad))

edad = "Perrito"

print(type(edad))

# Las variables pueden ser reasignadas a cualquier valor

edad = 30;
nombre = "Tomas"

# print("Hola" + nombre +"tenes" + edad + "años")

#No es posible concatenar strings con enteros, se debe concatenar strings con strings


print("Hola " + nombre + " tenes " + str(edad) + " años")

# Las variables no pueden empezar con numeros
# Python es Case sensitive, detecta mayusculas y minusculas.

### INPUT ###

name = input("Ingrese su name: ")
edad = input(("Ingrese su edad: "))

edadInt = int(edad)
# Todo lo ingresado via input sera almacenado como string
print("Su nombre y edad son: " + name + str(edadInt))