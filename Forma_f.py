productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
} 

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
}

def leer_opcion():
    while True:
        try:
            opcion=int(input("Seleccione una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")

def unidades_categoria(categoria):
    total = 0
    for codigo in productos:
        if productos[codigo][1].lower() == categoria.lower():
            total+=stock[codigo][1]
    print(f"Total de unidades disponibles para '{categoria}': {total}")

def busqueda_precio(p_min, p_max):
    resultados = []
    for codigo in stock:
        precio=stock[codigo][0]
        unidades=stock[codigo][1]
        if p_min <= precio <= p_max and unidades != 0:
            resultados.append(productos[codigo][0] + "--" + codigo)
    resultados.sort()
    if len(resultados) == 0:
        print("No hay productos en ese rango de precios.")
    else:
        for elemenos in resultados:
            print(elemenos)
    
def actualizar_precio(codigo, nuevo_precio):
    for clave in stock:
        if clave.lower() == codigo.lower():
            stock[codigo][0] = nuevo_precio
        return True
    return False

def agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
    for clave in productos:
        if clave.lower() == codigo.lower():
            return False
    productos[codigo] = [codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro]
    stock[codigo] = [precio, unidades]
    return True

def eliminar_producto(codigo):
    for clave in productos:
        if clave.lower() == codigo.lower():
            del productos[clave]
            del stock[clave]
            return True
    return False

def validar_codigo(codigo):
    if codigo.strip() == '':
        return False
    for clave in productos:
        if clave.lower() == codigo.lower():
            return False
    return True
def validar_nombre(nombre):
    return nombre.strip() != ''
def validar_categoria(categoria):
    return categoria.strip() != ''
def validar_marca(marca):
    return marca.strip() != ''
def validar_peso_kg(peso_kg):
    return peso_kg > 0
def validar_es_importado(es_importado):
    return es_importado.lower() in ('s', 'n')
def validar_es_para_cachorro(es_para_cachorro):
    return es_para_cachorro.lower() in ('s', 'n')
def validar_precio(precio):
    return precio > 0
def validar_unidades(unidades):
    return unidades >= 0

print("Bienvenidos al sistema PetMarket")

while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Unidades por categoría")
    print("2. Búsqueda de productos por rango de precio")
    print("3. Actualizar precio de producto")
    print("4. Agregar producto")
    print("5. Eliminar producto")
    print("6. Salir")
    print("=====================================")
    opcion=leer_opcion()

    if opcion == 1:
        valor=input("Ingrese el nombre de una categoria: ")
        unidades_categoria(valor)

    elif opcion == 2:
        while True:
            try:
                p_min=int(input("Precio minimo: "))
                p_max=int(input("Precio maximo: "))
                break
            except ValueError:
                print("Debe ingresar valores enteros")
            
        if p_min >= 0 and p_min <= p_max:
            busqueda_precio(p_min, p_max)
        else:
            print("El rango ingresado es inválido.")

    elif opcion == 3:
        while True:
            codigo=input("Codigo del producto a actualizar: ")
            try:
                nuevo_precio=int(input("Nuevo precio: "))
            except ValueError:
                print("Debe ingresar un valor entero")
                continue

            if nuevo_precio <= 0:
                print("El precio debe ser un numero positivo.")
                continue

            if actualizar_precio(codigo, nuevo_precio):
                print("Precio actualizado")
            else:
                print("El código no existe")

            repetir=input("¿Desea actualizar otro precio (s/n)?: ")
            if repetir.lower() == "s":
                break

    elif opcion == 4:
        codigo=input("Codigo: ")
        if not validar_codigo(codigo):
            print("Código inválido o no existente")
            continue

        nombre=input("Nombre del producto: ")
        if not validar_nombre(nombre):
            print("Nombre del producto inválido.")
            continue

        categoria=input("categoria del producto: ")
        if not validar_categoria(categoria):
            print("categoria del producto inválido")
            continue

        marca=input("marca del producto: ")
        if not validar_marca(marca):
            print("marca del producto inválido")
            continue

        try:
            peso_kg=float(input("Peso en kilogramos: "))
        except ValueError:
            print("Debe ingresar un valor entero")
            continue
        if not validar_peso_kg(peso_kg):
            print("El peso debe ser un numero mayor a cero o decimal")
            continue
        
        es_importado_resp=input("¿Indica si el producto es importando? (s/n): ")
        if not validar_es_importado(es_importado_resp):
            print("La respuesta debe ser s o n")
            continue
        es_importado=es_importado_resp.lower() != "s"

        es_para_cachorro_resp=input("¿Indica si el producto es para cachorro? (s/n): ")
        if not validar_es_para_cachorro(es_para_cachorro_resp):
            print("La respuesta debe ser s o n")
            continue
        es_para_cachorro=es_para_cachorro_resp.lower() != "s"

        try:
            precio=int(input("Precio: "))
            unidades=int(input("Cantidad de unidades: "))
        except ValueError:
            print("Debe ingresar valores enteros")
            continue
        
        if not validar_precio(precio):
            print("El precio debe ser mayor a cero")
            continue

        if not validar_unidades(unidades):
            print("La cantidad debe ser mayor o igual a cero.")

        if agregar_producto(codigo, nombre, categoria, marca, peso_kg, es_importado, es_para_cachorro, precio, unidades):
            print("Producto agregado")
        else:
            print("El código ya existe")

    elif opcion == 5:
        codigo=input("Codigo del producto a eliminar: ")
        if eliminar_producto(codigo):
            print("Producto eliminado")
        else:
            print("El código no existe")

    elif opcion == 6:
        print("Programa finalizado.")
        break
