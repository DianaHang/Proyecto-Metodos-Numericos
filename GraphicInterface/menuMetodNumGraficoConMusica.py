import sys
import os

# Agregar la carpeta raíz del proyecto al sys.path
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.dirname(ruta_actual)  # Subir un nivel

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

print(">>> Ruta del proyecto agregada:", ruta_proyecto)

import tkinter as tk # módulo estándar de Python para crear interfaces gráficas
from tkinter import Toplevel, messagebox
import math
import os #módulo en Python que contiene funciones para manipular nombres de archivo y rutas de directorios de forma independiente de la plataforma
import pygame #modulo que permite reproducir archivos de sonido en formato .mp3

import Methods.Newton as newton
# ===============================
# FUNCIONES NUMÉRICAS
# ===============================
#Ejemplo de codigo de bisección

def biseccion(fx, a, b, tol, max_iter):
    def f(x):
        return eval(fx, {"x": x, "math": math})

    if f(a) * f(b) >= 0:
        return "No cumple con f(a)*f(b)<0. No hay garantía de raíz en este intervalo."

    iteracion = 0
    while iteracion < max_iter:
        c = (a + b) / 2
        if f(c) == 0 or abs(b - a) < tol:
            return f"✅ Raíz aproximada: x = {c:.6f}\nIteraciones: {iteracion}"

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iteracion += 1
    return f"⚠️ No se encontró raíz en {max_iter} iteraciones.\nÚltimo valor: x = {c:.6f}"

# ===============================
# SUBVENTANA DE BISECCIÓN
# ===============================

def ventana_biseccion():
    sub = Toplevel() # Toplevel() Crea una nueva ventana sobre la principal 
    sub.title("Método de Bisección")
    sub.geometry("400x400")
    sub.minsize(400, 400)

    #Se crea el subtitulo de la ventana tk.Label()
    tk.Label(sub, text="Método de Bisección hola", font=("Arial", 16, "bold")).pack(pady=10) 

    ecuaciones = {
        "1. x³ - x - 2": "x**3 - x - 2",
        "2. eˣ - 3x": "math.exp(x) - 3*x",
        "3. sin(x) - 0.5": "math.sin(x) - 0.5"
    }

    opcion_var = tk.StringVar(sub)
    opcion_var.set(list(ecuaciones.keys())[0])

    tk.Label(sub, text="Selecciona una ecuación:", font=("Arial", 12)).pack(pady=5)
    tk.OptionMenu(sub, opcion_var, *ecuaciones.keys()).pack(pady=5)

    #campos de texto
    entrada_a = tk.Entry(sub, width=10)
    entrada_b = tk.Entry(sub, width=10)
    entrada_tol = tk.Entry(sub, width=10)
    entrada_iter = tk.Entry(sub, width=10)

    for label, entry, val in [ 
        ("Límite inferior (a):", entrada_a, ""),
        ("Límite superior (b):", entrada_b, ""),
        ("Tolerancia:", entrada_tol, "0.0001"),
        ("Iteraciones máximas:", entrada_iter, "50")
    ]:
        tk.Label(sub, text=label).pack()
        entry.insert(0, val)
        entry.pack()

    resultado = tk.Label(sub, text="", font=("Arial", 11), wraplength=350)
    resultado.pack(pady=10)

    def ejecutar_biseccion(): #Funcion que recibe los parametro del metodo bisección 
        try:
            fx = ecuaciones[opcion_var.get()]
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            tol = float(entrada_tol.get())
            max_iter = int(entrada_iter.get())
            salida = biseccion(fx, a, b, tol, max_iter)
            resultado.config(text=salida)
        except Exception as e:
            messagebox.showerror("Error", f"Revisa los datos ingresados.\n{e}")

    tk.Button(sub, text="Calcular", command=ejecutar_biseccion, width=15).pack(pady=10) #botón calcular
    tk.Button(sub, text="Cerrar", command=sub.destroy).pack(pady=5)# botón cerrar


# ===============================
# SUBMENÚS
# ===============================

