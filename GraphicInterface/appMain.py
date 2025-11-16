import sys
import os

# Rutas para importar Methods (directorio padre)
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.dirname(ruta_actual)
if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

import tkinter as tk
from tkinter import messagebox
import pygame

# Importar ventanas individuales
from .ventanaFalsaPosicion import ventanaFalsaPosicion
from .ventanaNewton import ventanaNewton
from .ventanaSecante import ventanaSecante
from .ventanaGauss import ventanaGauss
from .ventanaJacobi import ventanaJacobi
from .ventanaGaussSeidel import ventanaGaussSeidel
#from .ventanaDoolitle import ventanaDoolitle
#from .ventanaCholesky import ventanaCholesky
#from .ventanaPotencia import ventanaPotencia
#from .ventanaPotenciaInversa import ventanaPotenciaInversa


# ===============================
#            SUBMENÚS
# ===============================

def submenu_ecuaciones_no_lineales():
    sub = tk.Toplevel()
    sub.title("Ecuaciones no lineales")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Falsa Posición", width=20, command= ventanaFalsaPosicion).pack(pady=5)
    tk.Button(sub, text="Newton", width=20, command=ventanaNewton).pack(pady=5)
    tk.Button(sub, text="Secante", width=20, command = ventanaSecante).pack(pady=5)


def submenu_sistemas_lineales():
    sub = tk.Toplevel()
    sub.title("Sistemas lineales")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Gauss", width=20, command = ventanaGauss).pack(pady=5)
    tk.Button(sub, text="Jacobi", width=20, command = ventanaJacobi).pack(pady=5)
    tk.Button(sub, text="Gauss-Seidel", width=20, command = ventanaGaussSeidel).pack(pady=5)

def submenu_factorizacion_lu():
    sub = tk.Toplevel()
    sub.title("Factorización LU")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    #tk.Button(sub, text="Doolittle", width=20, command= ventanaDoolitle).pack(pady=5)
    #tk.Button(sub, text="Cholesky", width=20, command= ventanaCholesky).pack(pady=5)

def submenu_valores_vectores():
    sub = tk.Toplevel()
    sub.title("Valores y vectores propios")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    #tk.Button(sub, text="Método de la Potencia", width=20, command= ventanaPotencia).pack(pady=5)
    #tk.Button(sub, text="Método de la Potencia Inversa", width=20, command= ventanaPotenciaInversa).pack(pady=5)

# ===============================
#          MENÚ PRINCIPAL
# ===============================

def mostrar_menu(root):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text="MENÚ DE MÉTODOS NUMÉRICOS",
             font=("Arial", 16, "bold")).pack(pady=15)

    botones = [
        ("Ecuaciones no lineales", submenu_ecuaciones_no_lineales),
        ("Sistemas de ecuaciones lineales", submenu_sistemas_lineales),
        ("Factorización LU", submenu_factorizacion_lu),
        ("Valores y vectores propios", submenu_valores_vectores)
    ]

    # Crear botones para cada opción
    for texto, comando in botones:
        tk.Button(root, text=texto, width=25, height=2,
                  command=comando).pack(pady=5)

    tk.Button(root, text="Salir", width=25, height=2,
              command=lambda: pantalla_final(root)).pack(pady=15)


# ===============================
#   PANTALLAS DE PRESENTACIÓN
# ===============================

def mostrar_introduccion(root):
    for w in root.winfo_children():
        w.destroy() # Limpia la ventana principal

    texto = (
        "Bienvenido al programa de Métodos Numéricos.\n\n"
        "En este software podrás aplicar distintos métodos para resolver:\n"
        "- Ecuaciones no lineales.\n"
        "- Sistemas de ecuaciones lineales.\n"
        "- Factorización LU.\n"
        "- Cálculo de valores y vectores propios.\n\n"
        "Presiona 'Continuar' para acceder al menú principal."
    )

    tk.Label(root, text="Introducción",
             font=("Arial", 16, "bold")).pack(pady=10)
    tk.Message(root, text=texto, width=600, font=("Arial", 12)).pack(expand=True, fill="both", padx=20, pady=10)

    tk.Button(root, text="Continuar", width=20, height=2,
              command=lambda: mostrar_menu(root)).pack(pady=15)


def mostrar_portada(root):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text="MÉTODOS NUMÉRICOS",
             font=("Arial", 20, "bold")).pack(expand=True)

    tk.Button(root, text="Continuar", width=20,
              height=2, command=lambda: mostrar_introduccion(root)).pack(pady=30)

#Funcion para mostrar las introducciones
def mostrar_ventana_intro(root, titulo, texto, accion_continuar):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text=titulo, font=("Arial", 18, "bold")).pack(pady=15)
    tk.Message(root, text=texto, width=600, font=("Arial", 12)).pack(
        expand=True, fill="both", padx=20, pady=10
    )

    tk.Button(root, text="Continuar", width=20, height=2,
              command=accion_continuar).pack(pady=20)

#Funcion para mostrar la pantalla final (agradecimientos) 
def pantalla_final(root):
    mostrar_ventana_intro(
        root,
        "¡Gracias por usar el sistema!\n",
        "Este software fue desarrollado por estudiantes de MAC.\n"
        "\tDerechos reservados UNAM.©\n\n"
        "\n\n"
        "Cierra la ventana para salir o presiona 'Continuar'",
        lambda: root.quit()
    )

# ===============================
#             MAIN
# ===============================

def main():
    #Inicializar pygame para la música de fondo
    pygame.mixer.init()
    ruta_musica = os.path.join(ruta_proyecto, "Assets",     "Rivendell - Howard Shore.mp3")

    if os.path.exists(ruta_musica):
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play(-1) #Reproducir en bucle

    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Métodos Numéricos")
    root.geometry("700x500")
    root.minsize(500, 400)

    mostrar_portada(root)
    root.mainloop()