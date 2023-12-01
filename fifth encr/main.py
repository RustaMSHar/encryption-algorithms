def encrypt_block(block):
    # Шифрование блока
    encrypted_block = list(block.ljust(6))  # Дополняем блок пробелами до 6 символов
    encrypted_block[0], encrypted_block[3], encrypted_block[5] = chr((ord(encrypted_block[0]) - 1) % 256), chr((ord(encrypted_block[3]) - 1) % 256), chr((ord(encrypted_block[5]) - 1) % 256)
    encrypted_block[1], encrypted_block[2], encrypted_block[4] = chr((ord(encrypted_block[1]) + 1) % 256), chr((ord(encrypted_block[2]) + 1) % 256), chr((ord(encrypted_block[4]) + 1) % 256)
    return ''.join(encrypted_block)

def decrypt_block(block):
    # Расшифрование блока
    decrypted_block = list(block.ljust(6))  # Дополняем блок пробелами до 6 символов
    decrypted_block[0], decrypted_block[3], decrypted_block[5] = chr((ord(decrypted_block[0]) + 1) % 256), chr((ord(decrypted_block[3]) + 1) % 256), chr((ord(decrypted_block[5]) + 1) % 256)
    decrypted_block[1], decrypted_block[2], decrypted_block[4] = chr((ord(decrypted_block[1]) - 1) % 256), chr((ord(decrypted_block[2]) - 1) % 256), chr((ord(decrypted_block[4]) - 1) % 256)
    return ''.join(decrypted_block)

def encrypt_text(text):
    # Разбиваем текст на блоки по 6 символов и шифруем каждый блок
    encrypted_text = ''
    for i in range(0, len(text), 6):
        block = text[i:i+6]
        encrypted_text += encrypt_block(block)
    return encrypted_text

def decrypt_text(text):
    # Разбиваем текст на блоки по 6 символов и расшифровываем каждый блок
    decrypted_text = ''
    for i in range(0, len(text), 6):
        block = text[i:i+6]
        decrypted_text += decrypt_block(block)
    return decrypted_text

# Пример использования
plaintext = "Hello, World!"
encrypted_text = encrypt_text(plaintext)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = decrypt_text(encrypted_text)
print("Расшифрованный текст:", decrypted_text)
