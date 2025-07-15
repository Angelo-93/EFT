#Debes utilizar dos diccionarios:
#'juguetes': donde cada clave es el código del producto y su valor es una lista con [nombre, marca, edad recomendada, tipo].
#- 'inventario': donde cada clave es el código y su valor es una lista con [precio, cantidad en stock].

#Diccionario juguetes
juguetes = {
    "A001": ["alien","nova", "8", "muñeco"],
    "N002": ["nave","star","9","vehiculo"],
    "R003": ["rover","petalien","20","robot"]
}
#Diccionario inventario
inventario = {
    "A001" : [100000, 10],
    "N002" : [80000, 5],
    "R003" : [15000, 3]
}

#  1. Consultar stock por tipo de juguete (Ej: Muñeca, Vehículo, etc.)
def stock_tipo(jueguetes, inventario):
    tipo_buscado = input("ingrese tipo de juguete que deseas buscar: ").strip().lower()
    encontrado = False

    for codigo, datos in juguetes.items():
        nombre = datos[0]
        