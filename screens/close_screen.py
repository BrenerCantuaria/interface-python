import tkinter as tk
from tkinter import messagebox

class CloseScreen:
    def __init__(self, root):
        self.root = root  # Armazena uma referência à janela principal

    def close_window(self, window):
        """
        Fecha a janela especificada e opcionalmente realiza outras ações.
        """
        window.destroy()  # Destroi a janela passada como argumento

    def confirm_and_close_window(self, window, message="Deseja realmente fechar?"):
        """
        Exibe uma caixa de diálogo de confirmação antes de fechar a janela.
        """
        if messagebox.askyesno("Confirmar", message):
            self.close_window(window)  # Fecha a janela se o usuário confirmar

    def close_and_return(self, window):
        """
        Fecha a janela atual e retorna para a tela principal.
        """
        self.close_window(window)
        self.root.deiconify()  # Traz a janela principal de volta ao foco
