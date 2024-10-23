#Primero importar las clases creadas para llamarlos en el main
from prenda import Prenda
from ropahombre import RopaHombre
from ropamujer import RopaMujer
from inventario import Inventario

# Crear instancias de RopaHombre y RopaMujer
camisa = RopaHombre("Camisa de Hombre", 25.00, 50, "M")
pantalon = RopaHombre("Pantalón de Hombre", 30.00, 30, "L")
pollera = RopaMujer("Falda de Mujer", 28.00, 15, "S")
blusa = RopaMujer("Blusa de Mujer", 22.00, 40, "M")

# Crear el inventario y agregar las prendas
inventario = Inventario()
inventario.agregar_prenda(camisa)
inventario.agregar_prenda(pantalon)
inventario.agregar_prenda(pollera)
inventario.agregar_prenda(blusa)

# Mostrar el inventario
inventario.mostrar_inventario()

#Le añadi mas funcionalidades para probar mi codigo
# Simular la compra de una prenda
#print("\nProceso de compra:")
#inventario.comprar_prenda("Camisa de Hombre", 5)

# Mostrar inventario después de la compra
#print("\nInventario actualizado:")
#inventario.mostrar_inventario()

# Función para procesar la compra del usuario
def realizar_compras(inventario):
    total_compra = 0
    while True:
        try:
            opcion = int(input("Selecciona el número del artículo que deseas comprar (0 para salir): "))
            if opcion == 0:
                break

            cantidad = int(input("¿Cuántas unidades quieres comprar?: "))
            total_compra += inventario.comprar_prenda(opcion - 1, cantidad)

        except (ValueError, IndexError):
            print("Opción inválida, intenta de nuevo.")
        
    print(f"\nCompra finalizada. Total a pagar por todas las prendas: ${total_compra:.2f}")

# Procesar la compra interactiva del usuario
realizar_compras(inventario)