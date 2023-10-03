import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

# Функция для шифрования сообщения
def encrypt_message():
    e = int(e_entry.get())
    n = int(n_entry.get())
    message = message_entry.get()
    ciphertext = [pow(ord(char), e, n) for char in message]
    ciphertext_text.set("Зашифрованное сообщение: " + ' '.join(map(str, ciphertext)))
    # Копирование зашифрованного сообщения в буфер обмена
    root.clipboard_clear()
    root.clipboard_append(' '.join(map(str, ciphertext)))
    root.update()  # Обновление буфера обмена

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

# Кнопка для копирования зашифрованного сообщения
copy_button = ttk.Button(root, text="Копировать зашифрованное сообщение")
copy_button.pack()

def copy_ciphertext():
    ciphertext = ciphertext_text.get().split(": ")[1]  # Извлечение зашифрованного текста
    root.clipboard_clear()
    root.clipboard_append(ciphertext)
    root.update()
    messagebox.showinfo("Копирование", "Зашифрованное сообщение скопировано в буфер обмена")

copy_button.config(command=copy_ciphertext)

root.mainloop()
