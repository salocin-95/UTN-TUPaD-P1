from statistics import mode, median, mean
import random

# 1 
user_input = int(input("Ingresa tu edad: "))
if user_input > 18:
    print("Es mayor de edad")
    
# 2
user_input = int(input("Ingresa tu nota: "))
if user_input >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
# 3
user_input = int(input("Ingresa un número: "))
if user_input % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor ingrese un número par")
    
# 4  
user_input = int(input("Ingresa tu edad: "))
if user_input < 12:
    print("Niño/a")
elif 12 <= user_input < 18:
    print("Adolescente")
elif 18 <= user_input < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# 5
user_input = input("Ingresa tu contraseña: ")
if 8 <= len(user_input) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# 6
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios) 

mediana = median(numeros_aleatorios)

moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
else:
    print("Ninguna es verdad")
    
# 7
user_input = input("Ingrese una palabra o frase: ")
if user_input.endswith(("a", "e", "i", "o", "u")):
    print(user_input + "!")
    
# 8
nombre_usuario = input("Ingrese su nombre: ")
user_input = int(input("Ingrese 1 para mayúsculas, 2 para minúsculas y 3 para la primera letra en mayúscula: "))

if user_input == 1:
    nombre_usuario = nombre_usuario.upper()
    print(nombre_usuario)
elif user_input == 2:
    nombre_usuario = nombre_usuario.lower()
    print(nombre_usuario)
elif user_input == 3:
    nombre_usuario = nombre_usuario.title()
    print(nombre_usuario)
else:
    print("Elija una opción correcta")

# 9
user_input = float(input("Ingrese la magnitud del terremoto: "))
if user_input < 3:
    print("Muy leve")
elif 3 <= user_input < 4:
    print("Leve")
elif 4 <= user_input < 5:
    print("Moderado")
elif 5 <= user_input < 6:
    print("Fuerte")
elif 6 <= user_input < 7:
    print("Muy fuerte")
elif 7 <= user_input:
    print("Extremo")

# # 10
hemisferio = input("En que hemisferio te encontras? (norte/sur) ")
mes = input("Que mes? ") 
dia = int(input("Que dia? ")) 

if 21 <= dia and mes == "diciembre" or mes == "enero" or mes == "febrero" or dia <= 20 and mes == "marzo": 
    print("verano" if hemisferio == "sur" else "invierno")
elif 21 <= dia and mes == "marzo" or mes == "abril" or mes == "mayo" or dia <= 20 and mes == "junio": 
    print("otoño" if hemisferio == "sur" else "primavera")
elif 21 <= dia and mes == "junio" or mes == "julio" or mes == "agosto" or dia <= 20 and mes == "septiembre": 
    print("invierno" if hemisferio == "sur" else "verano")
elif 21 <= dia and mes == "septiembre" or mes == "octubre" or mes == "noviembre" or dia <= 20 and mes == "diciembre": 
    print("primavera" if hemisferio == "sur" else "otoño")