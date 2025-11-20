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

from GraphicInterface.ventanaGauss import ventanaGauss


def introGauss(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Gauss")
    intro.geometry("500x450")

    texto = (
    "Método de Eliminación de Gauss\n\n"
    "Este método se utiliza para resolver sistemas de ecuaciones lineales "
    "mediante la transformación del sistema en uno equivalente de forma "
    "triangular.\n\n"
    "Consiste en aplicar operaciones elementales a las filas de la matriz "
    "para obtener un sistema más simple que puede resolverse por sustitución "
    "hacia atrás.\n\n"
    "Es uno de los métodos fundamentales del álgebra lineal computacional.\n\n"
    "Haz clic en CONTINUAR para resolver un sistema utilizando este método."
)


    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirGauss(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirGauss(intro):
    intro.destroy()  # Cierra la introducción
    ventanaGauss()  # Abre tu ventana original