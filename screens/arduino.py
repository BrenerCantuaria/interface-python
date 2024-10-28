# import tkinter as tk
# from .centraliza_tela import center_window
# from .config_screens import window_height,window_width

# def abrir_janela_arduino(root):
#     janela_arduino = tk.Toplevel(root)
#     janela_arduino.title("Arduino")
#     center_window(janela_arduino, window_width, window_height)
#     tk.Label(janela_arduino, text="Arduino").pack()
import tkinter as tk
from tkinter import ttk
from .centraliza_tela import center_window
from .config_screens import window_height, window_width

# Essa função deve fazer uma conexão com FireBase 
# Retorna as lista de ESP32 cadastrados
def get_dispositivos_eps32():
    return ["ESP32 Dev Kit", "ESP32 WROOM", "ESP32 WROVER"]

def abrir_janela_arduino(root):
    janela_arduino = tk.Toplevel(root)
    janela_arduino.title("Arduino")
    center_window(janela_arduino, window_width, window_height)
    janela_arduino.resizable(False, False)

    # Container principal para os widgets
    container = ttk.Frame(janela_arduino)
    container.pack(padx=20, pady=20, fill='both', expand=True)

    dispositivos = get_dispositivos_eps32()

    # Combobox para selecionar dispositivos ESP32
    label_dispositivo = ttk.Label(container, text="Selecione o dispositivo ESP32:")
    label_dispositivo.pack(pady=(10, 5))

    if dispositivos:
        # Se há dispositivos, mostra o combobox
        combobox_dispositivo = ttk.Combobox(container, values=dispositivos)
        combobox_dispositivo.pack(pady=(0, 20))
        combobox_dispositivo.current(0)  # Seleciona o primeiro dispositivo por padrão
    else:
        # Se não há dispositivos, mostra mensagem de aviso
        label_no_device = ttk.Label(container, text="Não existe nenhum dispositivo ESP32 cadastrado", font=("Helvetica", 14))
        label_no_device.pack(pady=(10, 5))

    # Campo para nome do dispositivo
    label_nome = ttk.Label(container, text="Nome do dispositivo:")
    label_nome.pack(pady=(10, 5))

    entry_nome = ttk.Entry(container, width=40)
    entry_nome.pack(pady=(0, 20))

    # Campo para ID do dispositivo
    label_id = ttk.Label(container, text="ID do dispositivo:")
    label_id.pack(pady=(10, 5))

    entry_id = ttk.Entry(container, width=40)
    entry_id.pack(pady=(0, 20))

    # Botões para ações adicionais, se necessário
    btn_acionar = ttk.Button(container, text="Acionar Dispositivo")
    btn_acionar.pack(pady=(20, 0))