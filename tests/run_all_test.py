import sys
import os

# Agregamos el directorio raiz del proyecto al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importacion de los 10 modulos del proyecto
# (Los nombres importados coinciden EXACTAMENTE con los definidos en src/)
from src.crypto.caesar import encrypt_caesar, decrypt_caesar
from src.crypto.rsa_toy import generate_rsa_keys, encrypt_rsa, decrypt_rsa
from src.crypto.mpc_sum import mpc_average
from src.graphs.dijkstra import dijkstra, graph as sample_city_network
from src.graphs.station_closure import simulate_closure
from src.graphs.graph_coloring import color_graph, academic_graph as sample_academic_conflicts
from src.boole.truth_tables import truth_table, expr1 as expression_one
from src.boole.boolean_minimizer import simplify_minterms, verify_equivalence
from src.quantum.shannon_entropy import shannon_entropy
from src.quantum.qubit_simulator import QubitSimulator


def run_crypto_tests():
    print("*** [Bloque A: Criptografia] ***")

    # Punto 1: Cesar
    c_text = encrypt_caesar("HOLA UNAL", 3)
    p_text = decrypt_caesar(c_text, 3)
    assert c_text == "KROD XQDO"
    assert p_text == "HOLA UNAL"
    print("Punto 1 (Cifrado Cesar): Funciona correctamente.")

    # Punto 2: RSA
    n, phi, d = generate_rsa_keys(61, 53, 17)
    c_rsa = encrypt_rsa(65, 17, n)
    m_rsa = decrypt_rsa(c_rsa, d, n)
    assert n == 3233
    assert phi == 3120
    assert d == 2753
    assert c_rsa == 2790
    assert m_rsa == 65
    print("Punto 2 (RSA de Juguete): Verificado con caso de prueba obligatorio.")

    # Punto 3: MPC
    total_sum, average_val = mpc_average([40, 35, 50, 25])
    assert total_sum == 150
    assert average_val == 37.5
    print("Punto 3 (MPC Suma Secreta): Suma y promedio reconstruidos con exito.")


def run_graph_tests():
    print("\n*** [Bloque B: Grafos] ***")

    # Punto 4: Dijkstra
    cost, route = dijkstra(sample_city_network, 'Portal', 'Universidad')
    assert cost > 0
    assert len(route) >= 2
    print(f"Punto 4 (Dijkstra): Ruta hallada con costo {cost}.")

    # Punto 5: Cierre de Estacion
    test_routes = [('Portal', 'Universidad'), ('Calle26', 'Terminal')]
    impact_results = simulate_closure(sample_city_network, 'Centro', test_routes)
    assert len(impact_results) == 2
    print("Punto 5 (Impacto de Cierre): Analisis de red ejecutado correctamente.")

    # Punto 6: Coloreo de Grafos
    total_slots, _, is_valid = color_graph(sample_academic_conflicts)
    assert is_valid is True
    assert total_slots > 0
    print(f"Punto 6 (Coloreo Voraz): Asignacion valida usando {total_slots} franjas.")


def run_boole_and_quantum_tests():
    print("\n***[Bloque C: Boole, Shannon y Cuantica] ***")

    # Punto 7: Tablas de Verdad
    _, rows = truth_table(expression_one)
    assert len(rows) == 16
    print("Punto 7 (Tablas de Verdad): Evaluacion de 16 combinaciones correcta.")

    # Punto 8: Simplificacion Booleana
    target_minterms = {1, 3, 5, 7}
    simplified_expr = simplify_minterms(target_minterms)
    is_equivalent = verify_equivalence(target_minterms, simplified_expr)
    assert is_equivalent is True
    print(f"Punto 8 (Simplificacion Booleana): Expresion '{simplified_expr}' verificada.")

    # Punto 9: Entropia de Shannon
    entropy_rep, _ = shannon_entropy("AAAAAAABBBBBB")
    entropy_var, _ = shannon_entropy("El lenguaje de las matematicas discretas.")
    assert entropy_var > entropy_rep
    print(f"Punto 9 (Entropia de Shannon): {entropy_var:.2f} bits vs {entropy_rep:.2f} bits.")

    # Punto 10: Simulador Cuantico
    simulator = QubitSimulator()
    simulator.apply_h()
    measurements = simulator.measure(1000)
    assert "|0>" in measurements and "|1>" in measurements
    print("Punto 10 (Simulador Cuantico): Superposicion H|0> verificada con 1000 disparos.")


def main():
    print("==================================================")
    print("   EJECUTANDO PRUEBAS PARA EL TALLER 3  ")
    print("==================================================\n")

    try:
        run_crypto_tests()
        run_graph_tests()
        run_boole_and_quantum_tests()
        print("\n==================================================")
        print("  TODAS LAS PRUEBAS FUNCIONARON CORRECTAMENTE")
        print("==================================================")
    except AssertionError as error:
        print(f"\nError de asercion detectado durante la prueba: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"\nOcurrio un error inesperado: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
