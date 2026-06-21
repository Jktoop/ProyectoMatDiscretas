def construir_grafo(ciudades, conexiones):
    grafo = {}

    # crear una entrada vacia para cada ciudad
    for ciudad in ciudades:
        grafo[ciudad] = []

    # agregar cada conexion en ambas direcciones
    for origen, destino, peso in conexiones:
        grafo[origen].append((destino, peso))
        grafo[destino].append((origen, peso))

    return grafo