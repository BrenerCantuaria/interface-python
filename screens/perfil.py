import tkinter as tk
from .centraliza_tela import center_window

def abrir_janela_perfil(root):
    janela_perfil = tk.Toplevel(root)
    janela_perfil.title("Perfil")
    center_window(janela_perfil, 800, 600)
    tk.Label(janela_perfil, text="Perfil do Usuário").pack()
