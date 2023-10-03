import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
from tkinter import simpledialog

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
    # Копирование дешифрованного сообщения в буфер обмена
    root.clipboard_clear()
    root.clipboard_append(plaintext)
    root.update()  # Обновление буфера обмена

# Функция для открытия окна для расшифровки сообщения
def open_decrypt_window():
    password = simpledialog.askstring("Расшифровать сообщение", "Введите пароль для расшифровки:")
    if password is not None:
        try:
            d = int(d_entry.get())
            n = int(n_entry.get())
            ciphertext = list(map(int, ciphertext_entry.get().split()))
            plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
            decrypted_message = decrypt_with_password(plaintext, password)
            plaintext_text.set("Дешифрованное сообщение: " + decrypted_message)
            # Копирование дешифрованного сообщения в буфер обмена
            root.clipboard_clear()
            root.clipboard_append(decrypted_message)
            root.update()  # Обновление буфера обмена
        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректные значения для d и n")

# Функция для дешифрования сообщения с паролем
def decrypt_with_password(ciphertext, password):
    decrypted_message = ""
    for i, char in enumerate(ciphertext):
        decrypted_char = chr(ord(char) - ord(password[i % len(password)]))
        decrypted_message += decrypted_char
    return decrypted_message

# Функция для вставки текста из буфера обмена в поле ввода
def paste_text(entry):
    clipboard_data = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, clipboard_data)

# Функция для создания контекстного меню
def create_context_menu(event, entry):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Вставить", command=lambda: paste_text(entry))
    menu.post(event.x_root, event.y_root)

# Функция для очистки всех полей ввода
def clear_fields():
    e_entry.delete(0, tk.END)
    n_entry.delete(0, tk.END)
    d_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_text.set("Зашифрованное сообщение:")
    plaintext_text.set("Дешифрованное сообщение:")

# Создание графического интерфейса с помощью Tkinter
root = tk.Tk()
root.title("RSA Шифрование/Дешифрование")

# Ввод открытого ключа (e, n)
e_label = tk.Label(root, text="Открытая экспонента (e):")
e_label.grid(row=0, column=0, sticky="w")
e_entry = tk.Entry(root)
e_entry.grid(row=0, column=1)

n_label = tk.Label(root, text="Модуль (n):")
n_label.grid(row=1, column=0, sticky="w")
n_entry = tk.Entry(root)
n_entry.grid(row=1, column=1)

# Ввод закрытой экспоненты (d)
d_label = tk.Label(root, text="Закрытая экспонента (d):")
d_label.grid(row=2, column=0, sticky="w")
d_entry = tk.Entry(root)
d_entry.grid(row=2, column=1)

# Ввод сообщения и вывод результатов
message_label = tk.Label(root, text="Сообщение:")
message_label.grid(row=3, column=0, sticky="w")
message_entry = tk.Entry(root)
message_entry.grid(row=3, column=1)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message)
encrypt_button.grid(row=4, column=0, columnspan=2)

ciphertext_text = tk.StringVar()
ciphertext_label = tk.Label(root, textvariable=ciphertext_text)
ciphertext_label.grid(row=5, column=0, columnspan=2)

ciphertext_entry = tk.Entry(root)
ciphertext_entry.grid(row=6, column=0, columnspan=2)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message)
decrypt_button.grid(row=7, column=0, columnspan=2)

# Добавление кнопки для расшифровки сообщения
decrypt_window_button = tk.Button(root, text="Расшифровать сообщение", command=open_decrypt_window)
decrypt_window_button.grid(row=8, column=0, columnspan=2)

plaintext_text = tk.StringVar()
plaintext_label = tk.Label(root, textvariable=plaintext_text)
plaintext_label.grid(row=9, column=0, columnspan=2)

# Прикрепление контекстного меню к полям ввода
message_entry.bind("<Button-3>", lambda event: create_context_menu(event, message_entry))
ciphertext_entry.bind("<Button-3>", lambda event: create_context_menu(event, ciphertext_entry))

# Кнопка для копирования дешифрованного сообщения
copy_decrypt_button = ttk.Button(root, text="Copy", command=lambda: copy_text(plaintext_label))
copy_decrypt_button.grid(row=10, column=0, columnspan=2)

# Кнопка для копирования зашифрованного сообщения
copy_encrypt_button = ttk.Button(root, text="Copy", command=lambda: copy_text(ciphertext_entry))
copy_encrypt_button.grid(row=11, column=0, columnspan=2)

# Кнопка для очистки всех полей ввода
clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=12, column=0, columnspan=2)

root.mainloop()
