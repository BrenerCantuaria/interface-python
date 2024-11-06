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
from service.serial import send_device_info, open_serial_connection
from screens.close_screen import CloseScreen

def abrir_janela_esp32(root):
    root.withdraw()
    janela_esp32 = tk.Toplevel(root)
    janela_esp32.title("ESP32")
    center_window(janela_esp32, window_width, window_height)
    janela_esp32.resizable(False, False)
    janela_esp32.grab_set()
    fecha_janela = CloseScreen(root=root)

    
    
    # Variável para armazenar o informações
    id_var = tk.StringVar(value="")
    nome_dispositivo = tk.StringVar(value="")

    existing_id = get_existing_id()
    if existing_id:
        print("ID existente:", existing_id[0]['id'])  # Debug
        print("Nome do dispositivo:",
              existing_id[0]['nome_dispositivo'])  # Debug
        id_var.set(existing_id[0]['id'])
        nome_dispositivo.set(existing_id[0]['nome_dispositivo'])

    # Elementos em tela

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

    # Adiciona um observador para mudanças no Combobox
    def on_port_selected(event):
        selected_port = port_combobox.get()
        print(f"Porta selecionada: {selected_port}")
        open_serial_connection(selected_port)

    port_combobox.bind("<<ComboboxSelected>>", on_port_selected)

    # Campo de entrada do nome da ESP32
    label_name = ttk.Label(
        container, text="Nome do dispositivo: ", font=("Helvetica", 14))
    label_name.pack(pady=(10, 0))
    entry_name = tk.Entry(container, textvariable=nome_dispositivo, width=40)
    entry_name.pack(ipady=10, pady=10)

    # Campo de entrada de ID
    label_id = ttk.Label(container, text="ID: ", font=("Helvetica", 14))
    label_id.pack(pady=(10, 0))
    entry_id = ttk.Entry(container, textvariable=id_var, width=40)
    entry_id.pack(ipady=10, pady=20)

    # Botões gerar e gravar ID abaixo do campo de entrada
    button_container = ttk.Frame(container)
    button_container.pack(pady=10)

    def generate_id():
        if existing_id[0]['id'] == None:
            id_generated = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
            id_var.set(id_generated)
            save_button.pack(side='left', padx=10)  # Mostra o botão Gravar

    generate_button = ttk.Button(
        button_container, text="Gerar ID", command=generate_id)
    generate_button.pack(side='left', padx=10)

    def save_id():
        # Grava o ID gerado
        if id_var.get() and nome_dispositivo.get() != "":
            send_device_info(True, nome_dispositivo, id_var)
            messagebox.showinfo(
                "Sucesso", f"ID:{id_var.get()} gravado com sucesso na ESP32!")
        else:
            messagebox.showerror(
                "Falha", "Falha ao gravar ID, o campo nome não pode estar vazio.")
        save_button.pack_forget()  # Oculta o botão Gravar

    def save_database():
        messagebox.showinfo("Salvar", "Alterações salvas no banco de dados")

   


    #Ação de botões 
    save_button = ttk.Button(
        button_container, text="Gravar ID", command=save_id)
    save_button.pack_forget()  # Oculto até um ID ser gerado

    salvar_alteracoes = ttk.Button(janela_esp32, text="Salvar alterações", command=save_database)
    salvar_alteracoes.pack(side='bottom', pady=20)  # Posiciona no fundo da janela

    # Fechamento da tela
    voltar_button = tk.Button(janela_esp32, text="← Voltar",  command=lambda: fecha_janela.close_and_return(janela_esp32))
    voltar_button.place(x=10, y=10)
    janela_esp32.protocol("WM_DELETE_WINDOW", lambda: fecha_janela.close_and_return(janela_esp32))