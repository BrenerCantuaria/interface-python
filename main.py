import tkinter as tk
from screens.login import criar_tela_login
from screens.esp32 import abrir_janela_esp32
from screens.arduino import abrir_janela_arduino
from screens.perfil import abrir_janela_perfil
from screens.centraliza_tela import center_window
from screens.config_screens import window_height,window_width
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.style import Style


root = tk.Tk()
root.title("Tela Principal")
center_window(root, window_width, window_height)
root.withdraw()
style = Style(theme="superhero")

criar_tela_login(root)  # Start the application with the login screen

button_frame = tk.Frame(root)
button_frame.pack(expand=True)


original_icon1 = tk.PhotoImage(file='img\esp32.png')
original_icon2 = tk.PhotoImage(file='img\Arduino.png')
original_icon3 = tk.PhotoImage(file='img\perfil.png')

register_icon = original_icon1.subsample(4, 4)
arduino_icon = original_icon2.subsample(4, 4)
profile_icon = original_icon3.subsample(4, 4)


esp32_button = ttk.Button(button_frame, image=register_icon, command=lambda: abrir_janela_esp32(root), bootstyle="secondary-outline")
esp32_button.pack(side="left", padx=50)

arduino_button = ttk.Button(button_frame, image=arduino_icon, command=lambda: abrir_janela_arduino(root), bootstyle="secondary-outline")
arduino_button.pack(side="left", padx=50)

perfil_button = ttk.Button(button_frame, image=profile_icon, command=lambda: abrir_janela_perfil(root), bootstyle="secondary-outline")
perfil_button.pack(side="left", padx=50)


root.mainloop()
