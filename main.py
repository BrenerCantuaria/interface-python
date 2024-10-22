import tkinter as tk
from tkinter import Toplevel, PhotoImage, Button,Label,Entry
import random

window_width = 800
window_height = 600


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = int((screen_width - width) / 2)
    y = int((screen_height - height) / 2)
    window.geometry(f"{width}x{height}+{x}+{y}")


def login(email, senha):
    if email == "user@example.com" and senha == "password123":
        return True
    return False

def criar_tela_login():
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
            root.deiconify()  # Mostra a janela principal após o login
        else:
            Label(janela_login, text="Login falhou! Tente novamente.", fg="red").pack()

    botao_login = Button(janela_login, text="Login", command=handle_login)
    botao_login.pack(pady=10)

def abrir_janela_esp32():
    janela_esp32 = Toplevel(root)
    janela_esp32.title("ESP32")
    center_window(janela_esp32, window_width, window_height)
    tk.Label(janela_esp32, text="TELA ESP32").pack()
    manage_esp32_id(janela_esp32)

def manage_esp32_id(window):
    esp32_id = None

    def generate_id():
        nonlocal esp32_id
        esp32_id = f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(100,999)}"
        id_label.config(text=f"ID: {esp32_id}")
        generate_button.pack_forget()
        save_button.pack(side="top", pady=10)

    def save_id():
        # Simula a gravação do ID na ESP32
        confirm_button.pack(side="top", pady=10)

    def confirm():
        confirm_label = Label(window, text="ID gravado com sucesso!")
        confirm_label.pack(side="top", pady=10)
        save_button.pack_forget()
        confirm_button.pack_forget()

     # Centralizando o texto
    id_label = Label(window, text="", font=('Helvetica', 14), width=40, height=2)
    id_label.pack(side="top", fill='x', pady=20)

    generate_button = Button(window, text="Gerar ID para ESP32", command=generate_id, font=('Helvetica', 12))
    save_button = Button(window, text="Gravar na ESP32", command=save_id, font=('Helvetica', 12))
    confirm_button = Button(window, text="Confirmar", command=confirm, font=('Helvetica', 12))
    confirm_label = Label(window, text="", font=('Helvetica', 14), width=40, height=2)
    confirm_label.pack(side="top", fill='x', pady=10)

    if esp32_id:
        id_label.config(text=f"ID: {esp32_id}")
    else:
        generate_button.pack(side="top", pady=10)

def abrir_janela_arduino():
    janela_arduino = Toplevel(root)
    janela_arduino.title("Arduino")
    center_window(janela_arduino, window_width, window_height)
    tk.Label(janela_arduino, text="Arduino").pack()


def abrir_janela_perfil():
    janela_perfil = Toplevel(root)
    janela_perfil.title("Perfil")
    center_window(janela_perfil, window_width, window_height)
    tk.Label(janela_perfil, text="Perfil do Usuário").pack()


root = tk.Tk()
root.title("Tela Principal")
center_window(root, window_width, window_height)
root.withdraw()

criar_tela_login()
button_frame = tk.Frame(root)
button_frame.pack(expand=True)

original_icon1 = PhotoImage(file='img\esp32.png')
original_icon2 = PhotoImage(file='img\Arduino.png')
original_icon3 = PhotoImage(file='img\perfil.png')

register_icon = original_icon1.subsample(4, 4)
arduino_icon = original_icon2.subsample(4, 4)
profile_icon = original_icon3.subsample(4, 4)


esp32_button = Button(button_frame, image=register_icon, command=lambda: abrir_janela_esp32())
esp32_button.pack(side="left", padx=50)

arduino_button = Button(button_frame, image=arduino_icon, command=lambda: abrir_janela_arduino())
arduino_button.pack(side="left", padx=50)

perfil_button = Button(button_frame, image=profile_icon, command=lambda: abrir_janela_perfil())
perfil_button.pack(side="left", padx=50)




root.mainloop()
