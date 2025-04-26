# 1
lista = []
for _ in range(0, 100, 4):
    lista.append(_)

print(lista)

# 2
lista = ['rodrigo', 'nicolas', 29, True, False]
print(lista[4])

# 3
lista = []
lista.append('palabra')
lista.append('segunda')
lista.append('tres')
print(lista)

# 4
animales = ["perro", "gato", "conejo", "pez"]
print(animales)
animales[1] = "loro"
animales[3] = "oso"
print(animales)

# 5
# Selecciona el número con valor mas alto de la lista y lo remueve.

# 6
lista = []
for _ in range(10, 31, 5):
    lista.append(_)

print(lista[0], lista[1])

# 7
autos = ["seda", "polo", "suran", "gol"]
print(autos)
autos[1] = "milanesa"
autos[2] = "zapallo"
print(autos)

# 8
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print(dobles)

# 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], 
["agua"]]

print(compras)
compras[2].append("jugo")
print(compras)
compras[1][1] = "tallarines"
print(compras)
compras[0].remove("pan")
print(compras)

# 10
lista_anidada = [15, True, [25.5, 57.9, 30.6]]
print(lista_anidada)