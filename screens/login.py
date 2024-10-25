import tkinter as tk
from tkinter import Label, Entry, Button
from .centraliza_tela import center_window



def login(email, senha):
    return email == "user" and senha == "123"

def criar_tela_login(root):
    janela_login = tk.Toplevel(root)
    janela_login.title("Tela de Login")
    center_window(janela_login, 300, 200)

    label_email = Label(janela_login, text="E-mail:")
    label_email.pack(pady=(10, 0))
    entry_email = Entry(janela_login, width=30)
    entry_email.pack(pady=(0, 10))

    label_senha = Label(janela_login, text="Senha:")
    label_senha.pack(pady=(10, 0))
    entry_senha = Entry(janela_login, show="*", width=30)
    entry_senha.pack(pady=(0, 10))



    def handle_login():
        if login(entry_email.get(), entry_senha.get()):
            janela_login.destroy()
            root.deiconify()
        else:
            Label(janela_login, text="Login falhou! Tente novamente.", fg="red").pack()

    botao_login = Button(janela_login, text="Login", command=handle_login)
    botao_login.pack(pady=10)
