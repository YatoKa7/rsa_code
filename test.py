# print("Barev Valodik")

import random

# Функция для нахождения НОД (наибольшего общего делителя) двух чисел
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Функция для вычисления обратного элемента в кольце вычетов
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

# Генерация ключей RSA
def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбор открытой экспоненты (e), обычно 65537
    e = 65537

    # Вычисление закрытой экспоненты (d)
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Шифрование сообщения
def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# Дешифрование сообщения
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Пример использования
if __name__ == "__main__":
    p = 61
    q = 53
    public_key, private_key = generate_keypair(p, q)

    message = "Hello, RSA!"
    encrypted_message = encrypt(public_key, message)
    decrypted_message = decrypt(private_key, encrypted_message)

    print("Original message:", message)
    print("Encrypted message:", encrypted_message)
    print("Decrypted message:", decrypted_message)


