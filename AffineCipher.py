import time

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for i in range(m):
        if (a * i) % m == 1:
            return i
    return None

def affine_encrypt(plaintext, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("The value of 'a' must be coprime with 26.")
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            x = ord(char.lower()) - ord('a')
            enc = (a * x + b) % 26
            enc_char = chr(enc + ord('a'))
            ciphertext += enc_char.upper() if is_upper else enc_char
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse of a does not exist. 'a' must be coprime with 26.")
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            y = ord(char.lower()) - ord('a')
            dec = (a_inv * (y - b)) % 26
            dec_char = chr(dec + ord('a'))
            plaintext += dec_char.upper() if is_upper else dec_char
        else:
            plaintext += char
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    a = int(input("Enter value for a (must be coprime with 26): "))
    b = int(input("Enter value for b: "))
    start_time = time.time()
    encrypted_text = affine_encrypt(plaintext, a, b)
    encryption_time = time.time() - start_time
    print("Encrypted Text:", encrypted_text)
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    start_time = time.time()
    decrypted_text = affine_decrypt(encrypted_text, a, b)
    decryption_time = time.time() - start_time
    print("Decrypted Text:", decrypted_text)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

if __name__ == "__main__":
    main()
