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
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from Methods.Newton import metodoNewton, f1, df1, f2, df2, f3, df3

def mostrar_grafica_tkinter(frame, df, titulo, columna_y):
    # Borrar una gráfica previa dentro del frame
    for widget in frame.winfo_children():
        widget.destroy()

    fig = plt.Figure(figsize=(6,4), dpi=100)
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

def ventanaNewton():
    sub = tk.Toplevel()
    sub.title("Método de Newton")
    sub.geometry("600x600")

    tk.Label(sub, text="Método de Newton",
            font=("Arial", 16, "bold")).pack(pady=10)

    # Selección de función
    tk.Label(sub, text="Seleccione una ecuación:").pack()

    opciones = {
        "1. 3x - (x+2)² e⁻ˣ = 0": (f1, df1),
        "2. cos(x) + 2 sin(x) + x² = 0": (f2, df2),
        "3. sin(x) - 0.5 = 0": (f3, df3)
    }

    opcion_var = tk.StringVar(sub, value=list(opciones)[0])
    tk.OptionMenu(sub, opcion_var, *opciones.keys()).pack(pady=5)

    # Entrada de x0
    tk.Label(sub, text="Valor inicial x₀:", font=("Arial", 12)).pack(pady=5)
    entrada_x0 = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_x0.pack()

    # Entrada de número de iteraciones
    tk.Label(sub, text="Número de iteraciones:", font=("Arial", 12)).pack(pady=5)

    entrada_iter = tk.Entry(sub, width=10, font=("Arial", 12))
    entrada_iter.insert(0, "")
    entrada_iter.pack()

    frame_grafica = tk.Frame(sub)
    frame_grafica.pack(pady=10)

    #Mostrar resultados
    def resolver_newton():
        try:
            # Obtener función y derivada seleccionada
            f, df = opciones[opcion_var.get()]

            # Leer inputs
            x0 = float(entrada_x0.get())
            n = int(entrada_iter.get())

            # Ejecutar método de Newton
            dfNewton, raiz = metodoNewton(f, df, x0, n)

            # Texto de resultados
            texto = "RESULTADOS DEL MÉTODO DE NEWTON\n\n"
            
            texto += f"Función seleccionada:\n{opcion_var.get()}\n\n"
            texto += f"Valor inicial x₀ = {x0}\n"
            texto += f"Número de iteraciones: {n}\n\n"

            texto += "Convergencia del Método de Newton:\n"
            dfNewton = dfNewton.round(4)
            texto += dfNewton.to_string(index=False) + "\n\n"

            texto += f"Solución aproximada:\n x ≈ {raiz:.6f}\n"

            # Mostrar resultados
            messagebox.showinfo("Resultados", texto)

            # ---- Mostrar gráfica ----
            mostrar_grafica_tkinter(
                frame_grafica,
                dfNewton,
                "Convergencia del Método de Newton",
                "xn"
            )

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un problema:\n{e}")

    # Botón resolver
    tk.Button(sub,
            text="Mostrar resultados",
            font=("Arial", 12),
            width=15,
            command=resolver_newton).pack(pady=5)
    
    # Botón cerrar
    tk.Button(sub,
            text="Cerrar",
            font=("Arial", 12),
            command=sub.destroy).pack(pady=5)
