import math
import time

def encrypt_columnar_transposition(plaintext, key):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    num_cols = len(key)
    num_rows = math.ceil(len(plaintext) / num_cols)
    
    # Pad the plaintext with spaces if necessary
    plaintext += ' ' * (num_rows * num_cols - len(plaintext))
    
    # Create the matrix
    matrix = [list(plaintext[i:i+num_cols]) for i in range(0, len(plaintext), num_cols)]
    
    # Read columns in the order of the key
    ciphertext = ''
    for index, _ in key_order:
        for row in matrix:
            ciphertext += row[index]
    
    return ciphertext

def decrypt_columnar_transposition(ciphertext, key):
    key_order = sorted(list(enumerate(key)), key=lambda x: x[1])
    num_cols = len(key)
    num_rows = math.ceil(len(ciphertext) / num_cols)
    
    # Create an empty matrix
    matrix = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    index = 0
    for col_index, _ in key_order:
        for row in range(num_rows):
            if index < len(ciphertext):
                matrix[row][col_index] = ciphertext[index]
                index += 1
    
    # Read the matrix row-wise to get plaintext
    plaintext = ''.join([''.join(row) for row in matrix]).rstrip()
    
    return plaintext

def main():
    plaintext = input("Please enter the plaintext: ")
    key = input("Please enter the numeric key (example: 3124): ")
    key = [int(digit) for digit in key]
    
    # Measure encryption time
    start_encrypt = time.time()
    ciphertext = encrypt_columnar_transposition(plaintext, key)
    end_encrypt = time.time()
    encryption_time = end_encrypt - start_encrypt

    print("\nEncrypted Text:", ciphertext)
    print("Encryption Time: {:.6f} seconds".format(encryption_time))
    
    # Measure decryption time
    start_decrypt = time.time()
    decrypted_text = decrypt_columnar_transposition(ciphertext, key)
    end_decrypt = time.time()
    decryption_time = end_decrypt - start_decrypt

    print("\nDecrypted Text:", decrypted_text)
    print("Decryption Time: {:.6f} seconds".format(decryption_time))

if __name__ == "__main__":
    main()
