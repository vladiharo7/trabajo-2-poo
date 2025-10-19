# Trabajo 2: Python Programación Orientada a Objetos

## Descripcion
Desarrollar un sistema básico de inventario con POO en Python para gestionar productos y realizar operaciones de inventario.

## Requisitos
  * Crear una clase Producto con atributos para nombre, precio y cantidad
  * Implementar métodos para añadir, actualizar y mostrar información de productos
  * Desarrollar una clase Inventario que gestione una colección de productos
  * Implementar operaciones de inventario: añadir producto, buscar por nombre y calcular valor total
  * Manejar excepciones para entradas inválidas (precios negativos, nombres vacíos, etc.)
  * Crear un menú interactivo simple para probar las funcionalidades
  * Mostrar resultados de operaciones por consola de manera formateada
  * Validar que los datos ingresados sean del tipo correcto

## Instrucciones

Crea un archivo llamado sistema_inventario.py donde implementarás todo el código del sistema.

Define la clase Producto con un método constructor que inicialice los atributos nombre (str), precio (float) y cantidad (int). Incluye validaciones para que el precio no sea negativo, el nombre no esté vacío y la cantidad sea mayor o igual a cero.

Añade a la clase Producto los siguientes métodos:

actualizar_precio(nuevo_precio): para modificar el precio validando que sea positivo
actualizar_cantidad(nueva_cantidad): para modificar la cantidad validando que sea positiva
calcular_valor_total(): que devuelva el valor total (precio × cantidad)
__str__(): para mostrar la información del producto de forma legible
Crea la clase Inventario con un constructor que inicialice una lista vacía para almacenar productos.

Implementa en la clase Inventario los siguientes métodos:

  * agregar_producto(producto): para añadir un objeto de tipo Producto a la lista
  * buscar_producto(nombre): para encontrar un producto por su nombre
  * calcular_valor_inventario(): para sumar el valor total de todos los productos
  * listar_productos(): para mostrar todos los productos del inventario
  * Implementa un manejo de excepciones utilizando bloques try-except para capturar errores como valores negativos, tipos de datos incorrectos o
  productos no encontrados.

Crea una función menu_principal() que muestre opciones al usuario (1. Agregar producto, 2. Buscar producto, etc.) y procese la entrada del usuario.

En la sección principal del programa (bajo if __name__ == "__main__":), instancia un objeto de la clase Inventario y llama a la función menu_principal() para iniciar la aplicación.

## Criterios de Calificacion

### Implementación de la clase Producto
Correcta definición de la clase Producto con sus atributos (nombre, precio, cantidad) y métodos (actualizar_precio, actualizar_cantidad, calcular_valor_total, __str__). Incluye validaciones básicas para los datos.
Peso: 30%

### Implementación de la clase Inventario
Correcta implementación de la clase Inventario con métodos para agregar productos, buscar por nombre, calcular el valor total del inventario y listar todos los productos.
Peso: 30%

### Manejo de excepciones
Implementación de bloques try-except para manejar errores como valores negativos, tipos de datos incorrectos o productos no encontrados.
Peso: 20%

### Interfaz de usuario y funcionalidad
Desarrollo de un menú interactivo que permita al usuario realizar todas las operaciones solicitadas (agregar, buscar, listar productos y calcular valor total).
Peso: 20%
