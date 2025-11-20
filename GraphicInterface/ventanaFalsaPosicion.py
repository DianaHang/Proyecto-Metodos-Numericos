import sys
import os
# Ajustar la ruta para importar módulos desde el directorio del proyecto
ruta_actual = os.path.dirname(os.path.abspath(__file__))          # /GraphicInterface
ruta_proyecto = os.path.dirname(ruta_actual)                      # /ProyectoFinal

if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

"""##################################################
"""
#Librerías
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Methods.FalsaPosicion import metodoFalsaPosicion, f1, f2, f3

def mostrar_grafica_tkinter(frame, df, titulo, columna_y):
    # Elimina cualquier gráfica previa
    for widget in frame.winfo_children():
        widget.destroy()

    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)

    ax.plot(df["n"], df[columna_y],
            marker='o', linestyle='-', linewidth=2)

    ax.set_title(titulo, fontsize=14)
    ax.set_xlabel("Iteraciones")
    ax.set_ylabel(columna_y)
    ax.grid(True, linestyle='--', alpha=0.6)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

def ventanaFalsaPosicion():
    sub = tk.Toplevel()
    sub.title("Método de Falsa Posición")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de Falsa Posición",
             font=("Arial", 16, "bold")).pack(pady=10)

    # Selección de función
    tk.Label(sub, text="Seleccione una ecuación:").pack()

    opciones = {
        "1. 3x - (x+2)² e⁻ˣ = 0": f1,
        "2. cos(x) + 2 sin(x) + x² = 0": f2,
        "3. sin(x) - 0.5 = 0": f3
    }

    opcion_var = tk.StringVar(sub, value=list(opciones)[0])
    tk.OptionMenu(sub, opcion_var, *opciones.keys()).pack(pady=5)

    # Entradas a y b
    tk.Label(sub, text="Límite inferior (a):",
             font=("Arial", 12)).pack(pady=5)
    entrada_a = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_a.pack()

    tk.Label(sub, text="Límite superior (b):",
             font=("Arial", 12)).pack(pady=5)
    entrada_b = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_b.pack()

    # Entrada de iteraciones
    tk.Label(sub, text="Número de iteraciones:",
             font=("Arial", 12)).pack(pady=5)

    entrada_iter = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_iter.insert(0, "")
    entrada_iter.pack()

    frame_grafica = tk.Frame(sub)
    frame_grafica.pack(pady=10)

    #Mostrar resultados
    def resolver_falsa_posicion():
        try:
            f = opciones[opcion_var.get()]
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            n = int(entrada_iter.get())

            dfFP, raiz = metodoFalsaPosicion(f, a, b, n)

            #Texto de resultados
            texto = "RESULTADOS DEL MÉTODO DE FALSA POSICIÓN\n\n"

            texto += f"Función seleccionada:\n{opcion_var.get()}\n\n"
            texto += f"Intervalo inicial: [{a}, {b}]\n"
            texto += f"Número de iteraciones: {n}\n\n"

            texto += "Convergencia del Método de Falsa Posición:\n"
            dfFP = dfFP.round(4)
            texto += dfFP.to_string(index=False) + "\n\n"

            texto += f"Solución aproximada:\n x ≈ {raiz:.6f}\n"
            texto += f"f(x) ≈ {f(raiz):.6f}\n"

            messagebox.showinfo("Resultados", texto)

             # ---- Mostrar gráfica ----
            mostrar_grafica_tkinter(
                frame_grafica,
                dfFP,
                "Convergencia del Método de Falsa Posición",
                "c"
            )

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

    # Botón resolver
    tk.Button(sub,
              text="Mostrar resultados",
              font=("Arial", 12),
              width=18,
              command=resolver_falsa_posicion).pack(pady=15)

    # Botón cerrar
    tk.Button(sub,
              text="Cerrar",
              font=("Arial", 12),
              command=sub.destroy).pack(pady=5)