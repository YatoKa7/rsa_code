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
    # Копирование дешифрованного сообщения в буфер обмена
    root.clipboard_clear()
    root.clipboard_append(plaintext)
    root.update()  # Обновление буфера обмена

# Функция для копирования текста из поля ввода
def copy_text(entry):
    text = entry.get()
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()
    messagebox.showinfo("Копирование", "Текст скопирован в буфер обмена")

# Функция для создания контекстного меню
def create_context_menu(event):
    menu = tk.Menu(root, tearoff=0)
    if event.widget != ciphertext_entry:  # Исключаем поле для дешифрования
        menu.add_command(label="Вставить", command=lambda: paste_text(event.widget))
    menu.post(event.x_root, event.y_root)

# Функция для вставки текста из буфера обмена в поле ввода
def paste_text(entry):
    clipboard_data = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, clipboard_data)

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
e_label.pack()
e_entry = tk.Entry(root)
e_entry.pack()

# Прикрепление контекстного меню к полю ввода открытой экспоненты
e_entry.bind("<Button-3>", create_context_menu)

n_label = tk.Label(root, text="Модуль (n):")
n_label.pack()
n_entry = tk.Entry(root)
n_entry.pack()

# Прикрепление контекстного меню к полю ввода модуля
n_entry.bind("<Button-3>", create_context_menu)

# Ввод закрытой экспоненты (d)
d_label = tk.Label(root, text="Закрытая экспонента (d):")
d_label.pack()
d_entry = tk.Entry(root)
d_entry.pack()

# Прикрепление контекстного меню к полю ввода закрытой экспоненты
d_entry.bind("<Button-3>", create_context_menu)

# Ввод сообщения и вывод результатов
message_label = tk.Label(root, text="Сообщение:")
message_label.pack()
message_entry = tk.Entry(root)
message_entry.pack()

# Прикрепление контекстного меню к полю ввода сообщения
message_entry.bind("<Button-3>", create_context_menu)

encrypt_button = tk.Button(root, text="Зашифровать", command=encrypt_message)
encrypt_button.pack()

ciphertext_text = tk.StringVar()
ciphertext_label = tk.Label(root, textvariable=ciphertext_text)
ciphertext_label.pack()

ciphertext_entry = tk.Entry(root)
ciphertext_entry.pack()

# Прикрепление контекстного меню к полю ввода зашифрованного сообщения
ciphertext_entry.bind("<Button-3>", create_context_menu)

decrypt_button = tk.Button(root, text="Дешифровать", command=decrypt_message)
decrypt_button.pack()

plaintext_text = tk.StringVar()
plaintext_label = tk.Label(root, textvariable=plaintext_text)
plaintext_label.pack()

# Кнопка для очистки всех полей ввода
clear_button = ttk.Button(root, text="Очистить поля", command=clear_fields)
clear_button.pack()

# Кнопка для копирования дешифрованного сообщения
copy_decrypt_button = ttk.Button(root, text="Копировать дешифрованное сообщение", command=lambda: copy_text(plaintext_label))
copy_decrypt_button.pack()

root.mainloop()
