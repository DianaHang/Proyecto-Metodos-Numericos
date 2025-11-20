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

from GraphicInterface.ventanaSecante import ventanaSecante


def introSecante(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de la Secante")
    intro.geometry("500x450")

    texto = (
    "Método de la Secante\n\n"
    "Este método también busca aproximar raíces de ecuaciones no lineales, "
    "pero a diferencia del método de Newton, *no requiere derivada*.\n\n"
    "Utiliza dos valores iniciales para trazar una recta secante y obtener "
    "una aproximación a la raíz.\n\n"
    "Su fórmula es:\n\n"
    " x(n+1) = x(n) - f(x(n)) * (x(n) - x(n-1)) / (f(x(n)) - f(x(n-1)))\n\n"
    "Es más rápido que los métodos de intervalo y una alternativa práctica "
    "cuando la derivada es difícil de calcular.\n\n"
    "Presiona CONTINUAR para usar el método."
)


    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirSecante(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirSecante(intro):
    intro.destroy()  # Cierra la introducción
    ventanaSecante()  # Abre tu ventana original