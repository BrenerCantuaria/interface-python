import random
import tkinter as tk
from tkinter import ttk, messagebox
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from .centraliza_tela import center_window
from .config_screens import window_height,window_width

# Simulando a função que verifica se já existe um ID na ESP32
def get_existing_id():
    # Esta função deve interagir com o hardware ESP32 para obter o ID existente
    # Aqui está simulado como se sempre houvesse um ID já existente
    return None # Simula um ID existente


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
    container.place(relx=0.5, rely=0.5, anchor='center')  # Posiciona no centro da janela

    # Campo de entrada de ID
    entry_id = ttk.Entry(container, textvariable=id_var, width=40)
    entry_id.pack(ipady=10, pady=20)  # Aumenta o padding interno para maior altura

    # Botões gerar e gravar ID abaixo do campo de entrada
    button_container = ttk.Frame(container)
    button_container.pack(pady=10)

    def generate_id():
        if not existing_id:
            id_generated = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
            id_var.set(id_generated)
            save_button.pack(side='left', padx=10)  # Mostra o botão Gravar

    generate_button = ttk.Button(button_container, text="Gerar ID", command=generate_id)
    generate_button.pack(side='left', padx=10)

    def save_id():
        # Grava o ID gerado
        if id_var.get():
            messagebox.showinfo("Sucesso", "ID gravado com sucesso na ESP32!")
        else:
            messagebox.showerror("Falha", "Falha ao gravar ID.")
        save_button.pack_forget()  # Oculta o botão Gravar

    save_button = ttk.Button(button_container, text="Gravar ID", command=save_id)
    save_button.pack_forget()  # Oculto até um ID ser gerado