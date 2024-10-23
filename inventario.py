#Abstraccion
class Inventario:
    def __init__(self):
        self.prendas = [] # Lista para almacenar las prendas

    def agregar_prenda(self, prenda):
        self.prendas.append(prenda) # Agrega la prenda a la lista
    
    """
    def mostrar_inventario(self):
        if not self.prendas:
            print("El inventario está vacío.")
        else:
            for prenda in self.prendas:
                prenda.mostrar_info() # Muestra la información de cada prenda
                print("-" * 30) #Esta es para tener una linea que separe cada prenda

    def comprar_prenda(self, nombre, cantidad):
        for prenda in self.prendas:
            if prenda.nombre == nombre:
                prenda.actualizar_stock(cantidad)
                return
        print(f"No se encontró la prenda {nombre} en el inventario.") 
    """

    def mostrar_inventario(self):
        print("Inventario disponible:")
        for i, prenda in enumerate(self.prendas):
            print(f"{i + 1}. ", end="")
            prenda.mostrar_info()
            print("-" * 30)

    def comprar_prenda(self, indice_prenda, cantidad):
        prenda = self.prendas[indice_prenda]
        if prenda.actualizar_stock(cantidad):
            total = prenda.precio * cantidad
            print(f"Compra exitosa. Total a pagar: ${total:.2f}")
            return total
        return 0