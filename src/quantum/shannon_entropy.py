import math
from collections import Counter

"""
Calculo manual de la Entropia de Shannon para medir la incertidumbre e informacion en un texto.
"""

def shannon_entropy(text: str) -> tuple:
    # 1. Si el texto esta vacio, la entropia es 0
    if not text:
        return 0.0, {}

    n = len(text)
    
    # 2. Contamos la frecuencia de cada simbolo manualmente con Counter
    counts = Counter(text)
    probs = {}
    entropy = 0.0

    # 3. Calculamos la probabilidad p(x) y aplicamos la formula H(X) = - sum( p(x) * log2(p(x)) )
    for char, freq in counts.items():
        p = freq / n
        probs[char] = p
        entropy -= p * math.log2(p)

    return entropy, probs


# Comparacion 
if __name__ == "__main__":
    text1 = "AAAAAAAABBBBBBBB"
    text2 = "El conocimiento en matematicas discretas transforma el pensamiento."

    entropy1, _ = shannon_entropy(text1)
    entropy2, _ = shannon_entropy(text2)

    print(f"Texto 1 (Repetitivo): '{text1}'")
    print(f"  Entropia calculada: {entropy1:.4f} bits/simbolo")
    
    print(f"\nTexto 2 (Variado): '{text2}'")
    print(f"  Entropia calculada: {entropy2:.4f} bits/simbolo")
