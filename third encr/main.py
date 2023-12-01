import string

def load_table(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().strip()

def encrypt(text, table):
    words = text.split()
    encrypted_text = []

    for i, word in enumerate(words):
        # Проверка, является ли слово нечетным
        is_odd_word = i % 2 == 1

        # Удаление знаков препинания из слова
        word = word.strip(string.punctuation)

        # Если слово нечетное, перевернем буквы
        if is_odd_word:
            encrypted_word = ''.join(table.get(char, char) for char in reversed(word))
        else:
            encrypted_word = word

        # Возвращаем слово к исходному виду с добавлением знаков препинания
        encrypted_text.append(encrypted_word + string.punctuation)

    return ' '.join(encrypted_text)

def decrypt(text, table):
    return encrypt(text, table)  # Расшифровка аналогична шифрованию

def main():
    table_filename = input("Введите имя файла с таблицей замены: ")
    text = input("Введите текст: ")

    # Загрузка таблицы замены из файла
    table_str = load_table(table_filename)

    # Проверка, что строка имеет четную длину
    if len(table_str) % 2 != 0:
        print("Ошибка: Нечетное количество символов в таблице замены.")
        return

    # Создание словаря замены из строки таблицы
    table = dict(zip(table_str[:len(table_str)//2], table_str[len(table_str)//2:]))

    # Шифрование текста
    encrypted_text = encrypt(text, table)
    print(f"Зашифрованный текст: {encrypted_text}")

    # Расшифрование текста
    decrypted_text = decrypt(encrypted_text, table)
    print(f"Расшифрованный текст: {decrypted_text}")

if __name__ == "__main__":
    main()
