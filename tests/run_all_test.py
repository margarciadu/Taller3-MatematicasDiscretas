import sys
import os

# Agregamos el directorio raíz del proyecto al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importación de los 10 módulos del proyecto
from src.crypto.caesar import encrypt_caesar, decrypt_caesar
from src.crypto.rsa_toy import generate_rsa_keypair, encrypt_rsa_value, decrypt_rsa_value
from src.crypto.mpc_sum import run_mpc_average_protocol
from src.graphs.dijkstra import find_shortest_path_dijkstra, sample_city_network
from src.graphs.station_closure import simulate_station_closure
from src.graphs.graph_coloring import schedule_exam_timeslots, sample_academic_conflicts
from src.boole.truth_tables import generate_boolean_truth_table, expression_one
from src.boole.boolean_minimizer import simplify_three_var_minterms, verify_boolean_equivalence
from src.quantum.shannon_entropy import compute_shannon_entropy
from src.quantum.qubit_simulator import SingleQubitSimulator


def run_crypto_tests():
    print("*** [Bloque A: Criptografía] ***")
    
    # Punto 1: César
    c_text = encrypt_caesar("HOLA UNAL", 3)
    p_text = decrypt_caesar(c_text, 3)
    assert c_text == "KROD XQDO"
    assert p_text == "HOLA UNAL"
    print("Punto 1 (Cifrado César): Funciona correctamente.")

    # Punto 2: RSA
    rsa_keys = generate_rsa_keypair(61, 53, 17)
    c_rsa = encrypt_rsa_value(65, 17, rsa_keys["modulus_n"])
    m_rsa = decrypt_rsa_value(c_rsa, rsa_keys["private_exponent_d"], rsa_keys["modulus_n"])
    assert rsa_keys["modulus_n"] == 3233
    assert rsa_keys["totient_phi"] == 3120
    assert rsa_keys["private_exponent_d"] == 2753
    assert c_rsa == 2790
    assert m_rsa == 65
    print(" Punto 2 (RSA de Juguete): Verificado con caso de prueba obligatorio.")

    # Punto 3: MPC
    total_sum, average_val = run_mpc_average_protocol([40, 35, 50, 25])
    assert total_sum == 150
    assert average_val == 37.5
    print("Punto 3 (MPC Suma Secreta): Suma y promedio reconstruidos con éxito.")


def run_graph_tests():
    print("\n*** [Bloque B: Grafos] ***")
    
    # Punto 4: Dijkstra
    cost, route = find_shortest_path_dijkstra(sample_city_network, 'Portal', 'Universidad')
    assert cost > 0
    assert len(route) >= 2
    print(f"Punto 4 (Dijkstra): Ruta hallada con costo {cost}.")

    # Punto 5: Cierre de Estación
    test_routes = [('Portal', 'Universidad'), ('Calle26', 'Terminal')]
    impact_results = simulate_station_closure(sample_city_network, 'Centro', test_routes)
    assert len(impact_results) == 2
    print("Punto 5 (Impacto de Cierre): Análisis de red ejecutado correctamente.")

    # Punto 6: Coloreo de Grafos
    total_slots, _, is_valid = schedule_exam_timeslots(sample_academic_conflicts)
    assert is_valid is True
    assert total_slots > 0
    print(f"Punto 6 (Coloreo Voraz): Asignación válida usando {total_slots} franjas.")


def run_boole_and_quantum_tests():
    print("\n***[Bloque C: Boole, Shannon y Cuántica] ***")
    
    # Punto 7: Tablas de Verdad
    _, rows = generate_boolean_truth_table(expression_one)
    assert len(rows) == 16
    print("Punto 7 (Tablas de Verdad): Evaluación de 16 combinaciones correcta.")

    # Punto 8: Simplificación Booleana
    target_minterms = {1, 3, 5, 7}
    simplified_expr = simplify_three_var_minterms(target_minterms)
    is_equivalent = verify_boolean_equivalence(target_minterms, simplified_expr)
    assert is_equivalent is True
    print(f"Punto 8 (Simplificación Booleana): Expresión '{simplified_expr}' verificada.")

    # Punto 9: Entropía de Shannon
    entropy_rep, _ = compute_shannon_entropy("AAAAAAABBBBBB")
    entropy_var, _ = compute_shannon_entropy("El lenguaje de las matemáticas discretas.")
    assert entropy_var > entropy_rep
    print(f"Punto 9 (Entropía de Shannon): {entropy_var:.2f} bits vs {entropy_rep:.2f} bits.")

    # Punto 10: Simulador Cuántico
    simulator = SingleQubitSimulator()
    simulator.apply_hadamard_gate()
    measurements = simulator.measure_state(1000)
    assert "|0>" in measurements and "|1>" in measurements
    print("Punto 10 (Simulador Cuántico): Superposición H|0> verificada con 1000 disparos.")


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
        print(f"\nError de aserción detectado durante la prueba: {error}")
        sys.exit(1)
    except Exception as error:
        print(f"\nOcurrió un error inesperado: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
