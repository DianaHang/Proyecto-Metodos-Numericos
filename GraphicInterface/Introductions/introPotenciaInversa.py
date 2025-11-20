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

from GraphicInterface.ventanaPotenciaInversa import ventanaPotenciaInversa

def introPotenciaInversa(root):
    intro = tk.Toplevel(root)
    intro.title("Introducción - Método de la Potencia Inversa")
    intro.geometry("500x450")

    texto = (
    "Método de la Potencia Inversa\n\n"
    "Este método localiza el valor propio más pequeño en magnitud de una matriz.\n\n"
    "Utiliza la potencia aplicada a la matriz inversa A⁻¹, lo que conduce a la "
    "convergencia hacia el valor propio más cercano a cero.\n\n"
    "Es especialmente útil cuando se necesita encontrar valores propios mínimos.\n\n"
    "Haz clic en CONTINUAR para ejecutar el método."
)


    lbl = tk.Label(intro, text=texto, font=("Arial", 12), justify="left", wraplength=450)
    lbl.pack(pady=20)

    btn_continuar = tk.Button(intro, text="Continuar",
                              font=("Arial", 12),
                              command=lambda: abrirPotenciaInversa(intro))
    btn_continuar.pack(pady=5)

    btn_regresar = tk.Button(intro, text="Regresar al menú",
                             font=("Arial", 12),
                             command=intro.destroy)
    btn_regresar.pack(pady=5)


def abrirPotenciaInversa(intro):
    intro.destroy()  # Cierra la introducción
    ventanaPotenciaInversa() # Abre tu ventana original