import tkinter as tk

# Функция для шифрования сообщения
def encrypt_message():
    e = int(e_entry.get())
    n = int(n_entry.get())
    message = message_entry.get()
    ciphertext = [pow(ord(char), e, n) for char in message]
    ciphertext_text.set("Зашифрованное сообщение: " + ' '.join(map(str, ciphertext)))

# Функция для дешифрования сообщения
def decrypt_message():
    d = int(d_entry.get())
    n = int(n_entry.get())
    ciphertext = list(map(int, ciphertext_entry.get().split()))
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    plaintext_text.set("Дешифрованное сообщение: " + plaintext)

# Создание графического интерфейса с помощью Tkinter
root = tk.Tk()
root.title("RSA Шифрование/Дешифрование")

# Ввод открытого ключа (e, n)
e_label = tk.Label(root, text="Открытая экспонента (e):")
e_label.pack()
e_entry = tk.Entry(root)
e_entry.pack()

n_label = tk.Label(root, text="Модуль (n):")
n_label.pack()
n_entry = tk.Entry(root)
n_entry.pack()

# Ввод закрытой экспоненты (d)
d_label = tk.Label(root, text="Закрытая экспонента (d):")
d_label.pack()
d_entry = tk.Entry(root)
d_entry.pack()

# Ввод сообщения и вывод результатов
message_label = tk.Label(root, text="Сообщение:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

encrypt_button = tk.Button(root, text="Зашифровать", command=encrypt_message)
encrypt_button.pack()

ciphertext_text = tk.StringVar()
ciphertext_label = tk.Label(root, textvariable=ciphertext_text)
ciphertext_label.pack()

ciphertext_entry = tk.Entry(root)
ciphertext_entry.pack()

decrypt_button = tk.Button(root, text="Дешифровать", command=decrypt_message)
decrypt_button.pack()

plaintext_text = tk.StringVar()
plaintext_label = tk.Label(root, textvariable=plaintext_text)
plaintext_label.pack()

root.mainloop()
