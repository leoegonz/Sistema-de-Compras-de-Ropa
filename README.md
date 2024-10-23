# Sistema-de-Compras-de-Ropa
Programa de compra de ropas utilizando POO en Python.
-  El sistema debe permitir al usuario seleccionar entre diferentes ítems de ropa (camisas, pantalones, zapatos, etc.) y procesar la compra. Para ello, implementarán clases que representen los productos, categorías y la tienda. Además, deberán demostrar el uso de los 4 pilares de POO, empleando herencia, encapsulación, polimorfismo y abstracción.

--- Codigo base utilizado ---
Ejemplo de Encapsulamiento
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre  # Atributo público
        self.precio = precio  # Atributo público
        self.cantidad = cantidad  # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")
Ejemplo de Herencia
class RopaHombre(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)  # Llamada al constructor de la clase padre
        self.talla = talla  # Atributo específico de RopaHombre

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre
        print(f"Talla: {self.talla}")
Ejemplo de Polimorfismo
class RopaMujer(Prenda):
    def __init__(self, nombre, precio, cantidad, talla):
        super().__init__(nombre, precio, cantidad)
        self.talla = talla

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Talla: {self.talla}")
Ejemplo de Abstracción
class Inventario:
    def __init__(self):
        self.prendas = []  # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda)  # Agrega la prenda a la lista

    def mostrar_inventario(self):
        for prenda in self.prendas:
            prenda.mostrar_info()  # Muestra la información de cada prenda

Ejemplo de Implementación
#Crear instancias de RopaHombre y RopaMujer
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
falda = RopaMujer("Falda de Mujer", 28.00, 15, "S")

#Crear el inventario y agregar las prendas
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(falda)

#Mostrar el inventario
inventario.mostrar_inventario()

# Clases a Crear
1. Clase Prenda:
Atributos: nombre, precio, cantidad.
Métodos: mostrar_info().

2. Clase RopaHombre:
Hereda de Prenda.
Atributos adicionales: talla.
Método: mostrar_info().

3. Clase RopaMujer:
Hereda de Prenda.
Atributos adicionales: talla.
Método: mostrar_info().

4. Clase Inventario:
Atributo: prendas (lista).
Métodos: agregar_prenda(), mostrar_inventario().