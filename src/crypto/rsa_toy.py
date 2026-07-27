"""
Modulo RSA de Juguete
"""

def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    Algoritmo de Euclides Extendido.
    Calcula el MCD de (a, b) y los coeficientes de Bézout x, y tales que:
    a * x + b * y = gcd
    """
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    
    return gcd, x, y


def mod_inverse(e: int, phi: int) -> int:
    """
    Calcula el inverso modular d tal que (e * d) = 1 (mod phi).
    Lanza un error si e y phi no son coprimos.
    """
    gcd, x, _ = extended_gcd(e, phi)
    
    if gcd != 1:
        raise ValueError(
            f"El exponente e={e} no es válido porque gcd(e, phi(n)) = {gcd} != 1"
        )
        
    # Ajustamos el coeficiente para asegurar un resultado positivo módulo phi(n)
    return (x % phi + phi) % phi


def generate_rsa_keys(p: int, q: int, e: int) -> tuple[int, int, int]:
    """
    Calcula n, phi(n) y el exponente privado d dados dos números primos p, q y e.
    """
    n = p * q
    phi = (p - 1) * (q - 1)
    d = mod_inverse(e, phi)
    
    return n, phi, d


def encrypt_rsa(message: int, e: int, n: int) -> int:
    """
    Cifra un entero M: C = M^e (mod n)
    """
    return pow(message, e, n)


def decrypt_rsa(c: int, d: int, n: int) -> int:
    """
    Descifra un entero C: M = C^d (mod n)
    """
    return pow(c, d, n)


# --- Ejemplo con el caso obligatorio de la guía ---
if __name__ == "__main__":
    p, q, e, msg = 61, 53, 17, 65
    
    n, phi, d = generate_rsa_keys(p, q, e)
    encrypted_msg = encrypt_rsa(msg, e, n)
    decrypted_msg = decrypt_rsa(encrypted_msg, d, n)
    
    print(f"n      = {n}")          # Esperado: 3233
    print(f"phi(n) = {phi}")         # Esperado: 3120
    print(f"d      = {d}")          # Esperado: 2753
    print(f"C      = {encrypted_msg}")   # Esperado: 2790
    print(f"M      = {decrypted_msg}")   # Esperado: 65
