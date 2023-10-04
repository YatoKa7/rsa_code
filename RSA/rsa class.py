class Encryptor:
    def __init__(self, public_key):
        self.e, self.n = public_key

    def encrypt_message(self, message):
        ciphertext = [pow(ord(char), self.e, self.n) for char in message]
        return ciphertext


class Decryptor:
    def __init__(self, private_key):
        self.d, self.n = private_key

    def decrypt_message(self, ciphertext):
        plaintext = ''.join([chr(pow(char, self.d, self.n)) for char in ciphertext])
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
        encryptor = Encryptor(public_key)
        message = input("Введите сообщение для шифрования: ")
        ciphertext = encryptor.encrypt_message(message)
        print("Зашифрованное сообщение:", ciphertext)
    elif choice == '2':
        d = int(input("Введите значение закрытой экспоненты (d): "))
        n = int(input("Введите значение модуля n: "))
        private_key = (d, n)
        decryptor = Decryptor(private_key)
        ciphertext = input("Введите зашифрованное сообщение (через пробел): ").split()
        ciphertext = [int(char) for char in ciphertext]
        plaintext = decryptor.decrypt_message(ciphertext)
        print("Дешифрованное сообщение:", plaintext)
    elif choice == '3':
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")
