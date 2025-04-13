from math import pi

# 1
def imprimir_hola_mundo():
    print('Hola Mundo!')
  
# 2  
def saludar_usuario(nombre):
    print(f"Hola {nombre}")
  
# 3  
def informacion_personal(nombre, apellido, edad, residencia):
    while edad.isnumeric() == False:
        edad = input("Ingrese un numero: ")
    print(f"Soy {nombre} {apellido} tengo {edad} y vivo en {residencia}")
    
# 4
def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return f"{area:.2f}"

def calcular_permietro_circulo(radio):
    perimetro = 2 * pi * radio
    return f"{perimetro:.2f}"

# 5
def segundo_a_horas(segundos):
    horas = segundos / 3600
    return horas

# 6
def tabla_multiplicar(numero):
    i = 1
    while i <= 10:
        resultado = i * numero
        print(f"{i} x {numero} = {resultado}")
        i += 1

# 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division) 

# 8
def calcular_imc(peso, altura):
    imc = peso / (altura/100) ** 2
    return f"{imc:.2f}"

# 9
def celsius_a_farenheit(celsius):
    farenheit = (celsius  * (9 / 5)) + 32
    return f"{farenheit:.2f}"

# 10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return f"{promedio:.2f}"