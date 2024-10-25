import tkinter as tk
from tkinter import Label, Button, StringVar, Frame, Entry
from .centraliza_tela import center_window
from .config_screens import window_height,window_width

import random

def abrir_janela_esp32(root):
    janela_esp32 = tk.Toplevel(root)
    janela_esp32.title("ESP32")
    center_window(janela_esp32, window_width, window_height)
    janela_esp32.resizable(False, False)
    manage_esp32_id(janela_esp32)

def manage_esp32_id(window):
    esp32_id = None
    id_var = StringVar()
    container = tk.Frame(window)
    container.pack(padx=20, pady=20)

    id_label = Label(container, text="ID:", font=('Helvetica', 12))
    id_label.grid(row=0, column=0, pady=(0, 20))

    entry_id = Entry(container, textvariable=id_var, width=30)
    entry_id.grid(row=0, column=1)

    def generate_id():
        nonlocal esp32_id
        esp32_id = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
        id_var.set(esp32_id)
        generate_button.pack_forget()
        save_button.pack()

    generate_button = Button(container, text="Gerar ID", command=generate_id, font=('Helvetica', 12))
    generate_button.grid(row=0, column=2, padx=10)

    save_button = Button(window, text="Gravar ID", font=('Helvetica', 12))
    save_button.pack_forget()  # Inicialmente oculto
