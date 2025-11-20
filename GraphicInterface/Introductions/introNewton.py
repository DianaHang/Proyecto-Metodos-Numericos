import sys
import os
### Ajustar ruta para importar módulos del proyecto
ruta_actual = os.path.dirname(os.path.abspath(__file__))          # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)                      # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

"""##################################################
"""
#Librerías
import tkinter as tk
from tkinter import messagebox

from GraphicInterface.ventanaNewton import ventanaNewton  


def introNewton(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Newton")
    intro.geometry("500x450")

    texto = (
        "Método de Newton\n\n"
        "Este método numérico sirve para encontrar raíces de ecuaciones "
        "no lineales utilizando aproximaciones sucesivas mediante derivadas.\n\n"
        "La fórmula principal es:\n\n"
        "        x(n+1) = x(n) - f(x) / f'(x)\n\n"
        "Es un método rápido siempre que la aproximación inicial esté cerca "
        "de la raíz.\n\n"
        "Haz clic en CONTINUAR para ir a la ventana del método."
    )

    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirNewton(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirNewton(intro):
    intro.destroy()  # Cierra la introducción
    ventanaNewton()  # Abre tu ventana original