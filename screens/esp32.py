import random
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from .centraliza_tela import center_window
from .config_screens import window_height, window_width
from service.serial import get_existing_id


def abrir_janela_esp32(root):
    janela_esp32 = tk.Toplevel(root)
    janela_esp32.title("ESP32")
    center_window(janela_esp32, window_width, window_height)
    janela_esp32.resizable(False, False)

    # Variável para armazenar o ID gerado
    id_var = tk.StringVar(value="")

    existing_id = get_existing_id()
    if existing_id:
        id_var.set(existing_id)

    # Container principal para os widgets centralizados verticalmente
    container = ttk.Frame(janela_esp32)
    # Posiciona no centro da janela
    container.place(relx=0.5, rely=0.5, anchor='center')

    label_port = ttk.Label(container, text="Selecione a porta serial:")
    label_port.pack(pady=(10, 0))

    port_combobox = ttk.Combobox(container, width=37)
    port_combobox['values'] = ['COM3', 'COM4', 'COM5']
    port_combobox.pack(pady=10)
    port_combobox.current(0)

    
    # Campo de entrada do nome da ESP32
    label_name = ttk.Label(
        container, text="Nome do dispositivo: ", font=("Helvetica", 14))
    label_name.pack(pady=(10, 0))
    entry_name = ttk.Entry(container, width=40)
    entry_name.pack(ipady=10, pady=20)

    # Campo de entrada de ID
    label_id = ttk.Label(container, text="ID: ", font=("Helvetica", 14))
    label_id.pack(pady=(10, 0))
    entry_id = ttk.Entry(container, textvariable=id_var, width=40)
    entry_id.pack(ipady=10, pady=20)

    # Botões gerar e gravar ID abaixo do campo de entrada
    button_container = ttk.Frame(container)
    button_container.pack(pady=10)

    def generate_id():
        if not existing_id:
            id_generated = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
            id_var.set(id_generated)
            save_button.pack(side='left', padx=10)  # Mostra o botão Gravar

    generate_button = ttk.Button(
        button_container, text="Gerar ID", command=generate_id)
    generate_button.pack(side='left', padx=10)

    def save_id():
        # Grava o ID gerado
        if id_var.get():
            messagebox.showinfo("Sucesso", "ID gravado com sucesso na ESP32!")
        else:
            messagebox.showerror("Falha", "Falha ao gravar ID.")
        save_button.pack_forget()  # Oculta o botão Gravar

    save_button = ttk.Button(
        button_container, text="Gravar ID", command=save_id)
    save_button.pack_forget()  # Oculto até um ID ser gerado
