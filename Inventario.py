
import os
import uuid

#Función para limpiar la pantalla 
def limpiar_pantalla():
    # Si el sistema operativo es Windows, usa 'cls', si no, usa 'clear'
    if os.name == 'nt':
        os.system('cls')  # Comando para Windows
    else:
        os.system('clear')  # Comando para Unix/Linux/macOS


# Generar un UUID único
id_unico = uuid.uuid4()

# Definición de la clase Producto
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.id = uuid.uuid4()  # Asignar un ID único al producto
        self.nombre = nombre  # Nombre del producto, e.g., "manzana"
        self.precio = precio  # Precio del producto, e.g., 0.50 (en dólares)
        self.cantidad = cantidad  # Cantidad disponible en el inventario

    def __str__(self):
        return f"{self.nombre} (ID: {self.id}) - Precio: {self.precio}, Cantidad: {self.cantidad}"
    
# Definir la clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []  # Lista para almacenar productos

    def agregar_producto(self, producto):
        self.productos.append(producto)  # Añadir el producto a la lista

    def mostrar_total_productos(self):
        total = len(self.productos)  # Número total de productos en la lista
        return total

    def mostrar_productos(self):
        n = 0
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                n = n + 1
                print(f"\n{n}.")
                print(producto)

    # Método para devolver la lista de productos
    def lista_productos(self):
        return self.productos
    
    # Método para eliminar un producto por su ID
    def eliminar_producto(self, id_producto):
        # Indicador para saber si se eliminó el producto
        encontrado = False  
        for producto in self.productos:
            if producto.id == id_producto:
                self.productos.remove(producto)
                print(f"Producto {producto.nombre} eliminado del inventario.")
                encontrado = True
                break  # Salir del bucle una vez que se haya eliminado el producto

# Se inicializa el inventario
inventario = Inventario()

#Función para crear un nuevo producto
def prod_nuevo():
    # Solicitar al usuario los detalles del nuevo producto
    producto_nuevo = input("Ingrese el nombre del producto que desea añadir: ")
    while True:
        try:
            precio_producto_nuevo = float(input("Ingrese el precio del producto: "))  # Convertir a float
        except ValueError:
            print("El precio del producto no es un valor válido.")
            print("Inténtelo otra vez:")
            continue
        if isinstance(precio_producto_nuevo, float):
            print("El precio del producto "+ producto_nuevo + f" se ha registrado como:'{precio_producto_nuevo}'.")
            break

    while True:
        try:
            cantidad_producto_nuevo = int(input("Ingrese la cantidad del producto: "))  # Convertir a entero
        except ValueError:
            print(f"La cantidad del producto no es un valor válido.")
            print("Inténtelo otra vez:")
            continue
        if isinstance(cantidad_producto_nuevo, int):
            print("La canidad del producto "+ producto_nuevo + f" se ha registrado como:'{cantidad_producto_nuevo}'.")
            break

    # Crear la instancia del producto con los datos ingresados
    nuevo_producto = Producto(producto_nuevo, precio_producto_nuevo, cantidad_producto_nuevo)

    inventario.agregar_producto(nuevo_producto)

    # Visualizar el producto que ingresó el usuario
    print("Producto añadido:\n")
    print(nuevo_producto)


#Funcion para actualizar productos 
def act_prod():
    #Actualizar producto
    inventario.mostrar_productos()
    productos = inventario.lista_productos()
    while True:
        try:
            posicion_prod = int(input("Ingrese el número del producto que quiere actualizar: "))
        except ValueError:
            print("El número del producto no es un valor válido.")
            print("Inténtelo otra vez:")
            continue 
        if posicion_prod > len(productos):
            print("No hay un producto para este número.")
            print("Inténtelo otra vez:")
            continue
        else:
            print("Producto seleccionado.")
            break
    while True:
        try:
            parametro = int(input("\n1. Cambiar el precio.\n2. Cambiar la cantidad en inventario.\n"))
        except ValueError:
            print("Carácter Inválido.")
            print("Inténtelo otra vez:")
            continue
        if parametro not in [1,2]:
            print("Número Inválido.")
            print("Inténtelo otra vez:")
            continue
        if parametro == 1:
            try: 
                precio_nuevo = int(input("Ingrese el nuevo precio: "))
            except ValueError:
                print("Carácter Inválido.")
                print("Inténtelo otra vez:")
                continue
            else:
                productos[posicion_prod-1].precio = precio_nuevo
                break
        elif parametro == 2:
            try:
                cantidad_nueva = int(input("Ingrese la nueva cantidad: "))
            except ValueError:
                print("Carácter Inválido.")
                print("Inténtelo otra vez:")
                continue
            else:
                productos[posicion_prod-1].cantidad = cantidad_nueva
                break

    print("\nInventario actualizado.")
    inventario.mostrar_productos()

#Funcion para la Interfaz

def interfaz():
    print("Inventario\n")

    print("Menú de Opciones")
    print("1. Ver Inventario")
    print("2. Añadir elemento al inventario")
    print("3. Eliminar un elemento del inventario")
    print("4. Actualizar productos del inventario")
    print("5. Salir\n")
    while True:
        try: 
            menu_opcion = int(input("Seleccione una opción para continuar: "))
        except ValueError:
            print("Carácter Inválido.")
            print("Inténtelo otra vez:")
            continue
        if isinstance(menu_opcion, int):
            return menu_opcion

# Integracion de las funciones para el inventario

InventarioEncendido = True
print("Bienvenido!\n")
while InventarioEncendido:
    limpiar_pantalla()
    eleccion_usuario = interfaz()
    if eleccion_usuario == 1:
        limpiar_pantalla()
        inventario.mostrar_productos()
        
        while True:
            volver = input("Presione 'X' para volver al menú")
            if volver not in ['x','X']:
                print("Letra Invalida.")
                print("Inténtelo otra vez:")
                continue
            else:
                break
    elif eleccion_usuario == 2:
        limpiar_pantalla()
        prod_nuevo()

        while True:
            volver = input("Presione 'X' para volver al menú")
            if volver not in ['x','X']:
                print("Letra Invalida.")
                print("Inténtelo otra vez:")
                continue
            else:
                break
    
    elif eleccion_usuario == 3:
        limpiar_pantalla()
       # Mostrar productos en el inventario
        inventario.mostrar_productos()

        # Pedir al usuario que ingrese el ID del producto a eliminar
        id_eliminar = input("Ingrese el ID del producto que desea eliminar: ")

        try:
    # Convertir el ID ingresado a tipo UUID
            id_eliminar = uuid.UUID(id_eliminar)
            inventario.eliminar_producto(id_eliminar)
        except ValueError:
            print("ID inválido. Asegúrate de ingresar un ID correcto.")

        while True:
            volver = input("Presione 'X' para volver al menú")
            if volver not in ['x','X']:
                print("Letra Invalida.")
                print("Inténtelo otra vez:")
                continue
            else:
                break
    
    elif eleccion_usuario == 4:
        limpiar_pantalla()
        act_prod()

        while True:
            volver = input("Presione 'X' para volver al menú")
            if volver not in ['x','X']:
                print("Letra Invalida.")
                print("Inténtelo otra vez:")
                continue
            else:
                break
    
    elif eleccion_usuario == 5:
        InventarioEncendido = False
        break