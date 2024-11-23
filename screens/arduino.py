import tkinter as tk
from tkinter import ttk, messagebox
from .centraliza_tela import center_window
from .config_screens import window_height, window_width
from service.serial import open_serial_connection, get_existing_data
from screens.close_screen import CloseScreen

# Variável global para a conexão serial
serial_connection_arduino = None

def get_dispositivos_eps32():
    return ["ESP32 Dev Kit", "ESP32 WROOM", "ESP32 WROVER"]

def abrir_janela_arduino(root):
    global serial_connection_arduino
    root.withdraw()
    janela_arduino = tk.Toplevel(root)
    janela_arduino.title("Arduino")
    center_window(janela_arduino, window_width, window_height)
    janela_arduino.resizable(False, False)
    fecha_janela = CloseScreen(root=root)

    # Variáveis para armazenar informações
    id_var = tk.StringVar(value="")
    nome_dispositivo = tk.StringVar(value="")

    # Container principal para os widgets
    container = ttk.Frame(janela_arduino)
    container.pack(padx=20, pady=20, fill='both', expand=True)

    dispositivos = get_dispositivos_eps32()

    # Combobox para selecionar dispositivos ESP32
    label_dispositivo = ttk.Label(container, text="Selecione o dispositivo ESP32:")
    label_dispositivo.pack(pady=(10, 5))

    combobox_dispositivo = ttk.Combobox(container, values=dispositivos, state="readonly")
    combobox_dispositivo.pack(pady=(0, 20))
    combobox_dispositivo.current(0) if dispositivos else None

    # Combobox para seleção de porta serial
    label_port = ttk.Label(container, text="Selecione a porta serial:")
    label_port.pack(pady=(10, 0))
    port_combobox = ttk.Combobox(container, width=37, values=['COM3', 'COM4', 'COM5'], state="readonly")
    port_combobox.pack(pady=10)
    port_combobox.set('COM4')  # Define a porta padrão

    # Monitora mudanças na seleção da porta serial
    def on_port_selected(event):
        global serial_connection_arduino
        selected_port = port_combobox.get()
        new_connection, success = open_serial_connection(selected_port)
        if success:
            serial_connection_arduino = new_connection
            messagebox.showinfo("Conexão Serial", f"Conexão estabelecida com sucesso na porta {selected_port}.")
        else:
            messagebox.showerror("Conexão Serial", f"Falha ao estabelecer conexão na porta {selected_port}.")
    port_combobox.bind("<<ComboboxSelected>>", on_port_selected)

    # Botão para buscar dados e atualizar ID e nome
    def buscar_dados():
        data = get_existing_data(serial_connection_arduino)
        if data:
            nome_dispositivo.set(data['nome'])
            id_var.set(data['id'])
            entry_id.config(state='disabled')
        else:
            messagebox.showinfo("Aviso", "Dados não encontrados ou dispositivo desconectado.")

    buscar_dados_button = ttk.Button(janela_arduino, text="Buscar Dados", command=buscar_dados)
    buscar_dados_button.place(relx=0.99, rely=0.01, anchor='ne')

    # Interface para nome e ID do dispositivo
    label_nome = ttk.Label(container, text="Nome do dispositivo:")
    label_nome.pack(pady=(10, 5))
    entry_nome = ttk.Entry(container, width=40, textvariable=nome_dispositivo)
    entry_nome.pack(pady=(0, 20))

    label_id = ttk.Label(container, text="ID do dispositivo:")
    label_id.pack(pady=(10, 5))
    entry_id = ttk.Entry(container, width=40, textvariable=id_var, state='disabled' if id_var.get() else 'normal')
    entry_id.pack(pady=(0, 20))

    # Botão para voltar à tela principal
    voltar_button = tk.Button(janela_arduino, text="← Voltar", command=lambda: fecha_janela.close_and_return(janela_arduino))
    voltar_button.place(relx=0.01, rely=0.01, anchor='nw')

    janela_arduino.protocol("WM_DELETE_WINDOW", lambda: fecha_janela.close_and_return(janela_arduino))