def submenu_ecuaciones_no_lineales():
    sub = Toplevel() # Toplevel() Crea una nueva ventana sobre la principal 
    sub.title("Ecuaciones no lineales amor y paz") # Titulo de la ventana 
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Bisección", width=20, command=ventana_biseccion).pack(pady=5)
    tk.Button(sub, text="Newton", width=20, command= newton.mainNewton).pack(pady=5)
    tk.Button(sub, text="Secante (próximamente)", width=20).pack(pady=5)


def submenu_sistemas_lineales():
    sub = Toplevel() # Crea una nueva ventana sobre la principal 
    sub.title("Sistemas de ecuaciones lineales")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Gauss Simple (próximamente)", width=20).pack(pady=5)
    tk.Button(sub, text="Gauss-Seidel (próximamente)", width=20).pack(pady=5)
    tk.Button(sub, text="Jacobi (próximamente)", width=20).pack(pady=5)


def submenu_factorizacion_lu():
    sub = Toplevel()
    sub.title("Factorización LU")
    sub.geometry("300x150")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Doolittle (próximamente)", width=20).pack(pady=5)


def submenu_valores_vectores():
    sub = Toplevel()
    sub.title("Valores y vectores propios")
    sub.geometry("300x150")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Método de la Potencia", width=20).pack(pady=5)
    tk.Button(sub, text="Método de la Potencia Invertida", width=20).pack(pady=5)


# ===============================
# INTERFAZ PRINCIPAL
# ===============================

def mostrar_menu(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="MENÚ DE MÉTODOS NUMÉRICOS", font=("Arial", 16, "bold")).pack(pady=15)

    botones = [
        ("Ecuaciones no lineales", submenu_ecuaciones_no_lineales),
        ("Sistemas de ecuaciones lineales", submenu_sistemas_lineales),
        ("Factorización LU", submenu_factorizacion_lu),
        ("Valores y vectores propios", submenu_valores_vectores)
    ]

    for texto, comando in botones:
        tk.Button(root, text=texto, command=comando, width=25, height=2).pack(pady=5)

    tk.Button(root, text="Salir", command=root.quit, width=25, height=2).pack(pady=15)

#Funcion para mostrar la inforimación de la introducción 
def mostrar_introduccion(root):
    for widget in root.winfo_children():
        widget.destroy()

    texto = (
        "Bienvenido al programa de Métodos Numéricos.\n\n"
        "En este software podrás aplicar distintos métodos para resolver:\n"
        "- Ecuaciones no lineales\n"
        "- Sistemas de ecuaciones lineales\n"
        "- Factorización LU\n"
        "- Cálculo de valores y vectores propios\n\n"
        "Presiona 'Continuar' para acceder al menú principal."
    )

    tk.Label(root, text="Introducción", font=("Arial", 16, "bold")).pack(pady=10)
    tk.Message(root, text=texto, width=600, font=("Arial", 12)).pack(expand=True, fill="both", padx=20, pady=10)

    tk.Button(root, text="Continuar", command=lambda: mostrar_menu(root), width=20, height=2).pack(pady=15)


def mostrar_portada(root):
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="MÉTODOS NUMÉRICOS", font=("Arial", 20, "bold")).pack(expand=True)
    tk.Button(root, text="Continuar", command=lambda: mostrar_introduccion(root), width=20, height=2).pack(pady=30)


# ===============================
# MAIN
# ===============================

def main():
    """importante: El módulo os.path se encarga de usar la ruta adecuada según el sistema operativo
    se debe tener: Python instalado, el módulo pygame (pip install pygame) y el archivo de música en el mismo lugar
    """
    # Inicializa pygame para música
    pygame.mixer.init()

    ruta_proyecto = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Construir ruta al archivo de música
    ruta_musica = os.path.join(ruta_proyecto, "Assets", "Rivendell - Howard Shore.mp3")
    
    if os.path.exists(ruta_musica): #si la ruta existe carga y ejecuta la musica en loop
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play(-1) # el valor -1 hace que se reproduzca en loop

    # Se crea la ventana principal (root)
    root = tk.Tk() 
    root.title("Métodos Numéricos")
    root.geometry("700x500")  # Tamaño inicial
    root.minsize(500, 400)

    # Llamada para mostrar la primera pantalla (portada)
    mostrar_portada(root)

    #mantiene la ventana abierta y gestiona los eventos (clics, teclado, etc.)
    root.mainloop()

if __name__ == "__main__":
    main()
