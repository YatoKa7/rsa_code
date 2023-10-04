# Дешифрование сообщения
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Использование закрытого ключа для дешифрования
private_key = (d, n)  # Здесь 'd' и 'n' - это закрытый ключ

input = (a)
a = ciphertext
ciphertext = [здесь должен быть ваш зашифрованный текст в виде списка чисел]
decrypted_message = decrypt(private_key, ciphertext)
print("Decrypted message:", decrypted_message)
