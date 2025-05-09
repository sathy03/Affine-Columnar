import math
import string
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
        raise ValueError("a must be coprime with 26 for the cipher to work.")
    
    ciphertext = ''
    for char in plaintext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            enc = (a * (ord(char) - ord('a')) + b) % 26
            enc_char = chr(enc + ord('a'))
            ciphertext += enc_char.upper() if is_upper else enc_char
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        raise ValueError("Modular inverse of a does not exist.")
    
    plaintext = ''
    for char in ciphertext:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            dec = (a_inv * ((ord(char) - ord('a')) - b)) % 26
            dec_char = chr(dec + ord('a'))
            plaintext += dec_char.upper() if is_upper else dec_char
        else:
            plaintext += char
    return plaintext

def encrypt_columnar_transposition(plaintext, key):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)
    plaintext += ' ' * (num_rows * num_cols - len(plaintext))
    matrix = [list(plaintext[i:i+num_cols]) for i in range(0, len(plaintext), num_cols)]
    ciphertext = ''
    for index, _ in key_order:
        for row in matrix:
            ciphertext += row[index]
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    index = 0
    for col_index, _ in key_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                matrix[row][col_index] = ciphertext[index]
                index += 1
    plaintext = ''.join([''.join(row) for row in matrix]).rstrip()
    return plaintext

def main():
    plaintext = input("Enter the plaintext: ")
    a = int(input("Enter value for a (must be coprime with 26): "))
    b = int(input("Enter value for b: "))
    key = input("Enter the numeric key (example, 3124): ")
    key = [int(digit) for digit in key]
    
    start_time = time.time()
    affine_encrypted = affine_encrypt(plaintext, a, b)
    transposition_encrypted = encrypt_columnar_transposition(affine_encrypted, key)
    encryption_time = time.time() - start_time
    
    print("Encrypted Text:", transposition_encrypted)
    print(f"Encryption Time: {encryption_time:.6f} seconds")
    
    start_time = time.time()
    transposition_decrypted = decrypt_columnar_transposition(transposition_encrypted, key)
    affine_decrypted = affine_decrypt(transposition_decrypted, a, b)
    decryption_time = time.time() - start_time
    
    print("Decrypted Text:", affine_decrypted)
    print(f"Decryption Time: {decryption_time:.6f} seconds")

if __name__ == "__main__":
    main()


