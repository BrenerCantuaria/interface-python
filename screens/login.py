import tkinter as tk
from tkinter import Label, Entry, Button
from .centraliza_tela import center_window
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style
import ttkbootstrap as ttkb
import keyboard as kb

def login(email, senha):
    return email == "admin" and senha == "admin"

def criar_tela_login(root):
    janela_login = ttkb.Toplevel(root)
    janela_login.title("Tela de Login")
    center_window(janela_login, 600, 400)
    janela_login.resizable(False, False)

    container = ttk.Frame(janela_login)
    container.place(relx=0.5, rely=0.5, anchor='center')

    label_email = ttk.Label(container, text="E-mail: admin", font=("Helvetica", 14))
    label_email.pack(pady=(10, 0))
    entry_email = ttk.Entry(container, width=30, font=("Helvetica", 14))
    entry_email.pack(pady=(0, 10))

    label_senha = ttk.Label(container, text="Senha: admin", font=("Helvetica", 14))
    label_senha.pack(pady=(10, 0))
    entry_senha = ttk.Entry(container, show="*", width=30, font=("Helvetica", 14))
    entry_senha.pack(pady=(0, 10))

    kb.on_press_key("enter", lambda _: handle_login())

    def handle_login():
        if login(entry_email.get(), entry_senha.get()):
            janela_login.destroy()
            root.deiconify()  # Show the main root window
        else:
            Label(janela_login, text="Login falhou! Tente novamente.", fg="red").pack()

    botao_login = ttk.Button(container, text="Login", command=handle_login, bootstyle=(PRIMARY))
    botao_login.pack(pady=10)