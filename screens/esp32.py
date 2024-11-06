import random
import tkinter as tk
from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
from .centraliza_tela import center_window
from .config_screens import window_height, window_width
from service.serial import send_device_info, open_serial_connection, get_existing_data
from screens.close_screen import CloseScreen


def abrir_janela_esp32(root):
    root.withdraw()
    janela_esp32 = tk.Toplevel(root)
    janela_esp32.title("ESP32")
    center_window(janela_esp32, window_width, window_height)
    janela_esp32.resizable(False, False)
    janela_esp32.grab_set()
    fecha_janela = CloseScreen(root=root)

    # Variáveis para armazenar informações
    id_var = tk.StringVar(value="")
    nome_dispositivo = tk.StringVar(value="")

    # Conexão serial global
    global serial_connection
    serial_connection = open_serial_connection('COM4')  # Assume que retorna um tuple (connection, status)
    print(serial_connection)
    if not serial_connection:
        messagebox.showerror("Erro Serial", "Não foi possível abrir a conexão serial na porta padrão. COM3")

    

    # Obter dados existentes do dispositivo
    existing_data = get_existing_data(True)
    can_generate_id = True  # Presume que pode gerar um novo ID por padrão
    if existing_data:
        nome_dispositivo.set(existing_data['nome'])
        id_var.set(existing_data['id'])
        can_generate_id = False  # Desativa a geração de novo ID se já existir

    # Container principal para os widgets
    container = ttk.Frame(janela_esp32)
    container.place(relx=0.5, rely=0.5, anchor='center')

    # Combobox para seleção de porta serial
    label_port = ttk.Label(container, text="Selecione a porta serial:")
    label_port.pack(pady=(10, 0))
    port_combobox = ttk.Combobox(container, width=37, values=[
                                 'COM3', 'COM4', 'COM5'])
    port_combobox.pack(pady=10)
    port_combobox.set('COM4')  # Define a porta padrão ou a última usada
    
    def on_port_selected(event):
        global serial_connection
        selected_port = port_combobox.get()
        new_serial_connection, success = open_serial_connection(selected_port)
        if success:
            serial_connection = new_serial_connection  # Atualiza a conexão serial
            messagebox.showinfo("Conexão Serial", f"Conexão estabelecida com sucesso na porta {selected_port}.")
        else:
            messagebox.showerror("Conexão Serial", f"Falha ao estabelecer conexão na porta {selected_port}.")

    port_combobox.bind("<<ComboboxSelected>>", on_port_selected)

    # Campo de entrada do nome do dispositivo
    label_name = ttk.Label(
        container, text="Nome do dispositivo:", font=("Helvetica", 14))
    label_name.pack(pady=(10, 0))
    entry_name = ttk.Entry(container, textvariable=nome_dispositivo, width=40)
    entry_name.pack(ipady=10, pady=10)

    # Campo de entrada de ID
    label_id = ttk.Label(container, text="ID:", font=("Helvetica", 14))
    label_id.pack(pady=(10, 0))
    entry_id = ttk.Entry(container, textvariable=id_var, width=40,
                         state='normal' if can_generate_id else 'disabled')
    entry_id.pack(ipady=10, pady=20)

    # Botão para gerar um novo ID
    generate_button = ttk.Button(
        container, text="Gerar ID", command=lambda: generate_id(id_var))
    if can_generate_id:
        generate_button.pack(side='left', padx=10)

    # Botão para salvar as alterações
    save_button = ttk.Button(container, text="Salvar alterações", command=lambda: save_id(
        serial_connection, nome_dispositivo.get(), id_var.get()))
    save_button.pack(side='bottom', pady=20)


    def generate_id(id_var):
        id_generated = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
        id_var.set(id_generated)


    def save_id(serial_connection, name, device_id):
        if name and device_id:
            send_device_info(serial_connection, name, device_id)
            messagebox.showinfo(
            "Sucesso", f"ID: {device_id} e nome: {name} salvos com sucesso!")
        else:
            messagebox.showerror(
            "Erro", "Nome do dispositivo e ID são necessários.")

    # Fechamento da tela
    voltar_button = tk.Button(janela_esp32, text="← Voltar",  command=lambda: fecha_janela.close_and_return(janela_esp32))
    voltar_button.place(x=10, y=10)
    janela_esp32.protocol("WM_DELETE_WINDOW", lambda: fecha_janela.close_and_return(janela_esp32))
