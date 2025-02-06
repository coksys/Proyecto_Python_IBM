class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self._nombre = nombre
        self._categoria = categoria
        self._precio = precio
        self._cantidad = cantidad

    # Getters y Setters
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if isinstance(value, str) and value.strip():
            self._nombre = value
        else:
            raise ValueError("El nombre del producto debe ser una cadena no vacía.")

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, value):
        if isinstance(value, str) and value.strip():
            self._categoria = value
        else:
            raise ValueError("La categoría del producto debe ser una cadena no vacía.")

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._precio = value
        else:
            raise ValueError("El precio del producto debe ser un número mayor que cero.")

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, value):
        if isinstance(value, int) and value >= 0:
            self._cantidad = value
        else:
            raise ValueError("La cantidad del producto debe ser un número no negativo.")

    def __str__(self):
        return f"Nombre: {self.nombre}, Categoría: {self.categoria}, Precio: {self.precio}, Cantidad: {self.cantidad}"


class Inventario:
    def __init__(self):
        self._productos = []

    # Agregar un producto
    def agregar_producto(self, nombre, categoria, precio, cantidad):
        for producto in self._productos:
            if producto.nombre == nombre and producto.categoria == categoria:
                raise ValueError(f"El producto '{nombre}' ya existe en el inventario.")
        
        nuevo_producto = Producto(nombre, categoria, precio, cantidad)
        self._productos.append(nuevo_producto)

    # Actualizar un producto
    def actualizar_producto(self, nombre, nueva_categoria=None, nuevo_precio=None, nueva_cantidad=None):
        for i, producto in enumerate(self._productos):
            if producto.nombre == nombre:
                if nueva_categoria is not None:
                    producto.categoria = nueva_categoria
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                return f"Producto '{nombre}' actualizado."
        raise ValueError(f"No se encontró el producto '{nombre}'.")

    # Eliminar un producto
    def eliminar_producto(self, nombre):
        for i, producto in enumerate(self._productos):
            if producto.nombre == nombre:
                del self._productos[i]
                return f"Producto '{nombre}' eliminado."
        raise ValueError(f"No se encontró el producto '{nombre}'.")

    # Mostrar inventario
    def mostrar_inventario(self):
        if not self._productos:
            print("El inventario está vacío.")
        else:
            for producto in self._productos:
                print(producto)

    # Buscar un producto por nombre
    def buscar_producto(self, nombre):
        encontrado = False
        for producto in self._productos:
            if producto.nombre == nombre:
                print(producto)
                encontrado = True
        if not encontrado:
            raise ValueError(f"No se encontró el producto '{nombre}'.")


# Función principal para probar la aplicación
def main():
    inventario = Inventario()

    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar Producto")
        print("2. Actualizar Producto")
        print("3. Eliminar Producto")
        print("4. Mostrar Inventario")
        print("5. Buscar Producto")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Introduzca el nombre del producto: ")
            categoria = input("Introduzca la categoría del producto: ")
            precio = float(input("Introduzca el precio del producto: "))
            cantidad = int(input("Introduzca la cantidad en stock: "))
            inventario.agregar_producto(nombre, categoria, precio, cantidad)
        elif opcion == '2':
            nombre = input("Introduzca el nombre del producto a actualizar: ")
            nueva_categoria = input("Introduzca la nueva categoría (deje vacío si no desea cambiarla): ")
            nuevo_precio = input("Introduzca el nuevo precio (deje vacío si no desea cambiarlo): ")
            nueva_cantidad = input("Introduzca la nueva cantidad en stock (deje vacío si no desea cambiarla): ")

            if nueva_categoria:
                nueva_categoria = nueva_categoria
            if nuevo_precio:
                nuevo_precio = float(nuevo_precio)
            if nueva_cantidad:
                nueva_cantidad = int(nueva_cantidad)

            inventario.actualizar_producto(nombre, nueva_categoria, nuevo_precio, nueva_cantidad)
        elif opcion == '3':
            nombre = input("Introduzca el nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '4':
            inventario.mostrar_inventario()
        elif opcion == '5':
            nombre = input("Introduzca el nombre del producto a buscar: ")
            try:
                inventario.buscar_producto(nombre)
            except ValueError as e:
                print(e)
        elif opcion == '0':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

    print("Saliendo...")


if __name__ == "__main__":
    main()