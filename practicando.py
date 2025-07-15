# =======================
# Diccionarios iniciales
# =======================
juguetes = {
    "A001": ["alien", "nova", "8", "muñeco"],
    "N002": ["nave", "star", "9", "vehiculo"],
    "R003": ["rover", "petalien", "20", "robot"]
}

inventario = {
    "A001": [100000, 10],
    "N002": [80000, 5],
    "R003": [15000, 3]
}

# =======================
# FUNCIONES DEL MENÚ
# =======================

# 1. Consultar stock por tipo
def consultar_stock_por_tipo():
    tipo_buscado = input("Ingrese el tipo de juguete: ").strip().lower()
    encontrado = False

    for codigo in juguetes:
        tipo = juguetes[codigo][3].lower()
        nombre = juguetes[codigo][0]
        stock = inventario[codigo][1]
        if tipo == tipo_buscado:
            print(f"{nombre} (Código: {codigo}) - Stock: {stock}")
            encontrado = True

    if not encontrado:
        print("No se encontraron juguetes de ese tipo.")

# 2. Buscar productos por rango de precio
def buscar_por_precio():
    try:
        minimo = int(input("Ingrese precio mínimo: "))
        maximo = int(input("Ingrese precio máximo: "))
        encontrados = False

        for codigo in inventario:
            precio = inventario[codigo][0]
            if minimo <= precio <= maximo:
                nombre = juguetes[codigo][0]
                print(f"{nombre} (Código: {codigo}) - Precio: {precio}")
                encontrados = True

        if not encontrados:
            print("No se encontraron productos en ese rango.")
    except:
        print("Debes ingresar precios válidos.")

# 3. Actualizar precio por código
def actualizar_precio():
    codigo = input("Ingrese código del producto: ").strip().upper()
    if codigo in inventario:
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            inventario[codigo][0] = nuevo_precio
            print("Precio actualizado correctamente.")
        except:
            print("Precio inválido.")
    else:
        print("Código no encontrado.")

# 4. Agregar nuevo producto
def agregar_producto():
    codigo = input("Ingrese nuevo código: ").strip().upper()
    if codigo in juguetes:
        print("Ese código ya existe.")
        return

    nombre = input("Nombre del juguete: ")
    marca = input("Marca: ")
    edad = input("Edad recomendada: ")
    tipo = input("Tipo: ")
    try:
        precio = int(input("Precio: "))
        stock = int(input("Stock disponible: "))
    except:
        print("Precio o stock inválido.")
        return

    juguetes[codigo] = [nombre, marca, edad, tipo]
    inventario[codigo] = [precio, stock]
    print("Producto agregado exitosamente.")

# 5. Eliminar producto por código
def eliminar_producto():
    codigo = input("Código del producto a eliminar: ").strip().upper()
    if codigo in juguetes:
        del juguetes[codigo]
        del inventario[codigo]
        print("Producto eliminado.")
    else:
        print("Código no encontrado.")

# 6. Ver todos los productos
def ver_todos():
    print("\nLista de productos:")
    for codigo in juguetes:
        nombre, marca, edad, tipo = juguetes[codigo]
        precio, stock = inventario[codigo]
        print(f"{codigo}: {nombre}, {marca}, Edad: {edad}, Tipo: {tipo}, Precio: {precio}, Stock: {stock}")

# 7. Buscar producto por código
def buscar_por_codigo():
    codigo = input("Ingrese código a buscar: ").strip().upper()
    if codigo in juguetes:
        nombre, marca, edad, tipo = juguetes[codigo]
        precio, stock = inventario[codigo]
        print(f"{codigo}: {nombre}, {marca}, Edad: {edad}, Tipo: {tipo}, Precio: {precio}, Stock: {stock}")
    else:
        print("Producto no encontrado.")

# =======================
# MENÚ PRINCIPAL
# =======================
while True:
    print("\nMENÚ PRINCIPAL TOYWORLD")
    print("1. Consultar stock por tipo de juguete")
    print("2. Buscar productos por rango de precio")
    print("3. Actualizar precio de un producto")
    print("4. Agregar nuevo producto")
    print("5. Eliminar producto")
    print("6. Ver todos los productos")
    print("7. Buscar producto por código")
    print("8. Salir")

    opcion = input("Selecciona una opción (1-8): ")

    if opcion == "1":
        consultar_stock_por_tipo()
    elif opcion == "2":
        buscar_por_precio()
    elif opcion == "3":
        actualizar_precio()
    elif opcion == "4":
        agregar_producto()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        ver_todos()
    elif opcion == "7":
        buscar_por_codigo()
    elif opcion == "8":
        print("¡Gracias por usar ToyWorld!")
        break
    else:
        print("Opción inválida. Intenta nuevamente.")
