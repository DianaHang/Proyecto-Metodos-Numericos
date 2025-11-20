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

from Methods.PotenciaInversa import metodoPotenciaInversa

def ventanaPotenciaInversa():
    sub = tk.Toplevel()
    sub.title("Método de la Potencia Inversa")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de la Potencia Inversa",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Ingrese el tamaño de la matriz (nxn):", font=("Arial", 12)).pack()

    entrada_n = tk.Entry(sub, width=5, font=("Arial", 12))
    entrada_n.pack()

    frame_matriz = tk.Frame(sub)
    frame_vector = tk.Frame(sub)

    entradas_A = []
    entradas_x0 = []

    # Crear campos dinámicos
    def crear_campos():
        nonlocal entradas_A, entradas_x0
        # Limpiar posibles widgets anteriores
        for w in frame_matriz.winfo_children(): w.destroy()
        for w in frame_vector.winfo_children(): w.destroy()

        entradas_A = []
        entradas_x0 = []

        try:
            n = int(entrada_n.get())
            if n < 2:
                raise ValueError("n debe ser mayor o igual a 2")
        except:
            messagebox.showerror("Error", "Ingresa un valor entero válido para n.")
            return

        # Matriz A
        tk.Label(sub, text=f"Ingrese los valores de la matriz A ({n} × {n}):", font=("Arial", 12)).pack(pady=5)
        frame_matriz.pack(pady=5)

        # Crear entradas para A
        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame_matriz, width=6, font=("Arial", 12))
                e.grid(row=i, column=j, padx=3, pady=3)
                fila.append(e)
            entradas_A.append(fila)

        # Vector inicial x0
        tk.Label(sub, text=f"Ingrese el vector inicial x0 ({n} x 1) ≠ 0: ", font=("Arial", 12)).pack(pady=5)
        frame_vector.pack()

        # Crear entradas para x0
        for i in range(n):
            e = tk.Entry(frame_vector, width=6, font=("Arial", 12))
            e.grid(row=i, column=0, pady=3)
            entradas_x0.append(e)

        btn_resolver.pack(pady=15)

    #Botón para generar la matriz y el vector
    tk.Button(sub, text="Crear matriz",  font=("Arial", 12), command=crear_campos).pack(pady=10)

    # Entrada número de iteraciones
    tk.Label(sub, text="Número de iteraciones:", font=("Arial", 12)).pack()
    entrada_iter = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_iter.insert(0, "")
    entrada_iter.pack()

    # Resolver método de la potencia inversa
    def resolver_potencia_inversa():
        try:
            n = int(entrada_n.get())
            numIterStr = entrada_iter.get()

            try:
                numIter = int(numIterStr) + 1
            except ValueError:
                messagebox.showerror("Error", "Ingresa un número válido de iteraciones.")
                return

            # Leer matriz A
            A = np.zeros((n, n))
            for i in range(n):
                for j in range(n):
                    A[i][j] = float(entradas_A[i][j].get())

            # Leer vector inicial x0
            x0 = np.zeros(n)
            for i in range(n):
                x0[i] = float(entradas_x0[i].get())

            #Verificar que x0 no sea el vector nulo
            if np.allclose(x0, 0):
                messagebox.showerror("Error", "El vector inicial x0 no puede ser nulo.")
                return

            # Ejecutar método d ela Potencia Inversa
            lambda_min, x, historial = metodoPotenciaInversa(A, x0, numIter)

            #Mostrar resultados
            texto = "RESULTADOS DEL MÉTODO DE LA POTENCIA INVERSA\n\n"

            texto += "Iteraciones:\n"
            for k, (lam, xv) in enumerate(historial):
                texto += f"Iteración {k}:\n"
                texto += f"  λₖ = {lam:.4f}\n"
                texto += f"  xₖ = {xv}\n\n"

            texto += "\nValor propio mínimo aproximado:\n"
            texto += f"λ_min ≈ {lambda_min:.4f}\n\n"

            texto += "Vector propio asociado:\n"
            for i, val in enumerate(x):
                texto += f"x{i+1} = {val:.4f}\n"

            messagebox.showinfo("Resultados", texto)

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

    btn_resolver = tk.Button(sub, text="Calcular", font=("Arial", 12), command=resolver_potencia_inversa)
    btn_resolver.pack_forget()  # Oculto hasta crear la matriz
 
