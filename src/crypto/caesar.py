"""
Modulo de Cifrado Cesar.
"""

def encrypt_caesar(original_text: str, shift_key: int) -> str:
    """
    Cifra un texto desplazando cada letra una cantidad fija de posiciones
    Conserva mayúsculas, minúsculas, números, espacios y signos de puntuación.
    """
    #Lista donde se van agregando los caracteres que ya estan cifrados
    encrypted_characters = []
    
    for character in original_text:
        if character.isupper():
            # Procesamos mayúsculas 
            base_ascii = ord('A')
            shifted_code = (ord(character) - base_ascii + shift_key) % 26 + base_ascii
            encrypted_characters.append(chr(shifted_code))
            
        elif character.islower():
            # Procesamos minúsculas
            base_ascii = ord('a')
            shifted_code = (ord(character) - base_ascii + shift_key) % 26 + base_ascii
            encrypted_characters.append(chr(shifted_code))
            
        else:
            # Los números, espacios y símbolos se dejan exactamente igual
            encrypted_characters.append(character)
            
    return "".join(encrypted_characters)


def decrypt_caesar(cipher_text: str, shift_key: int) -> str:
    """
    Descifra el texto aplicando el desplazamiento contrario 
    """
    return encrypt_caesar(cipher_text, -shift_key)


def brute_force_caesar(cipher_text: str) -> dict[int, str]:
    """
    Prueba los 26 desplazamientos posibles para intentar encontrar el mensaje sin conocer k.
    Devuelve un diccionario con cada clave k y su correspondiente texto descifrado.
    """
    decryption_attempts = {}
    for candidate_shift in range(26):
        decryption_attempts[candidate_shift] = decrypt_caesar(cipher_text, candidate_shift)
    return decryption_attempts


# Ejemplo minimo de ejecución manual para probar el archivo solo
if __name__ == "__main__":
    message = "HOLA UNAL"
    key = 3
    
    ciphertext = encrypt_caesar(message, key)
    recovered = decrypt_caesar(ciphertext, key)
    
    print(f"Original:   {message}")
    print(f"Cifrado:    {ciphertext}")  # Esperado: KROD XQDO
    print(f"Descifrado: {recovered}")
