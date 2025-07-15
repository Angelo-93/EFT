# Diccionario principal de productos (juguetes)
# Cada clave es un código único del producto, y su valor es una lista con:
# [nombre, marca, edad recomendada, tipo]
juguetes = {
    'JX100': ['Auto Carrera', 'HotWheels', 6, 'Vehículo'],
    'BL200': ['Bloques Creativos', 'MegaBlocks', 3, 'Construcción'],
    'MU300': ['Muñeca Elsa', 'Disney', 4, 'Muñeca'],
    'DR400': ['Dragón Rojo', 'PlayFun', 7, 'Acción']
}

# Diccionario que almacena el precio y la cantidad en stock de cada producto
# La clave es el mismo código del producto
inventario = {
    'JX100': [8990, 5],
    'BL200': [12990, 0],
    'MU300': [15990, 3],
    'DR400': [17990, 10]
}

# Función que calcula el stock total disponible de un tipo de juguete
def stock_tipo(tipo):
    tipos_disponibles = set([j[3].lower() for j in juguetes.values()])
    if tipo.lower() not in tipos_disponibles:
        print("Tipo no válido. Tipos disponibles:", ', '.join(tipos_disponibles))
        return
    total = 0
    for codigo in juguetes:
        if juguetes[codigo][3].lower() == tipo.lower():
            total += inventario[codigo][1]
    print(f"El stock total para el tipo '{tipo}' es:", total)

# Función que busca productos dentro de un rango de precios
def buscar_precio(p_min, p_max):
    resultados = []
    for codigo in inventario:
        precio, unidades = inventario[codigo]
        if p_min <= precio <= p_max and unidades > 0:
            marca = juguetes[codigo][1]
            nombre = juguetes[codigo][0]
            resultados.append(f"{marca} - {nombre}")
    if resultados:
        print("Juguetes encontrados:", sorted(resultados))
    else:
        print("No hay juguetes en ese rango de precios.")

# Función que actualiza el precio de un producto si existe
def actualizar_precio(codigo, nuevo_precio):
    if codigo in inventario:
        inventario[codigo][0] = nuevo_precio
        return True
    else:
        return False

# Permite agregar un nuevo producto al sistema
def agregar_producto():
    codigo = input("Ingrese código del nuevo juguete: ")
    if codigo in juguetes:
        print("El código ya existe.")
        return
    nombre = input("Ingrese nombre del juguete: ")
    marca = input("Ingrese marca: ")
    edad = int(input("Edad recomendada: "))
    tipo = input("Tipo de juguete: ")
    precio = int(input("Precio: "))
    stock = int(input("Cantidad en stock: "))
    juguetes[codigo] = [nombre, marca, edad, tipo]
    inventario[codigo] = [precio, stock]
    print("Producto agregado exitosamente.")

# Permite eliminar un producto según su código
def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo in juguetes:
        del juguetes[codigo]
        del inventario[codigo]
        print("Producto eliminado.")
    else:
        print("El código no existe.")

# Muestra todos los productos disponibles en el sistema
def mostrar_productos():
    print("Lista de productos:")
    for codigo in juguetes:
        print(f"{codigo}: {juguetes[codigo]}, Precio: {inventario[codigo][0]}, Stock: {inventario[codigo][1]}")

# Permite buscar un producto específico por su código
def buscar_producto():
    codigo = input("Ingrese código del producto a buscar: ")
    if codigo in juguetes:
        print(f"{codigo}: {juguetes[codigo]}, Precio: {inventario[codigo][0]}, Stock: {inventario[codigo][1]}")
    else:
        print("Producto no encontrado.")

# Menú principal del programa
while True:
    print("\n*** MENÚ PRINCIPAL ***")
    print("1. Consultar stock por tipo de juguete")
    print("2. Buscar por rango de precio")
    print("3. Actualizar precio de un juguete")
    print("4. Agregar nuevo producto")
    print("5. Eliminar producto")
    print("6. Ver todos los productos")
    print("7. Buscar producto por código")
    print("8. Salir")
    
    opcion = input("Ingrese opción: ")
    if opcion == "1":
        tipo = input("Ingrese tipo de juguete a consultar: ")
        stock_tipo(tipo)
    elif opcion == "2":
        try:
            p_min = int(input("Ingrese precio mínimo: "))
            p_max = int(input("Ingrese precio máximo: "))
            buscar_precio(p_min, p_max)
        except:
            print("Debe ingresar valores enteros!!")
    elif opcion == "3":
        codigo = input("Ingrese código de juguete a actualizar: ")
        try:
            nuevo_precio = int(input("Ingrese nuevo precio: "))
            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado!!")
            else:
                print("El código ingresado no existe!!")
        except:
            print("Debe ingresar un valor numérico para el precio.")
    elif opcion == "4":
        agregar_producto()
    elif opcion == "5":
        eliminar_producto()
    elif opcion == "6":
        mostrar_productos()
    elif opcion == "7":
        buscar_producto()
    elif opcion == "8":
        print("Programa finalizado.")
        break
    else:
        print("Debe seleccionar una opción válida!!")
