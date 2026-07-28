import heapq

"""
Algoritmo de Dijkstra para la busqueda de la ruta mas corta en un grafo ponderado.
"""

def dijkstra(graph: dict, start: str, target: str) -> tuple:
    # Validacion: Si el origen o el destino no existen en el grafo, no hay ruta
    if start not in graph or target not in graph:
        return float('inf'), []

    # 1. Inicializamos todas las distancias en infinito, excepto el origen que es 0
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Diccionario para rastrear el camino de procedencia (nodo_previo -> nodo_actual)
    parents = {}

    # 2. Cola de prioridad (min-heap) que guarda tuplas de la forma: (distancia_acumulada, nodo)
    pq = [(0, start)]

    # 3. Bucle principal de exploracion
    while pq:
        # Extraemos el nodo con la menor distancia acumulada procesada hasta ahora
        curr_dist, curr_node = heapq.heappop(pq)

        # Optimizacion: Si alcanzamos el destino deseado, detenemos la busqueda
        if curr_node == target:
            break

        # Si encontramos una distancia registrada menor a la procesada actual, la descartamos
        if curr_dist > distances[curr_node]:
            continue

        # Evaluamos todas las conexiones (vecinos) del nodo actual
        for neighbor, weight in graph[curr_node].items():
            new_dist = curr_dist + weight

            # Si la nueva ruta hacia el vecino es mas corta que la registrada:
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                parents[neighbor] = curr_node
                heapq.heappush(pq, (new_dist, neighbor))

    # 4. Si la distancia final al destino sigue siendo infinito, no existe un camino accesible
    if distances[target] == float('inf'):
        return float('inf'), []

    # 5. Reconstruccion de la ruta mas corta trazando desde el destino hacia el origen
    path = []
    curr = target

    while curr in parents:
        path.append(curr)
        curr = parents[curr]

    # Anadimos el origen al final y volteamos la lista para mostrarla de Origen -> Destino
    path.append(start)
    path.reverse()

    return distances[target], path


# Definicion del grafo
graph = {
    'Portal': {'Calle26': 4, 'Bosa': 8},
    'Calle26': {'Portal': 4, 'Museo': 3, 'Centro': 6},
    'Museo': {'Calle26': 3, 'Centro': 2, 'Universidad': 5},
    'Centro': {'Calle26': 6, 'Museo': 2, 'Terminal': 7},
    'Universidad': {'Museo': 5, 'Terminal': 1, 'Suba': 4},
    'Bosa': {'Portal': 8, 'Terminal': 9},
    'Terminal': {'Centro': 7, 'Universidad': 1, 'Bosa': 9, 'Suba': 2},
    'Suba': {'Universidad': 4, 'Terminal': 2}
}


# Ejemplo de Ejecucion
if __name__ == "__main__":
    start = 'Portal'
    target = 'Universidad'

    total_cost, optimal_path = dijkstra(graph, start, target)

    print(f"Calculo de Ruta de '{start}' a '{target}'")
    print(f"Costo minimo de viaje: {total_cost}")
    print(f"Ruta a seguir: {' -> '.join(optimal_path)}")
