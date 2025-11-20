import sys
import os
### Ajustar ruta para importar módulos del proyecto
ruta_actual = os.path.dirname(os.path.abspath(__file__))          # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)                      # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

"""##################################################
"""
#librerías
import tkinter as tk
from tkinter import messagebox
import numpy as np
from Methods.Doolittle import doolittle


def ventanaDoolittle():
    sub = tk.Toplevel()
    sub.title("Método LU – Doolittle")
    sub.geometry("600x600")

    tk.Label(sub, text="Método LU – Doolittle",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Ingrese el tamaño de la matriz (nxn): ", font=("Arial", 12)).pack()
    entrada_n = tk.Entry(sub, width=5, font=("Arial", 12))
    entrada_n.pack()

    frame_matriz = tk.Frame(sub)
    frame_vector = tk.Frame(sub)

    entradas_A = []
    entradas_b = []

    # Crear entradas dinámicas
    def crear_matriz():
        nonlocal entradas_A, entradas_b

        # Limpiar posibles widgets anteriores
        for w in frame_matriz.winfo_children(): w.destroy()
        for w in frame_vector.winfo_children(): w.destroy()

        entradas_A = []
        entradas_b = []

        try:
            n = int(entrada_n.get())
            if n < 2:
                raise ValueError("n debe ser mayor o igual a 2")
        except:
            messagebox.showerror("Error", "Ingresa un entero válido para n.")
            return

        tk.Label(sub, text=f"Ingrese los valores de la matriz A ({n} × {n}):", font=("Arial", 12)).pack(pady=5)
        frame_matriz.pack(pady=5)

        # Crear campos de entrada para la matriz A y el vector b
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame_matriz, width=6, font=("Arial", 12))
                e.grid(row=i, column=j, padx=3, pady=3)
                fila.append(e)
            entradas_A.append(fila)

        tk.Label(sub, text=f"Ingrese el vector b ({n} x 1):", font=("Arial", 12)).pack(pady=5)
        frame_vector.pack()

        for i in range(n):
            e = tk.Entry(frame_vector, width=6, font=("Arial", 12))
            e.grid(row=i, column=0, pady=3)
            entradas_b.append(e)

        btn_resolver.pack(pady=15)

    #Botón para crear matriz
    tk.Button(sub, text="Crear matriz",  font=("Arial", 12), command=crear_matriz).pack(pady=10)

    # Ejecutar Doolittle
    def resolver_doolittle():
        try:
            n = int(entrada_n.get())

            A = np.zeros((n, n))
            b = np.zeros(n)

            # Obtener valores de las entradas
            for i in range(n):
                for j in range(n):
                    A[i][j] = float(entradas_A[i][j].get())

            for i in range(n):
                b[i] = float(entradas_b[i].get())

            # Ejecutar el método de Doolittle
            L, U, v, x = doolittle(A, b)

            # Mostrar resultados
            texto = "RESULTADOS DEL MÉTODO DOOLITTLE\n\n"

            texto += "Matriz L (inferior):\n"
            texto += str(L) + "\n\n"

            texto += "Matriz U (superior):\n"
            texto += str(U) + "\n\n"

            texto += "Vector intermedio v (Lv = b):\n"
            texto += str(v) + "\n\n"

            texto += "Solución final (x):\n"
            for i, val in enumerate(x):
                texto += f"x{i+1} = {val:.6f}\n"

            texto += "\nComprobación A·x:\n"
            texto += str(A @ x)

            messagebox.showinfo("Resultados", texto)

        except Exception:
            messagebox.showerror("Error: Se ingresó un valor inesperado. Revise las entradas.")

    btn_resolver = tk.Button(sub, text="Resolver sistema",
                             font=("Arial", 12),
                             command=resolver_doolittle)
    btn_resolver.pack_forget()