# Inventario de Productos

Este es un programa de inventario en Python que permite a cualquier usuario gestionar un inventario de productos, incluyendo agregar, ver, actualizar y eliminar productos.

## Características

- **Agregar Producto**: Permite al usuario crear productos especificando nombre, precio y cantidad.
- **Mostrar Inventario**: Muestra una lista de todos los productos, incluyendo detalles como ID, nombre, precio y cantidad.
- **Actualizar Producto**: Permite modificar el precio o la cantidad de un producto existente en el inventario.
- **Eliminar Producto**: Elimina un producto del inventario basado en su ID único.

## Requisitos

Este programa requiere Python 3 para ejecutarse.

## Estructura del Código

El código está compuesto por las siguientes clases y funciones principales:

1. **Clase `Producto`**: Define cada producto con propiedades como `id`, `nombre`, `precio` y `cantidad`.
2. **Clase `Inventario`**: Administra los productos en una lista. Contiene métodos para agregar, mostrar, actualizar y eliminar productos.
3. **Función `prod_nuevo`**: Permite al usuario crear un nuevo producto ingresando sus detalles.
4. **Función `act_prod`**: Permite actualizar el precio o la cantidad de un producto.
5. **Función `interfaz`**: Proporciona un menú de opciones para que el usuario navegue por las funciones del inventario.
6. **Función `limpiar_pantalla`**: Limpia la pantalla según el sistema operativo.
7. **Bucle Principal**: Ejecuta el programa y permite al usuario interactuar con el inventario hasta que decida salir.

## Cómo Usarlo

1. **Ejecutar el Programa**:
   ```bash
   python inventario.py
2. **Navegar por el Menú**;

1. **Ver Inventario**: Muestra todos los productos en el inventario. Si está vacío, se notificará.
2. **Añadir Producto**: Permite agregar un nuevo producto solicitando nombre, precio y cantidad.
3. **Eliminar Producto**: Solicita el ID del producto a eliminar del inventario.
4. **Actualizar Producto**: Permite cambiar el precio o la cantidad de un producto existente.
5. **Salir**: Finaliza el programa.

## Ejemplo de Uso

A continuación, se describe un ejemplo de cómo se utiliza el programa:

### Añadir un Producto

- El usuario elige la opción 2 y sigue las indicaciones para ingresar el nombre, precio y cantidad.
- El producto se añade al inventario y se muestra la confirmación.

### Actualizar un Producto

- El usuario elige la opción 4, selecciona el producto a modificar y especifica el nuevo precio o cantidad.

### Eliminar un Producto

- El usuario elige la opción 3, ingresa el ID del producto y el sistema elimina dicho producto del inventario.

## Notas Adicionales

- **ID Único**: Cada producto tiene un ID generado automáticamente usando `uuid`, que es necesario para realizar ciertas acciones, como la eliminación.
- **Control de Errores**: El programa cuenta con validaciones para entradas inválidas y muestra mensajes para que el usuario ingrese datos válidos.

## Contribuciones

Las contribuciones son bienvenidas. Puedes mejorar o ampliar la funcionalidad mediante un pull request.

## Licencia

Este proyecto se distribuye bajo la licencia MIT. Ver el archivo `LICENSE` para más detalles.
