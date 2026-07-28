import math
import random

"""
Simulador manual de un Qubit individual basado en transformaciones de vectores de estado.
Soporta las compuertas cuanticas X, Z y Hadamard (H).
"""

class QubitSimulator:
    def __init__(self):
        # Estado inicial |0> representado por el vector [alpha, beta] = [1.0, 0.0]
        self.state = [1.0, 0.0]

    def apply_x(self):
        # Compuerta X (NOT cuantica): Invierte amplitudes [alpha, beta] -> [beta, alpha]
        alpha, beta = self.state
        self.state = [beta, alpha]

    def apply_z(self):
        # Compuerta Z (Cambio de fase): Cambia el signo de beta [alpha, beta] -> [alpha, -beta]
        alpha, beta = self.state
        self.state = [alpha, -beta]

    def apply_h(self):
        # Compuerta Hadamard (Superposicion): Multiplica por la matriz H = 1/sqrt(2) * [[1, 1], [1, -1]]
        alpha, beta = self.state
        norm = 1.0 / math.sqrt(2)
        new_alpha = norm * (alpha + beta)
        new_beta = norm * (alpha - beta)
        self.state = [new_alpha, new_beta]

    def measure(self, shots: int = 1000) -> dict:
        # 1. Obtenemos las probabilidades segun la Regla de Born: P(0) = |alpha|^2
        alpha, beta = self.state
        p0 = abs(alpha) ** 2
        
        zeros = 0
        ones = 0

        # 2. Simulacion de medicion mediante el metodo de Monte Carlo
        for _ in range(shots):
            if random.random() < p0:
                zeros += 1
            else:
                ones += 1

        return {"|0>": zeros, "|1>": ones}


# Prueba
if __name__ == "__main__":
    print("*CASO 1: Prueba de X|0> = |1>")
    q1 = QubitSimulator()
    q1.apply_x()
    print(f"Resultado tras aplicar X: {q1.measure(1000)}")

    print("\n*CASO 2: Prueba de H|0> (Superposicion ~50/50)")
    q2 = QubitSimulator()
    q2.apply_h()
    print(f"Resultado tras aplicar H: {q2.measure(1000)}")

    print("\n*CASO 3: Prueba de HH|0> = |0>")
    q3 = QubitSimulator()
    q3.apply_h()
    q3.apply_h()
    print(f"Resultado tras aplicar H e inmediatamente H: {q3.measure(1000)}")
