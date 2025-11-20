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

from GraphicInterface.ventanaPotencia import ventanaPotencia


def introPotencia(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de la Potencia")
    intro.geometry("500x450")

    texto = (
    "Método de la Potencia\n\n"
    "Este método calcula el valor propio dominante (el mayor en magnitud) "
    "de una matriz, junto con su vector propio asociado.\n\n"
    "Funciona multiplicando repetidamente un vector inicial por la matriz, "
    "normalizándolo en cada iteración.\n\n"
    "Es sencillo, rápido y útil para matrices grandes y dispersas.\n\n"
    "Presiona CONTINUAR para aplicar el método de la potencia."
)


    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirPotencia(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirPotencia(intro):
    intro.destroy()  # Cierra la introducción
    ventanaPotencia() # Abre tu ventana original