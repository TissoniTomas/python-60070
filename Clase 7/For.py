### --------------------------------###
# contrasenia = "Homero123"
# valor_ingresado = input("Ingrese su contraseña: ")

# while (contrasenia != valor_ingresado):
#     print("Contraseña incorrecta, vuelva a intentarlo")
#     valor_ingresado = input("Ingrese su contraseña: ")  

# numero = int(input("Ingrese un numero y le mostrare todos los anteriore a este: "))

# while (numero != 0):
#     print(numero - 1 )
#     numero -= 1
    
### --------------------------------###
### --------------------------------###
# numero = int(input("Ingrese un numero: "))
# i = 1

# while i < numero:
#     if (i > 10):
#         break; #BREAK: Corta el while y sale-
#     if(i % 3 == 0):
#         i += 1
#         continue; #CONTINUE: Pasa a la siguiente vuelta del bucle
#     print(i)
#     i+= 1

### --------------------------------###

# numero = int(input("Ingrese el numero secreto: "))
# numero_secreto = 23
# intentos = 3

# while (numero != numero_secreto):
#     intentos -= 1
#     print(f"Error. Le quedan {intentos} intentos")
#     if(intentos == 0):
#         break;
#     numero = int(input("Ingrese el numero secreto: "))

### --------------------------------###
### --------------------------------###

suma_total = 0
numero_ingresado = (input("Ingrese un numero, si quiere salir escriba exit(): "))

while(numero_ingresado != "exit()"):
    if(type(numero_ingresado) != int ):
        print("Error. Solo valores numericos")
    suma_total += int(numero_ingresado)
    numero_ingresado = (input("Ingrese un numero, si quiere salir escriba exit(): "))
    
print(f"La suma de los valores ingresados es {suma_total}")