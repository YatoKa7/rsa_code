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
def generate_rsa_keys(bits):
    # Генерация случайных простых чисел p и q
    while True:
        p = random.getrandbits(bits)
        if p % 2 != 0 and all(p % i != 0 for i in range(2, int(p**0.5) + 1)):
            break
    while True:
        q = random.getrandbits(bits)
        if q % 2 != 0 and all(q % i != 0 for i in range(2, int(q**0.5) + 1)):
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбор открытой экспоненты (e)
    e = random.randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = random.randint(2, phi - 1)

    # Вычисление закрытой экспоненты (d)
    d = mod_inverse(e, phi)

    return (e, n), (d, n)

# Генерация ключей
key_size = 16  # Размер ключа (в битах)
public_key, private_key = generate_rsa_keys(key_size)

# Вывод ключей
print("Открытый ключ (e, n):", public_key)
print("Закрытый ключ (d, n):", private_key)
