import random

def generate_key():
    key = {}
    for i in range(256):
        key[chr(i)] = i * 2
    return key

def encrypt(input_file, output_file, key):
    with open(input_file, 'r', encoding='utf-8') as file:
        plaintext = file.read()

    ciphertext = ''
    for char in plaintext:
        if char in key:
            ciphertext += str(key[char]) + ' '
        else:
            ciphertext += str(ord(char)) + ' '

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(ciphertext)

def decrypt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        ciphertext = file.read()

    plaintext = ''.join(chr(int(token) // 2) for token in ciphertext.split())

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(plaintext)

# Пример использования:
input_filename = 'input.txt'
encrypted_filename = 'encrypted.txt'
decrypted_filename = 'decrypted.txt'

# Генерация ключа
key = generate_key()

# Шифрование
encrypt(input_filename, encrypted_filename, key)

# Расшифровка
decrypt(encrypted_filename, decrypted_filename)
