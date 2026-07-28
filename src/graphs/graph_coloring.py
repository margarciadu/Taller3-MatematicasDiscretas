"""
Coloreo voraz de grafos para la programacion de horarios de examenes libres de cruces
"""

def color_graph(graph: dict) -> tuple:
    colors = {}

    # Asignamos el menor color disponible a cada nodo
    for node in graph:
        # Consultamos que colores ya tienen los cursos 
        used_colors = {
            colors[neighbor]
            for neighbor in graph[node]
            if neighbor in colors
        }

        # Buscamos el color disponible con el menor indice
        color = 0
        while color in used_colors:
            color += 1

        colors[node] = color

    # Agrupamos los nodos por su franja horaria (color)
    num_colors = max(colors.values()) + 1 if colors else 0
    slots = {c: [] for c in range(num_colors)}

    for node, color in colors.items():
        slots[color].append(node)

    # Verificacion de validez de la asignacion de colores
    is_valid = True
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if colors[node] == colors[neighbor]:
                is_valid = False
                break

    return num_colors, slots, is_valid


# --- Grafo con 10 Cursos (Vertices) ---
academic_graph = {
    'DiscreteMath': ['Calculus1', 'Physics1', 'LinearAlgebra'],
    'Calculus1': ['DiscreteMath', 'Chemistry1'],
    'Physics1': ['DiscreteMath', 'Chemistry1', 'Programming1'],
    'LinearAlgebra': ['DiscreteMath', 'Statistics1'],
    'Programming1': ['Physics1', 'Databases1'],
    'Chemistry1': ['Calculus1', 'Physics1'],
    'Statistics1': ['LinearAlgebra', 'Ethics'],
    'Databases1': ['Programming1', 'OperatingSystems'],
    'Ethics': ['Statistics1'],
    'OperatingSystems': ['Databases1']
}

if __name__ == "__main__":
    total_slots, schedules, is_valid = color_graph(academic_graph)
    print(f"Franjas horarias necesarias: {total_slots}")
    print(f"Asignacion valida sin cruces: {is_valid}")
    for slot_num, courses in schedules.items():
        print(f"  Franja {slot_num + 1}: {', '.join(courses)}")
