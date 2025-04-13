from funciones import imprimir_hola_mundo, saludar_usuario, informacion_personal, calcular_area_circulo 
from funciones import calcular_permietro_circulo, segundo_a_horas, tabla_multiplicar, operaciones_basicas, calcular_imc, celsius_a_farenheit, calcular_promedio

# # 1
def main():
    imprimir_hola_mundo()
# 2
    saludar_usuario("Rodrigo")
# 3
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = input("Ingresa tu edad: ")
    residencia = input("Ingresa tu residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
# 4
    radio = int(input("Ingrese el radio de un circulo: "))
    print(calcular_area_circulo(radio))    
    print(calcular_permietro_circulo(radio))    
# 5
    segundos = int(input("Ingrese la cantidad de segundos: "))
    print(segundo_a_horas(segundos))
# 6
    numero = int(input("Ingrese un número: "))
    tabla_multiplicar(numero)
# 7
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese un número: "))
    while b == 0:
        b = int(input("Ingrese un número distinto de cero: "))
    print(operaciones_basicas(a, b))
# 8
    peso = int(input("Ingrese su peso en kilos: "))
    altura = int(input("Ingrese su altura en centimetros: "))
    print(calcular_imc(peso, altura))
# 9
    celsius = int(input("Ingrese la temperatura en celsius: "))
    print(celsius_a_farenheit(celsius))
    
# 10
    a = int(input("Ingrese un número: "))
    b = int(input("Ingrese un número: "))
    c = int(input("Ingrese un número: "))
    print(calcular_promedio(a, b, c))

if __name__ == "__main__":
    main()