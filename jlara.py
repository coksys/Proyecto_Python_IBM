# Alumno: javier.lara.laboral@gmail.com
# Al consultar a la IA, me aconsejaba crear 2 clases independientes, pero he preferido crear una herencia entre clases
# No he utilizado decoradores porque no me ha dado tiempo a ver bien cómo funcionan


class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__cantidad = cantidad
    
    # getters
    def get_nombre (self, nombre):
        return self.__nombre
    
    def get_categoria (self, categoria):
        return self.__categoria
    
    def get_precio (self, precio):
        return self.__precio
    
    def get_cantidad (self, cantidad):
        return self.__cantidad

    # setters
    def set_nombre (self, nombre): # nombre solamente con letras, sin números ni símbolos
        if nombre.isalpha():
            get_nombre = nombre
            return True            # permite alterar comportamiento de condicional o bucle
        else:
            print("Tiene que introducir un nombre que contenga únicamente letras.")

    def set_categoria (self, categoria):    # la categoría puede adoptar todos los caracteres
        get_categoria = categoria    # ejemplos: moda+, calzado nuevo (outlet), 4K

    def set_precio (self, precio):    # el precio debe ser superior a cero
        if precio > 0:
            get_precio = precio
            return True
        elif precio <= 0:
            print("Tiene que ser un valor superior a cero.")
        else:
            print("El precio tiene que ser un número superior a cero.")

    def set_cantidad (self, cantidad): # la cantidad debe ser positiva o nula
        if cantidad >= 0:
            get_cantidad = cantidad
            return True                 
        elif cantidad < 0:
            print("Tiene que ser un valor superior o igual a cero.")
        else:
            print("La cantidad tiene que ser positiva o nula.")

