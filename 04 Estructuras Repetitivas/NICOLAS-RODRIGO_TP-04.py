import math, random

# 1
n = 0
while n <= 100:
    print(n)
    n += 1
    
# 2
user_input = int(input("Ingrese un número: "))
contador = 0
while user_input > 0:
    user_input = math.floor(user_input / 10)
    contador += 1
print(f"Digitos: {contador}")

# 3
primer_valor = int(input("Ingrese un valor: "))
segundo_valor = int(input("Ingrese un valor: "))
suma = 0

if primer_valor < segundo_valor:
    a = primer_valor
    b = segundo_valor
if primer_valor > segundo_valor:
    a = segundo_valor
    b = primer_valor

a = a + 1

for i in range(a, b):
    print(i)
    suma += i
    
print(suma)

# 4
user_input = int(input("Ingrese un número: "))
suma = 0
while user_input != 0:
    suma += user_input
    user_input = int(input("Ingrese un número: "))
print(suma)

# 5
user_input = int(input("Adivina un número entre 0 y el 9: "))
numero = random.randint(0, 9)
intentos = 0
while user_input != numero:
    intentos += 1
    user_input = int(input("Adivina un número entre 0 y el 9: "))

print(f"El numero era {numero} y te llevo {intentos} intentos")    

# 6
n = 100
while n >= 0:
    print(n)
    n -= 1
    
# 7
user_input = int(input("Ingresa un número: "))
suma = 0
for i in range(user_input):
    suma += i + 1
print(suma)

# 8
pares = 0
impares = 0
negativos = 0
positivos = 0
n = 0
while n < 100:
    n += 1
    user_input = int(input("Ingrese un número: "))
    if user_input % 2 == 0:
        pares += 1
    else:
        impares += 1
    if user_input > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Pares: {pares} Impares: {impares} Positivos: {positivos} Negativos: {negativos}")

# 9
n = 0
suma = 0
while n < 100:
    n += 1
    user_input = int(input("Ingrese un numero: "))
    suma += user_ineput
print(f"La media es {suma/n}")

# 10
user_input = input("Ingresa un número: ")
valores = ""
i = len(user_input)
while i > 0:
    i -= 1
    valores += user_input[i]
print(valores)