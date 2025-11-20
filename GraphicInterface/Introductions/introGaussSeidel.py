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

from GraphicInterface.ventanaGaussSeidel import ventanaGaussSeidel


def introGaussSeidel(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de Gauss-Seidel")
    intro.geometry("500x450")

    texto = (
    "Método Iterativo de Gauss-Seidel\n\n"
    "Este método es una mejora del método de Jacobi, pues utiliza los valores "
    "ya actualizados dentro de la misma iteración para acelerar la convergencia.\n\n"
    "Es especialmente útil en sistemas grandes y es más rápido que Jacobi en "
    "la mayoría de los casos.\n\n"
    "Se recomienda usar matrices diagonalmente dominantes para garantizar su "
    "estabilidad.\n\n"
    "Presiona CONTINUAR para aplicar el método."
)



    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirGaussSeidel(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirGaussSeidel(intro):
    intro.destroy()  # Cierra la introducción
    ventanaGaussSeidel()  # Abre tu ventana original