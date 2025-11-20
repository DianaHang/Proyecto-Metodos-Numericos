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
from Methods.Jacobi import jacobi
from Methods.inputsMatriz import diagonalDominante


def ventanaJacobi():
    sub = tk.Toplevel()
    sub.title("Método de Jacobi")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de Jacobi",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Ingrese el tamaño de la matriz (nxn):",
             font=("Arial", 12)).pack()

    entrada_n = tk.Entry(sub, width=5, font=("Arial", 12))
    entrada_n.pack()

    frame_matriz = tk.Frame(sub)
    frame_vector = tk.Frame(sub)

    entradas_A = []
    entradas_b = []

    # Crear matriz dinámica
    def crear_matriz():
        nonlocal entradas_A, entradas_b

        # Limpiar posibles widgets anteriores
        for w in frame_matriz.winfo_children():
            w.destroy()
        for w in frame_vector.winfo_children():
            w.destroy()

        entradas_A = []
        entradas_b = []

        try:
            n = int(entrada_n.get())
            if n < 2:
                raise ValueError("n debe ser mayor o igual a 2")
        except:
            messagebox.showerror("Error", "Ingresa un valor entero válido para n.")
            return

        tk.Label(sub, text=f"Ingrese los valores de la matriz A ({n} × {n}):",
                 font=("Arial", 12)).pack(pady=5)
        frame_matriz.pack(pady=5)

        # Crear campos A
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame_matriz, width=6, font=("Arial", 12))
                e.grid(row=i, column=j, padx=3, pady=3)
                fila.append(e)
            entradas_A.append(fila)

        tk.Label(sub, text=f"Ingrese el vector b ({n} x 1):",
                 font=("Arial", 12)).pack(pady=5)
        frame_vector.pack()

        # Crear campos b
        for i in range(n):
            e = tk.Entry(frame_vector, width=6, font=("Arial", 12))
            e.grid(row=i, column=0, pady=3)
            entradas_b.append(e)

        btn_resolver.pack(pady=15)

    # Botón para generar matriz
    tk.Button(sub, text="Crear matriz", font=("Arial", 12),
              command=crear_matriz).pack(pady=10)   

    # Entrada número de iteraciones
    tk.Label(sub, text="Número de iteraciones:", font=("Arial", 12)).pack()
    entrada_iter = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_iter.insert(0, "")
    entrada_iter.pack()

    # Resolver Jacobi
    def resolver_jacobi():
        try:
            n = int(entrada_n.get())
            numIterStr = entrada_iter.get()

            try:
                numIter = int(numIterStr) + 1
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido de iteraciones.")
                return

            # Leer matriz A
            A = np.zeros((n, n), float)
            for i in range(n):
                for j in range(n):
                    A[i][j] = float(entradas_A[i][j].get())

            # Leer vector b
            b = np.zeros(n, float)
            for i in range(n):
                b[i] = float(entradas_b[i].get())

            # Reacomodar (si se puede)
            ADom, bDom = diagonalDominante(A, b)
            if ADom is None:
                ADom = A
                bDom = b
                messagebox.showwarning("Advertencia",
                                       "La matriz no es diagonal dominante y no pudo reacomodarse.\n"
                                       "El método podría no converger.")

            #Mostrar advertencia si no es diagonal dominante
            else:
                messagebox.showinfo("Información",
                                    "La matriz ha sido reacomodada para ser diagonal dominante.")

            # Ejecutar método de Jacobi
            solucion, dfJacobi = jacobi(ADom, bDom, numIter)

            #Mostrar resultados
            texto = "RESULTADOS DEL MÉTODO DE JACOBI\n\n"

            texto += "Matriz diagonal dominante utilizada:\n"
            texto += str(ADom) + "\n\n"

            texto += f"Convergencia del método para {numIter-1} iteraciones:\n"
            texto += dfJacobi.to_string(index=False) + "\n\n"

            texto += "Solución aproximada:\n"
            for i, val in enumerate(solucion):
                texto += f"x{i+1} = {val:.6f}\n"

            # Mostrar resultados
            messagebox.showinfo("Resultados", texto)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

    btn_resolver = tk.Button(sub, text="Mostrar resultados",
                             font=("Arial", 12),
                             command=resolver_jacobi)
    btn_resolver.pack_forget()  # Oculto hasta crear la matriz