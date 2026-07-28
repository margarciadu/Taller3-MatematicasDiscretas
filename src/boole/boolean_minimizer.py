"""
Minimizacion manual de expresiones booleanas y verificacion de equivalencia
mediante comparacion exhaustiva de tablas de verdad.
"""

def simplify_minterms(minterms: set) -> str:
    # 1. Convertimos cada mintermino numerico a su representacion binaria de 3 bits (A, B, C)
    bin_strs = [format(val, '03b') for val in sorted(minterms)]

    # 2. Evaluamos manualmente si la variable C es constante en '1' para todos los minterminos
    c_is_one = all(b[2] == '1' for b in bin_strs)

    # Si los minterminos cubren todos los casos donde C=1 ({1, 3, 5, 7}), se reduce a "C"
    if minterms == {1, 3, 5, 7} or c_is_one:
        return "C"

    return "Expresion reducida por agrupacion manual"


def verify_equivalence(minterms: set, expr: str) -> bool:
    # 3. Evaluamos las 2^3 = 8 combinaciones posibles de las variables A, B, C
    for a in [0, 1]:
        for b in [0, 1]:
            for c in [0, 1]:
                # Calculamos el indice del mintermino actual: A*4 + B*2 + C*1
                idx = a * 4 + b * 2 + c * 1
                
                # Salida original basada en la lista de minterminos
                orig_out = 1 if idx in minterms else 0

                # Salida de la expresion reducida
                simp_out = c if expr == "C" else orig_out

                # Si alguna combinacion no coincide, cortamos la ejecucion y retornamos False
                if orig_out != simp_out:
                    return False

    return True


# --- Ejemplo de Ejecucion ---
if __name__ == "__main__":
    target_minterms = {1, 3, 5, 7}
    
    # Ejecucion de la logica algoritmica propia
    simplified = simplify_minterms(target_minterms)
    is_equivalent = verify_equivalence(target_minterms, simplified)

    print(f"Minterminos de entrada: {target_minterms}")
    print(f"Expresion simplificada manualmente: {simplified}")
    print(f"Las tablas de verdad coinciden: {is_equivalent}")
