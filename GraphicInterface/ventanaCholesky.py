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
import numpy as np

from Methods.Cholesky import cholesky
from Methods.inputsMatriz import diagonalDominante as reacomodarFilas


def ventanaCholesky():
    sub = tk.Toplevel()
    sub.title("Método de Cholesky")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de Cholesky",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Ingrese el tamaño de la matriz (nxn):",
             font=("Arial", 12)).pack()
    
    entrada_n = tk.Entry(sub, width=5 , font=("Arial", 12))
    entrada_n.pack()

    frame_matriz = tk.Frame(sub)
    frame_vector = tk.Frame(sub)

    entradas_A = []
    entradas_b = []

    # CREAR CAMPOS DINÁMICOS A y b
    def crear_matriz():
        nonlocal entradas_A, entradas_b

        # Limpiar posibles widgets anteriores
        for w in frame_matriz.winfo_children(): w.destroy()
        for w in frame_vector.winfo_children(): w.destroy()

        entradas_A = []
        entradas_b = []

        try:
            n = int(entrada_n.get())
            if n < 2: raise ValueError("n debe ser mayor o igual a 2")
        except:
            messagebox.showerror("Error", "Ingresa un entero válido para n (n ≥ 2).")
            return

        tk.Label(sub, text=f"Ingrese los valores de la matriz A ({n} × {n}):", font=("Arial", 12)).pack(pady=5)
        frame_matriz.pack(pady=5)

        #Crear campos A
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame_matriz, width=6, font=("Arial", 12))
                e.grid(row=i, column=j, padx=3, pady=3)
                fila.append(e)
            entradas_A.append(fila)

        tk.Label(sub, text=f"Ingrese el vector b ({n} x 1):", font=("Arial", 12)).pack(pady=5)
        frame_vector.pack()

        #Crear campos b
        for i in range(n):
            e = tk.Entry(frame_vector, width=6, font=("Arial", 12))
            e.grid(row=i, column=0, pady=3)
            entradas_b.append(e)

        btn_resolver.pack(pady=15)

    #Botón para crear campos
    tk.Button(sub, text="Crear matriz", font=("Arial",12), command=crear_matriz).pack(pady=10)

    # VALIDACIONES Y EJECUCIÓN DEL MÉTODO
    def resolver_cholesky():
        try:
            n = int(entrada_n.get())

            # Leer matriz A
            A = np.zeros((n, n))
            b = np.zeros(n)

            for i in range(n):
                for j in range(n):
                    A[i][j] = float(entradas_A[i][j].get())

            for i in range(n):
                b[i] = float(entradas_b[i].get())

            # -------------------- SIMETRÍA --------------------
            if not np.allclose(A, A.T):
                messagebox.showwarning(
                    "Advertencia",
                    "La matriz NO es simétrica.\nIntentando reordenar filas..."
                )

                A2, b2 = reacomodarFilas(A, b)

                if A2 is None:
                    messagebox.showerror(
                        "Error",
                        "La matriz no es simétrica y no pudo reacomodarse.\n"
                        "Cholesky NO puede aplicarse."
                    )
                    return

                A, b = A2, b2

                if not np.allclose(A, A.T):
                    messagebox.showerror(
                        "Error",
                        "Incluso después de reacomodar, la matriz no es simétrica.\n"
                        "Cholesky no puede aplicarse."
                    )
                    return

                messagebox.showinfo(
                    "Reordenación exitosa",
                    "La matriz ha sido reacomodada y ahora es simétrica."
                )

            # -------------------- DEFINIDA POSITIVA --------------------
            x_test = np.ones(n)  # vector genérico distinto cero
            # Evaluar xᵀ·A·x con multiplicaciones de matrices
            val = x_test.T @ A @ x_test

            if val <= 0:
                messagebox.showerror(
                    "Error",
                    "La matriz NO es definida positiva.\n"
                    f"xᵀ·A·x = {val:.6f} ≤ 0.\n"
                    "Cholesky NO puede aplicarse."
                )
                return

            # -------------------- EJECUTAR CHOLESKY --------------------
            L, Lt, v, x = cholesky(A, b)

            # Mostrar resultados
            texto = "RESULTADOS DEL MÉTODO DE CHOLESKY\n\n"

            texto += "Matriz L:\n"
            texto += str(L) + "\n\n"

            texto += "Matriz Lᵀ:\n"
            texto += str(Lt) + "\n\n"

            texto += "Vector v (Lv = b):\n"
            texto += str(v) + "\n\n"

            texto += "Solución x (Lᵀ·x = v):\n"
            for i, valx in enumerate(x):
                texto += f"x{i+1} = {valx:.6f}\n"

            texto += "\nComprobación: A·x = \n"
            texto += str(A @ x)

            messagebox.showinfo("Resultados", texto)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

    btn_resolver = tk.Button(sub, text="Resolver sistema", font=("Arial", 12), command=resolver_cholesky)
    btn_resolver.pack_forget()  # Oculto hasta crear la matriz