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

def dijkstra(grafo, origen):
    distancias = {}
    anteriores = {}
    visitados = {}
    
    for ciudad in grafo:
        distancias[ciudad] = float('inf')
        anteriores[ciudad] = None
        visitados[ciudad] = False
        
    distancias[origen] = 0
    
    total_ciudades = len(grafo)
    contador_visitados = 0
    
    while contador_visitados < total_ciudades:
        ciudad_actual = None
        menor_distancia = float('inf')
        
        for ciudad in grafo:
            if not visitados[ciudad] and distancias[ciudad] < menor_distancia:
                menor_distancia = distancias[ciudad]
                ciudad_actual = ciudad
        
        if ciudad_actual is None:
            break
        
        visitados[ciudad_actual] = True
        contador_visitados += 1
        
        for vecino, peso in grafo[ciudad_actual]:
            if visitados[vecino]:
                continue
            
            nueva_distancia = distancias[ciudad_actual] + peso
            
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = ciudad_actual
    
    return distancias, anteriores
