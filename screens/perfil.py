import tkinter as tk
from tkinter import ttk, messagebox
from .centraliza_tela import center_window

def abrir_janela_perfil(root):
    janela_perfil = tk.Toplevel(root)
    janela_perfil.title("Perfil do Usuário")
    center_window(janela_perfil, 800, 600)
    janela_perfil.resizable(False, False)

    usuario_nome = tk.StringVar(value="Nome do Usuário")
    usuario_email = tk.StringVar(value="email@exemplo.com")

    container = ttk.Frame(janela_perfil)
    container.pack(expand=True)

    ttk.Label(container, text="Perfil do Usuário", font=('Helvetica', 18, 'bold')).pack(pady=20)

    ttk.Label(container, text="Nome:", font=('Helvetica', 14)).pack(pady=(10, 0))
    entry_nome = ttk.Entry(container, font=('Helvetica', 14), state='normal')
    entry_nome.insert(0, usuario_nome.get())
    entry_nome.config(state='readonly')
    entry_nome.pack(pady=(0, 20))

    ttk.Label(container, text="Email:", font=('Helvetica', 14)).pack(pady=(10, 0))
    entry_email = ttk.Entry(container, font=('Helvetica', 14), state='normal')
    entry_email.insert(0, usuario_email.get())
    entry_email.config(state='readonly')
    entry_email.pack(pady=(0, 20))

    ttk.Button(container, text="Encerrar Sessão", command=lambda: [root.deiconify(), janela_perfil.destroy()]).pack(pady=30)

    janela_perfil.grab_set()
