from math import pi

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
class Persona():
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad 
    
    def saludar(self):
        print(f"Hola! Soy {self.nombre}, vivo en {self.pais} y tengo {self.edad} años.")
        
persona = Persona('Rodrigo', 'Argentina', 29)
persona.saludar()

# 5
class Circulo():
    
    def __init__(self, radio):
        self.radio = radio
        
    def calcular_area(self):
        return round(pi * self.radio ** 2, 2)

    def calcular_perimetro(self):
        return round(2 * pi * self.radio, 2)
    
circulo = Circulo(25)
print(circulo.calcular_area())
print(circulo.calcular_perimetro())

# 6
string_a = "({[]})"
string_b = "({[})"
class Pila():
    
    def __init__(self):
        pass

# 7
class Cola():
    
    def __init__(self):
        self.clientes = []
    
    def encolar(self, cliente):
        self.clientes.append(cliente)
        pass
    
    def desencolar(self):
        self.clientes.pop()
        pass
    
    def esta_vacia(self):
        return len(self.clientes) == 0
    
    def mostar_cliente(self):
        return self.clientes[-1] if not self.esta_vacia() else "No hay clientes en la cola"
    
cola = Cola()

print(cola.clientes)

# Demuestra que pasa cuando la cola esta vacia
print(cola.mostar_cliente())

cola.encolar('rodrigo')
print(cola.mostar_cliente())

cola.encolar('nicolas')
print(cola.mostar_cliente())

cola.encolar('ezequiel')
print(cola.mostar_cliente())
print(cola.clientes)

cola.desencolar()
print(cola.clientes)
print(cola.mostar_cliente())

# 8
class Nodo():
    
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class ListaEnlazada():
    
    def __init__(self):
        self.cabeza = None
        
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
    
    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
        
    def invertir(self):
        actual = self.cabeza
        while actual:
            print(actual.siguiente, end= " -> " )
            actual = self.cabeza
        print("None")
           
lista = ListaEnlazada()
lista.insertar(3)
lista.insertar(2)
lista.insertar(1)
lista.mostrar()

# 9
lista.invertir()