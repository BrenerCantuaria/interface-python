import tkinter as tk
from tkinter import ttk, messagebox

from screens.close_screen import CloseScreen
from .centraliza_tela import center_window
from .config_screens import window_height, window_width
from service.serial import open_serial_connection, get_existing_data

def get_dispositivos_eps32():
    return ["ESP32 Dev Kit", "ESP32 WROOM", "ESP32 WROVER"]

def abrir_janela_arduino(root):
    root.withdraw()
    janela_arduino = tk.Toplevel(root)
    janela_arduino.title("Arduino")
    center_window(janela_arduino, window_width, window_height)
    janela_arduino.resizable(False,False)
    janela_arduino.grab_set()
    janela_arduino.resizable(False, False)
    fecha_janela = CloseScreen(root=root)

    
    # Container principal para os widgets
    container = ttk.Frame(janela_arduino)
    container.pack(padx=20, pady=20, fill='both', expand=True)

    dispositivos = get_dispositivos_eps32()

    # Combobox para selecionar dispositivos ESP32
    label_dispositivo = ttk.Label(container, text="Selecione o dispositivo ESP32:")
    label_dispositivo.pack(pady=(10, 5))

    if dispositivos:
        combobox_dispositivo = ttk.Combobox(container, values=dispositivos,state="readonly")
        combobox_dispositivo.pack(pady=(0, 20))
        combobox_dispositivo.current(0)  # Seleciona o primeiro dispositivo por padrão
    else:
        label_no_device = ttk.Label(container, text="Não existe nenhum dispositivo ESP32 cadastrado", font=("Helvetica", 14))
        label_no_device.pack(pady=(10, 5))

       # Combobox para seleção de porta serial
    label_port = ttk.Label(container, text="Selecione a porta serial:")
    label_port.pack(pady=(10, 0))
    port_combobox = ttk.Combobox(container, width=37, values=['COM3', 'COM4', 'COM5'],state="readonly")
    port_combobox.pack(pady=10)
    port_combobox.set('COM3')  # Define a porta padrão


    label_nome = ttk.Label(container, text="Nome do dispositivo:")
    label_nome.pack(pady=(10, 5))
    entry_nome = ttk.Entry(container, width=40)
    entry_nome.pack(pady=(0, 20))

    label_id = ttk.Label(container, text="ID do dispositivo:")
    label_id.pack(pady=(10, 5))
    entry_id = ttk.Entry(container, width=40)
    entry_id.pack(pady=(0, 20))

 

    # Gerencia a abertura da conexão serial ao mudar de porta
    def on_port_selected(event):
        selected_port = port_combobox.get()
        serial_connection, success = open_serial_connection(selected_port)
        if success:
            messagebox.showinfo("Conexão Serial", f"Conexão estabelecida com sucesso na porta {selected_port}.")
        else:
            messagebox.showerror("Conexão Serial", f"Falha ao estabelecer conexão na porta {selected_port}.")
    port_combobox.bind("<<ComboboxSelected>>", on_port_selected)

    btn_acionar = ttk.Button(container, text="Acionar Dispositivo")
    btn_acionar.pack(pady=(20, 0))


     # Fechamento da tela
    voltar_button = tk.Button(janela_arduino, text="← Voltar",  command=lambda: fecha_janela.close_and_return(janela_arduino))
    voltar_button.place(x=10, y=10)
    janela_arduino.protocol("WM_DELETE_WINDOW", lambda: fecha_janela.close_and_return(janela_arduino))  # Garante o fechamento correto
