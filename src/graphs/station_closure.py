from copy import deepcopy
from dijkstra import dijkstra, graph as city_graph

"""
Analizador de impacto en redes de transporte tras la clausura de un nodo o estacion.
"""

def simulate_closure(graph: dict, closed_node: str, routes: list) -> list:
    # Copiamos el grafo para aislar los cambios de la red original
    disrupted_graph = deepcopy(graph)

    # Eliminamos el nodo clausurado y todas sus conexiones
    if closed_node in disrupted_graph:
        del disrupted_graph[closed_node]
        for node in disrupted_graph:
            if closed_node in disrupted_graph[node]:
                del disrupted_graph[node][closed_node]

    results = []

    # Evaluamos el impacto del cierre para cada par origen-destino
    for start, target in routes:
        dist_before, _ = dijkstra(graph, start, target)
        dist_after, _ = dijkstra(disrupted_graph, start, target)

        if dist_after == float('inf'):
            status = "DESCONECTADO"
            diff = "N/A"
        elif dist_after > dist_before:
            status = "AUMENTO DISTANCIA"
            diff = dist_after - dist_before
        else:
            status = "SIN CAMBIOS"
            diff = 0

        results.append({
            "origin": start,
            "destination": target,
            "dist_before": dist_before,
            "dist_after": dist_after,
            "diff": diff,
            "status": status
        })

    return results


# Pruebas con 5 pares
if __name__ == "__main__":
    test_routes = [
        ('Portal', 'Universidad'),
        ('Calle26', 'Terminal'),
        ('Bosa', 'Suba'),
        ('Museo', 'Terminal'),
        ('Portal', 'Centro')
    ]
    
    closed_node = 'Centro'
    results = simulate_closure(city_graph, closed_node, test_routes)

    print(f"*** IMPACTO TRAS CERRAR LA ESTACION: {closed_node} ***")
    print(f"{'Origen':<12} {'Destino':<12} {'Antes':<8} {'Despues':<8} {'Diferencia':<12} {'Estado'}")
    print("-" * 65)
    for row in results:
        print(f"{row['origin']:<12} {row['destination']:<12} {row['dist_before']:<8} {row['dist_after']:<8} {str(row['diff']):<12} {row['status']}")
