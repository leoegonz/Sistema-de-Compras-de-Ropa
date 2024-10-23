#Encapsulamiento
class Prenda:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre # Atributo público
        self.precio = precio # Atributo público
        self.cantidad = cantidad # Atributo público

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Precio: ${self.precio}, Stock: {self.cantidad}")
    
    #def actualizar_stock(self, cantidad_comprada):
     #   if cantidad_comprada <= self.cantidad:
         #   self.cantidad -= cantidad_comprada
      #      print(f"Se han comprado {cantidad_comprada} unidades de {self.nombre}. Stock restante: {self.cantidad}")
       # else:
        #    print(f"ERROR! No hay suficiente stock de {self.nombre}. Existen {self.cantidad} unidades disponibles.")

    def actualizar_stock(self, cantidad_comprada):
        if cantidad_comprada <= self.cantidad:
            self.cantidad -= cantidad_comprada
            return True  # Compra exitosa
        else:
            print(f"ERROR! No hay suficiente stock de {self.nombre}. Existen {self.cantidad} unidades disponibles.")
            return False  # Compra fallida