# 1

def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n-1)

user_input = int(input("Ingrese un número: "))

for i in range(1, user_input + 1):
    print(f"El factorial de {i} es: {factorial(i)}")

# 2

def fibonacci(pos):
    if pos==0:
        return 0
    elif pos==1:
        return 1
    else:
        return fibonacci(pos-1) + fibonacci(pos-2)
    
user_input = int(input("Ingrese un número: "))

print(f" El valor de fibonacci en la pos {user_input} es {fibonacci(user_input)}")
for i in range(0, user_input+1):
    print(f" El valor de fibonacci en la pos {i} es {fibonacci(i)}")

# 3
def potencia(n, m):
    if m == 0:
        return 1
    elif m == 1:
        return n
    else:
        return n * (potencia(n, m-1))

print(potencia(2,5))

# 4
def binario(numero):

    if numero == 0:
        return "0"
    if numero//2 == 0:
        return str(numero%2)
    else:
        return binario(numero//2) + str(numero%2)

print(binario(10))
print(binario(19))
print(binario(25))

# 5
def es_palindromo(palabra):

    if len(palabra) <= 1:
        return True    
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:len(palabra)-1])

palabra = "palabra"  
print(es_palindromo(palabra))
palabra = "qwertytrewq"  
print(es_palindromo(palabra))
palabra = "acurruca"  
print(es_palindromo(palabra))

# 6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n//10) 

print(suma_digitos(1234))
print(suma_digitos(9))
print(suma_digitos(305))

# 7
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(1))
print(contar_bloques(2))
print(contar_bloques(4))

# 8
def contar_digito(numero, digito):
    if 9 > digito < 0:
        return False
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero//10, digito)
    else:
        return 0 + contar_digito(numero//10, digito)

print(contar_digito(0, 2))
print(contar_digito(0, 10))
print(contar_digito(12233421, 2))
print(contar_digito(5555, 5))
print(contar_digito(123456, 7))