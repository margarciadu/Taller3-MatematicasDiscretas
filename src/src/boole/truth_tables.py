import itertools

"""
Generador y evaluador manual de tablas de verdad para circuitos booleanos de 4 variables.
"""

def truth_table(func) -> tuple:
    # 1. Definimos las columnas de entrada para las 4 variables booleanas
    cols = ['A', 'B', 'C', 'D']
    rows = []

    # 2. Generamos manualmente las 16 combinaciones posibles (2^4) usando itertools
    for a, b, c, d in itertools.product([True, False], repeat=4):
        # Evaluamos la funcion logica pasada como argumento
        out = func(a, b, c, d)
        rows.append((a, b, c, d, out))

    return cols, rows


# 3. Expresiones booleanas definidas mediante funciones lambda
expr1 = lambda a, b, c, d: (a and b) or (not c)
expr2 = lambda a, b, c, d: (a ^ b) and c
expr3 = lambda a, b, c, d: (a or b) and ((not a) or c)


# Ejemplo de Ejecucion 
if __name__ == "__main__":
    cols, data = truth_table(expr1)
    
    print("Tabla de Verdad para: (A AND B) OR (NOT C)")
    print(f"{'A':<6} {'B':<6} {'C':<6} {'D':<6} | {'Salida'}")
    print("-" * 35)
    for row in data:
        a, b, c, d, res = row
        print(f"{str(a):<6} {str(b):<6} {str(c):<6} {str(d):<6} | {str(res)}")