class Inventario(Producto):
    def __init__(self, nombre=None, categoria=None, precio=0, cantidad=0, inventario=[]):
        super().__init__(nombre, categoria, precio, cantidad)
        self.__producto = [nombre, categoria, precio, cantidad]
        self.__inventario = []                  

    def get_producto(self, producto):
        return self.__producto

    def get_inventario(self, inventario):
        return self.__inventario

    def set_producto(self, producto):
        get_producto = [get_nombre, get_categoria, get_precio, get_cantidad]

    def set_inventario(self, inventario):
        get_inventario = []
    
    def pedirDatos(self):
        while True:
            nombre = input("Introduzca nombre del producto: ").strip().lower()
            while self.comprobarNombre(nombre):                 # la función comprobarNombre() se encuentra más abajo
                nombre = input("Introduzca nombre del producto: ").strip().lower()
            if self.set_nombre(nombre): # comprobamos validez del input en la clase Producto
                break
        categoria = input("Introduzca categoría: ").strip().lower()
        self.set_categoria(categoria)
        # Excepción ValueError para que no se pare el programa en este punto en caso de no introducir un tipo "float"
        while True:                         
            try:
                precio = float(input("Introduzca precio: ").strip())
                if self.set_precio(precio): # comprobamos validez del input en la clase Producto
                    break
            except ValueError:
                print("Tiene que introducir un número.")
        # Excepción ValueError para que no se pare el programa en este punto en caso de no introducir un tipo "int"
        while True:
            try:
                cantidad = int(input("Introduzca cantidad: ").strip())
                if self.set_cantidad(cantidad): # comprobamos validez del input en la clase Producto
                    break
            except ValueError:
                print("Tiene que introducir un número (sin decimales).")
        self.get_producto = [nombre, categoria, precio, cantidad]

    def comprobarNombre(self, nombre):          # Se utiliza en la función pedirDatos() más arriba
        for producto in inventario:
            while nombre in producto[0]:
                print("El nombre de producto introducido ya existe. Por favor, elija otro nombre.")
                return True                     # Vuelve a preguntar mientras sea True

    def agregarProducto(self):
        inventario.append(self.get_producto)
        print (f"\n===== Producto agregado =====\nNombre: {self.get_producto[0]}  Categoría: {self.get_producto[1]}  Precio: {self.get_producto[2]}  Cantidad: {self.get_producto[3]}  ")
        return inventario

    def buscarProducto(self):
        if inventario == []:
            print('El inventario está vacío.\nPuede añadir un producto con la opción "1. Agregar Producto" a continuación:')
        else:
            busca = input("Introduzca el nombre del producto a buscar: ").lower()
            for self.get_producto in inventario:
                if busca in self.get_producto[0]:
                    print (f"\nNombre: {self.get_producto[0]}  Categoría: {self.get_producto[1]}  Precio: {self.get_producto[2]}  Cantidad: {self.get_producto[3]}  ")
                    break
            if busca not in self.get_producto[0]:
                print("No hay ningún producto con ese nombre.")

    def actualizarProducto(self):
        if inventario == []:
            print('No hay ningún producto en el inventario.\nPuede añadir un producto con la opción "1. Agregar Producto" a continuación:')
        else:
            busca = input("\nIntroduzca el nombre del producto a actualizar: ").lower()
            for producto in inventario:
                if busca in producto[0]:
                    print(f"\n===== Producto a actualizar =====\nNombre: {producto[0]}  Categoría: {producto[1]}  Precio: {producto[2]}  Cantidad: {producto[3]}\n")
                    # Reutilizamos las mismas comprobaciones que cuando agregamos un producto
                    while True:
                        try:
                            precioNuevo = float(input("Introduzca precio: ").strip())
                            if self.set_precio(precioNuevo): # comprobamos validez del input en la clase Producto
                                break
                        except ValueError:
                            print("Tiene que introducir un número.")
                    # Reutilizamos las mismas comprobaciones que cuando agregamos un producto
                    while True:
                        try:
                            cantidadNuevo = int(input("Introduzca cantidad: ").strip())
                            if self.set_cantidad(cantidadNuevo): # comprobamos validez del input en la clase Producto
                                break
                        except ValueError:
                            print("Tiene que introducir un número (sin decimales).")
                    producto[2] = precioNuevo
                    producto[3] = cantidadNuevo
                    print(f"\n===== Producto actualizado =====\nNombre: {producto[0]}  Categoría: {producto[1]}  Precio: {producto[2]}  Cantidad: {producto[3]}")
                    break
            if busca not in producto[0]:
                print("No hay ningún producto con ese nombre.")

    def borrarProducto():
        if inventario == []:
            print('No hay ningún producto en el inventario.\nPuede añadir un producto con la opción "1. Agregar Producto" a continuación:')
        else:
            busca = input("Introduzca el nombre del producto a suprimir: ").lower()
            for i, producto in enumerate(inventario):
                if busca in producto[0]:
                    print(f"El producto {producto[0]} ha sido eliminado.")
                    # Eliminamos el producto i del inventario en la iteración i, que es cuando encuentra "busca"
                    inventario.pop(i)
                    break
            if busca not in producto[0]:
                print("No hay ningún producto con ese nombre.")

    def mostrarInventario():
        if inventario == []:
            print("El inventario está vacío")
        else:
            print("\n===== Inventario =====")
            for producto in inventario:
                print(f"Nombre: {producto[0]}  Categoría: {producto[1]}  Precio: {producto[2]}  Cantidad: {producto[3]}")

    def menuInicio():
        producto1 = Inventario()
        while True:
            print("\n--- Indique la opción deseada seleccionando el número correspondiente ---")
            print("1. Agregar Producto")
            print("2. Actualizar Producto")
            print("3. Eliminar Producto")
            print("4. Mostrar Inventario")
            print("5. Buscar Producto")
            print("0. Salir")
            print("\n")

            opcion = (input("Seleccione una opción: "))
            if   opcion == '1':
                producto1.pedirDatos()
                producto1.agregarProducto()
            elif opcion == '2':
                producto1.actualizarProducto()
            elif opcion == '3':
                Inventario.borrarProducto()
            elif opcion == '4':
                Inventario.mostrarInventario()
            elif opcion == '5':
                producto1.buscarProducto()
            elif opcion == '0':
                break
            else:
                print("Introduzca una opción válida (del 0 al 5).")

# He intentado incluir la variable "inventario" en las clases pero no me ha funcionado 
inventario = []
Inventario.menuInicio()