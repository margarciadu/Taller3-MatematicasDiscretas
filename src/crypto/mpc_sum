import random

"""
Simulaciones de Computacion Multipartita Segura (MPC)
Calcula la suma y promedio de notas entre tres servidores sin exponer notas individuales
"""

def split_into_shares(score: int, modulus: int = 1000003) -> tuple:
    part1 = random.randint(0, modulus - 1)
    part2 = random.randint(0, modulus - 1)
    
    # La tercera parte se calcula para que la suma tenga logica con la nota original
    part3 = (score - part1 - part2) % modulus
    
    return part1, part2, part3


def mpc_average(scores: list, modulus: int = 1000003) -> tuple:
    s1_parts = []
    s2_parts = []
    s3_parts = []

    # Cada estudiante reparte en secreto sus 3 partes a los 3 servidores
    for current_score in scores:
        part1, part2, part3 = split_into_shares(current_score, modulus)
        s1_parts.append(part1)
        s2_parts.append(part2)
        s3_parts.append(part3)

    # Cada servidor suma sus partes de manera aislada
    s1_sum = sum(s1_parts) % modulus
    s2_sum = sum(s2_parts) % modulus
    s3_sum = sum(s3_parts) % modulus

    
    total_sum = (s1_sum + s2_sum + s3_sum) % modulus
    average = total_sum / len(scores)

    return total_sum, average


# Ejemplo
if __name__ == "__main__":
    scores = [40, 35, 50, 25]
    total_sum, average = mpc_average(scores)
    
    print(f"Notas originales: {scores}")
    print(f"Suma calculada en secreto: {total_sum} (Esperado: 150)")
    print(f"Promedio obtenido: {average} (Esperado: 37.5)")
