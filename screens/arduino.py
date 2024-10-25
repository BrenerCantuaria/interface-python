import tkinter as tk
from .centraliza_tela import center_window
from .config_screens import window_height,window_width

def abrir_janela_arduino(root):
    janela_arduino = tk.Toplevel(root)
    janela_arduino.title("Arduino")
    center_window(janela_arduino, window_width, window_height)
    tk.Label(janela_arduino, text="Arduino").pack()
