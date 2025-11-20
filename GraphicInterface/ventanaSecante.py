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
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Methods.Secante import metodoSecante, f1, f2, f3

def mostrar_grafica_tkinter(frame, df, titulo, columna_y):
    # Elimina una gráfica anterior
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

def ventanaSecante():
    sub = tk.Toplevel()
    sub.title("Método de la Secante")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de la Secante",
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

     # Entradas de x₀ y x₁
    tk.Label(sub, text="Valor inicial x₀:",
             font=("Arial", 12)).pack(pady=5)
    entrada_x0 = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_x0.pack()

    tk.Label(sub, text="Valor inicial x₁:",
             font=("Arial", 12)).pack(pady=5)
    entrada_x1 = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_x1.pack()

    # Entrada de número de iteraciones
    tk.Label(sub, text="Número de iteraciones:",
             font=("Arial", 12)).pack(pady=5)

    entrada_iter = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_iter.insert(0, "")
    entrada_iter.pack()

    frame_grafica = tk.Frame(sub)
    frame_grafica.pack(pady=10)

    #Mostrar resultados
    def resolver_secante():
        try:
            f = opciones[opcion_var.get()]
            x0 = float(entrada_x0.get())
            x1 = float(entrada_x1.get())
            n = int(entrada_iter.get())

            dfSec, raiz = metodoSecante(f, x0, x1, n)

            # Construir texto igual que Jacobi
            texto = "RESULTADOS DEL MÉTODO DE LA SECANTE\n\n"

            texto += f"Función seleccionada:\n{opcion_var.get()}\n\n"

            texto += f"Valores iniciales:\n"
            texto += f"x₀ = {x0}\n"
            texto += f"x₁ = {x1}\n"
            texto += f"Iteraciones: {n}\n\n"

            texto += "Convergencia del Método de la Secante:\n"
            dfSec = dfSec.round(4)
            texto += dfSec.to_string(index=False)
            texto += "\n\n"

            texto += f"Solución aproximada:\n x ≈ {raiz:.6f}\n"
            texto += f"f(x) ≈ {f(raiz):.6f}\n"

            messagebox.showinfo("Resultados", texto)

            # ---- Mostrar gráfica ----
            mostrar_grafica_tkinter(
                frame_grafica,
                dfSec,
                "Convergencia del Método de la Secante",
                "xn"
            )

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

    # Botón resolver
    tk.Button(sub,
              text="Mostrar resultados",
              font=("Arial", 12),
              width=15,
              command=resolver_secante).pack(pady=15)

    # Botón cerrar
    tk.Button(sub,
              text="Cerrar",
              font=("Arial", 12),
              command=sub.destroy).pack(pady=5)