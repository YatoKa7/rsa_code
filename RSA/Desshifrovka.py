# Функция для шифрования сообщения
def encrypt_message(public_key, message):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in message]
    return ciphertext

# Функция для дешифрования сообщения
def decrypt_message(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

while True:
    print("\nВыберите действие:")
    print("1. Зашифровать сообщение")
    print("2. Дешифровать сообщение")
    print("3. Выход")

    choice = input("Введите номер выбранного действия: ")

    if choice == '1':
        e = int(input("Введите значение открытой экспоненты (e): "))
        n = int(input("Введите значение модуля n: "))
        public_key = (e, n)
        message = input("Введите сообщение для шифрования: ")
        ciphertext = encrypt_message(public_key, message)
        print("Зашифрованное сообщение:", ciphertext)
    elif choice == '2':
        d = int(input("Введите значение закрытой экспоненты (d): "))
        n = int(input("Введите значение модуля n: "))
        private_key = (d, n)
        ciphertext = input("Введите зашифрованное сообщение (через пробел): ").split()
        ciphertext = [int(char) for char in ciphertext]
        plaintext = decrypt_message(private_key, ciphertext)
        print("Дешифрованное сообщение:", plaintext)
    elif choice == '3':
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
