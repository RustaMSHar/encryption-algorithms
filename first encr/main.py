def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') + shift) % 26 + ord('A' if char.isupper() else 'a'))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            decrypted_char = chr((ord(char) - ord('A' if char.isupper() else 'a') - shift) % 26 + ord('A' if char.isupper() else 'a'))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text

# Получаем текст и сдвиг от пользователя
input_text = input("Введите текст: ")
shift_value = int(input("Введите число для сдвига: "))

# Шифруем и расшифровываем текст
encrypted_text = encrypt(input_text, shift_value)
decrypted_text = decrypt(encrypted_text, shift_value)

# Выводим результаты
print("Зашифрованный текст:", encrypted_text)
print("Расшифрованный текст:", decrypted_text)
