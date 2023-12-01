def swap_chars(word):
    chars = list(word)
    for i in range(0, len(chars)-1, 2):
        chars[i], chars[i+1] = chars[i+1], chars[i]
    return ''.join(chars)

def encrypt(text):
    encrypted_text = ' '.join(swap_chars(word) for word in text.split())
    return encrypted_text

def decrypt(text):
    decrypted_text = ' '.join(swap_chars(word) for word in text.split())
    return decrypted_text

# Пример использования
original_text = "Hello World"
print("Оригинальный текст:", original_text)

encrypted_text = encrypt(original_text)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Расшифрованный текст:", decrypted_text)
