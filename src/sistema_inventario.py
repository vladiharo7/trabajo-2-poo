'''
Módulo de sistema de inventario que permite gestionar productos, 
incluyendo agregar, buscar y calcular el valor total del inventario.
'''

class Producto:
    ''' Clase que representa un producto en el inventario.'''

    __slots__ = ['nombre', 'precio', 'cantidad']

    def __init__(self, nombre: str, precio: float, cantidad: int):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def actualizar_precio(self, nuevo_precio: float):
        ''' Actualiza el precio del producto. '''
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad: int):
        ''' Actualiza la cantidad del producto. '''
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self.cantidad = nueva_cantidad

    def calcular_valor_total(self) -> float:
        ''' Calcula el valor total del producto en inventario. '''
        return self.precio * self.cantidad

    def __str__(self) -> str:
        return f"Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"

class Inventario:
    ''' Clase que gestiona una colección de productos en el inventario.'''

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto: Producto):
        ''' Agrega un producto al inventario. '''
        self.productos.append(producto)

    def buscar_producto(self, nombre: str) -> Producto:
        ''' Busca un producto por su nombre. '''
        producto = next(filter(lambda p: p.nombre == nombre, self.productos), None)
        if producto is None:
            raise ValueError("Producto no encontrado.")
        return producto


    def calcular_valor_inventario(self) -> float:
        ''' Calcula el valor total del inventario. '''
        return sum(producto.calcular_valor_total() for producto in self.productos)

    def listar_productos(self) -> str:
        ''' Lista todos los productos en el inventario. '''
        return "\n".join(str(producto) for producto in self.productos)


def menu_principal():
    ''' Función que muestra el menú principal y procesa las opciones del usuario. '''
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Calcular valor total del inventario")
        print("4. Listar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                nombre = input("Ingrese el nombre del producto: ")
                precio = float(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                producto = Producto(nombre, precio, cantidad)
                inventario.agregar_producto(producto)
                print("Producto agregado exitosamente.")

            elif opcion == '2':
                nombre = input("Ingrese el nombre del producto a buscar: ")
                producto = inventario.buscar_producto(nombre)
                print(f"Producto encontrado: {producto}")

            elif opcion == '3':
                valor_total = inventario.calcular_valor_inventario()
                print(f"Valor total del inventario: {valor_total}")

            elif opcion == '4':
                print("Productos en el inventario:")
                print(inventario.listar_productos())

            elif opcion == '5':
                print("Saliendo del sistema de inventario.")
                break

            else:
                print("Opción inválida. Por favor, intente de nuevo.")

        except ValueError as e:
            print(f"Error: {e}")

        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    menu_principal()
