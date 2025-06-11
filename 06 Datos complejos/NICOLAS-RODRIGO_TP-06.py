import math

# 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(precios_frutas)


precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

# 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

# 3
lista = []
for key in precios_frutas:
    lista.append(key)
print(lista)

# 4
contactos = {}
n = 0
while n < 5:
    n += 1
    contacto = input("Ingresa el nombre: ")
    numero = input("Ingresa el número: ")
    contactos[contacto] = numero

contacto = input("Ingresa el contacto que queres buscar: ")
print(f"El numero de {contacto} es {contactos[contacto]}")

# 5
frase = input("Ingrese una frase: ")
frase_lista = frase.split()
frase_dict = set(frase_lista)
contador = {}
for palabra in frase_lista:
    contador[palabra] = frase_lista.count(palabra) 

print(f"Palabras únicas: {frase_dict}")
print(f"Recuento: {contador}")

# 6
alumnos = {
    "Sofía": (10, 9, 8),
    "Luis": (6, 7, 7),
    "Rodrigo": (4, 5, 8)
}

for alumno in alumnos:
    tupla = alumnos[alumno]
    lista = [*tupla]
    lista = sum(lista)
    promedio = lista/3
    print(f"{alumno}: Su promedio es {math.trunc(promedio)}")

# 7
parcial1 = {2, 3, 4, 5, 6}
parcial2 = {3, 6, 7, 8, 9}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# 8
productos = {
    "zanahorias": 9,
    "lechugas": 4,
    "cebollas": 7
}

producto = input("Ingresá el nombre del producto: ")

if producto in productos:
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    productos[producto] += agregar
    print(f"Nuevo stock de {producto}: {productos[producto]}")
else:
    nuevo_stock = int(input("Producto nuevo. Ingresá el stock inicial: "))
    productos[producto] = nuevo_stock
    print(f"Producto {producto} agregado con {nuevo_stock} unidades.")

# 9
agenda = {
    ("lunes", "12:00"): "Gimnasio",
    ("martes", "15:00"): "Sesión de estudio",
    ("miercoles", "18:00"): "Salir a caminar"
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (ej: 10:00): ")

clave = (dia, hora)

if clave in agenda:
    print(f"Actividad: {agenda[clave]}")
else:
    print("No hay actividades programadas.")


# 10
paises = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Colombia": "Bogota"
}

invertido = {}

for pais, capital in paises.items():
    invertido[capital] = pais

print("Diccionario original:", paises)
print("Diccionario invertido:", invertido)