import sys
import os
import tkinter as tk
from tkinter import messagebox
import numpy as np

from potencia import metodoPotencia


def ventanaPotencia():
    sub = tk.Toplevel()
    sub.title("Método de la Potencia")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de la Potencia",
             font=("Arial", 16, "bold")).pack(pady=10)

    tk.Label(sub, text="Tamaño de la matriz n×n:",
             font=("Arial", 12)).pack()

    entrada_n = tk.Entry(sub, width=5, font=("Arial", 12))
    entrada_n.pack()

    frame_matriz = tk.Frame(sub)
    entradas_A = []

    def crear_matriz():
        nonlocal entradas_A

        for w in frame_matriz.winfo_children():
            w.destroy()

        entradas_A = []

        try:
            n = int(entrada_n.get())
            if n < 2:
                raise ValueError
        except:
            messagebox.showerror("Error", "Ingresa un entero válido.")
            return

        tk.Label(sub, text=f"Ingresa la matriz A ({n}×{n}):",
                 font=("Arial", 12)).pack()

        frame_matriz.pack(pady=5)

        for i in range(n):
            fila = []
            for j in range(n):
                e = tk.Entry(frame_matriz, width=6, font=("Arial", 11))
                e.grid(row=i, column=j, padx=3, pady=3)
                fila.append(e)
            entradas_A.append(fila)

        btn_resolver.pack(pady=15)

    tk.Button(sub, text="Crear matriz", font=("Arial", 12),
              command=crear_matriz).pack(pady=10)

    def resolver():
        try:
            n = int(entrada_n.get())
            A = np.zeros((n, n))

            for i in range(n):
                for j in range(n):
                    A[i][j] = float(entradas_A[i][j].get())

            λ, v, it = metodoPotencia(A)

            texto = f"Autovalor dominante:\nλ = {λ:.6f}\n\n"
            texto += "Autovector:\n"
            texto += str(v) + "\n"
            texto += f"\nIteraciones: {it}"

            messagebox.showinfo("Resultados", texto)

        except Exception as e:
            messagebox.showerror("Error", str(e))

    btn_resolver = tk.Button(sub, text="Calcular",
                             font=("Arial", 12),
                             command=resolver)
    btn_resolver.pack_forget()
