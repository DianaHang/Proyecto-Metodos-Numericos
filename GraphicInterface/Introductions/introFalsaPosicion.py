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

from GraphicInterface.ventanaFalsaPosicion import ventanaFalsaPosicion


def introFalsaPosicion(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Falsa Posicion")
    intro.geometry("500x450")

    texto = (
    "Método de Falsa Posición (Regula Falsi)\n\n"
    "Este método pertenece a la familia de métodos de búsqueda de raíces "
    "que utilizan intervalos donde la función cambia de signo.\n\n"
    "A diferencia del método de bisección, la Falsa Posición traza una "
    "línea secante entre los puntos del intervalo y usa la intersección "
    "con el eje X como la siguiente aproximación.\n\n"
    "Es más rápido que la bisección y garantiza la convergencia cuando "
    "la función cumple la condición de cambio de signo.\n\n"
    "Haz clic en CONTINUAR para utilizar el método."
)


    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirFalsaPosicion(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirFalsaPosicion(intro):
    intro.destroy()  # Cierra la introducción
    ventanaFalsaPosicion()  # Abre tu ventana original