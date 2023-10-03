import tkinter as tk
import tkinter.ttk as ttk
from tkinter import simpledialog

def encrypt_message():
    e = int(e_entry.get())
    n = int(n_entry.get())
    message = message_entry.get()
    ciphertext = [pow(ord(char), e, n) for char in message]
    ciphertext_text.set("Зашифрованное сообщение: " + ' '.join(map(str, ciphertext)))

def decrypt_message():
    d = int(d_entry.get())
    n = int(n_entry.get())
    ciphertext = list(map(int, ciphertext_entry.get().split()))
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    plaintext_text.set("Дешифрованное сообщение: " + plaintext)

def open_decrypt_window():
    password = simpledialog.askstring("Расшифровать сообщение", "Введите пароль для расшифровки:")
    if password is not None:
        try:
            d = int(d_entry.get())
            n = int(n_entry.get())
            ciphertext = list(map(int, ciphertext_entry.get().split()))
            plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
            decrypted_message = decrypt_with_password(plaintext, password)
            show_decrypt_window(decrypted_message)
        except ValueError:
            pass

def show_decrypt_window(plaintext):
    decrypt_window = tk.Toplevel(root)
    decrypt_window.title("Дешифрование сообщения")

    plaintext_label = tk.Label(decrypt_window, text="Дешифрованное сообщение:")
    plaintext_label.pack()

    plaintext_text = tk.StringVar()
    plaintext_text.set(plaintext)
    plaintext_display = tk.Label(decrypt_window, textvariable=plaintext_text)
    plaintext_display.pack()

    close_button = tk.Button(decrypt_window, text="Закрыть", command=decrypt_window.destroy)
    close_button.pack()

def decrypt_with_password(ciphertext, password):
    decrypted_message = ""
    for i, char in enumerate(ciphertext):
        decrypted_char = chr(ord(char) - ord(password[i % len(password)]))
        decrypted_message += decrypted_char
    return decrypted_message

def paste_text(entry):
    clipboard_data = root.clipboard_get()
    entry.delete(0, tk.END)
    entry.insert(0, clipboard_data)

def create_context_menu(event, entry):
    menu = tk.Menu(root, tearoff=0)
    menu.add_command(label="Вставить", command=lambda: paste_text(entry))
    menu.add_separator()
    menu.add_command(label="Расшифровать", command=open_decrypt_window)
    menu.add_command(label="Дешифровать", command=decrypt_message)
    menu.post(event.x_root, event.y_root)

def clear_fields():
    e_entry.delete(0, tk.END)
    n_entry.delete(0, tk.END)
    d_entry.delete(0, tk.END)
    message_entry.delete(0, tk.END)
    ciphertext_entry.delete(0, tk.END)
    ciphertext_text.set("Зашифрованное сообщение:")
    plaintext_text.set("Дешифрованное сообщение:")

root = tk.Tk()
root.title("RSA Шифрование/Дешифрование")

# Создание главного меню
main_menu = tk.Menu(root)
root.config(menu=main_menu)

# Добавление кнопок в главное меню
decrypt_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Главное меню", menu=decrypt_menu)
decrypt_menu.add_command(label="Расшифровать", command=open_decrypt_window)
decrypt_menu.add_command(label="Дешифровать", command=decrypt_message)

e_label = tk.Label(root, text="Открытая экспонента (e):")
e_label.grid(row=0, column=0, sticky="w")
e_entry = tk.Entry(root)
e_entry.grid(row=0, column=1)

n_label = tk.Label(root, text="Модуль (n):")
n_label.grid(row=1, column=0, sticky="w")
n_entry = tk.Entry(root)
n_entry.grid(row=1, column=1)

d_label = tk.Label(root, text="Закрытая экспонента (d):")
d_label.grid(row=2, column=0, sticky="w")
d_entry = tk.Entry(root)
d_entry.grid(row=2, column=1)

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

message_entry.bind("<Button-3>", lambda event: create_context_menu(event, message_entry))
ciphertext_entry.bind("<Button-3>", lambda event: create_context_menu(event, ciphertext_entry))

copy_decrypt_button = ttk.Button(root, text="Copy", command=lambda: paste_text(plaintext_label))
copy_decrypt_button.grid(row=7, column=0, columnspan=2)

copy_encrypt_button = ttk.Button(root, text="Copy", command=lambda: paste_text(ciphertext_entry))
copy_encrypt_button.grid(row=8, column=0, columnspan=2)

clear_button = ttk.Button(root, text="Clear", command=clear_fields)
clear_button.grid(row=9, column=0, columnspan=2)

root.mainloop()
