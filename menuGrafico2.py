import tkinter as tk
from tkinter import Toplevel, messagebox
import math


# ===============================
# FUNCIONES NUMÉRICAS
# ===============================

def biseccion(fx, a, b, tol, max_iter):
    """
    Ejecuta el método de bisección.
    fx: función en texto, ejemplo: "x**3 - x - 2"
    a, b: intervalos iniciales
    tol: tolerancia
    max_iter: número máximo de iteraciones
    """

    def f(x):
        return eval(fx, {"x": x, "math": math})

    if f(a) * f(b) >= 0:
        return "No cumple con f(a)*f(b)<0. No hay garantía de raíz en este intervalo."

    iteracion = 0
    while iteracion < max_iter:
        c = (a + b) / 2

        if f(c) == 0 or abs(b - a) < tol:
            return f"✅ Raíz aproximada: x = {c:.6f} \nIteraciones: {iteracion}"

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iteracion += 1

    return f"⚠️ No se encontró raíz en {max_iter} iteraciones.\nÚltimo valor aproximado: x = {c:.6f}"


# ===============================
# VENTANA DE BISECCIÓN (MODIFICADA)
# ===============================

def ventana_biseccion():
    sub = Toplevel()
    sub.title("Método de Bisección")
    sub.geometry("400x400")

    tk.Label(sub, text="Método de Bisección", font=("Arial", 14, "bold")).pack(pady=10)

    tk.Label(sub, text="Selecciona una ecuación:", font=("Arial", 11)).pack(pady=5)

    # OPCIONES DE FUNCIONES PARA SELECCIONAR
    ecuaciones = {
        "1.  x^3 - x - 2": "x**3 - x - 2",
        "2.  e^x - 3x": "math.exp(x) - 3*x",
        "3.  sin(x) - 0.5": "math.sin(x) - 0.5"
    }

    opcion_var = tk.StringVar(sub)
    opcion_var.set("1.  x^3 - x - 2")  # Valor por defecto

    menu = tk.OptionMenu(sub, opcion_var, *ecuaciones.keys())
    menu.pack(pady=5)

    # Entradas de valores numéricos
    tk.Label(sub, text="Límite inferior (a):").pack()
    entrada_a = tk.Entry(sub, width=10)
    entrada_a.pack()

    tk.Label(sub, text="Límite superior (b):").pack()
    entrada_b = tk.Entry(sub, width=10)
    entrada_b.pack()

    tk.Label(sub, text="Tolerancia:").pack()
    entrada_tol = tk.Entry(sub, width=10)
    entrada_tol.insert(0, "0.0001")
    entrada_tol.pack()

    tk.Label(sub, text="Iteraciones máximas:").pack()
    entrada_iter = tk.Entry(sub, width=10)
    entrada_iter.insert(0, "50")
    entrada_iter.pack()

    resultado = tk.Label(sub, text="", font=("Arial", 11), wraplength=350)
    resultado.pack(pady=10)

    def ejecutar_biseccion():
        try:
            fx = ecuaciones[opcion_var.get()]  # obtiene la función seleccionada
            a = float(entrada_a.get())
            b = float(entrada_b.get())
            tol = float(entrada_tol.get())
            max_iter = int(entrada_iter.get())

            salida = biseccion(fx, a, b, tol, max_iter)
            resultado.config(text=salida)

        except Exception as e:
            messagebox.showerror("Error", "Revisa los datos ingresados.\n" + str(e))

    tk.Button(sub, text="Calcular", command=ejecutar_biseccion, width=15).pack(pady=10)
    tk.Button(sub, text="Cerrar", command=sub.destroy).pack(pady=5)


# ===============================
# SUBMENÚS
# ===============================

def submenu_ecuaciones_no_lineales():
    sub = Toplevel()
    sub.title("Ecuaciones no lineales")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)

    tk.Button(sub, text="Bisección", width=20, command=ventana_biseccion).pack(pady=5)
    tk.Button(sub, text="Newton-Raphson (próximamente)", width=20).pack(pady=5)
    tk.Button(sub, text="Secante (próximamente)", width=20).pack(pady=5)


def submenu_sistemas_lineales():
    sub = Toplevel()
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

    tk.Button(sub, text="Método de la Potencia (próximamente)", width=20).pack(pady=5)


# ===============================
# MENÚ PRINCIPAL
# ===============================

def main():
    root = tk.Tk()
    root.title("Métodos Numéricos")
    root.geometry("330x350")

    tk.Label(root, text="MENÚ DE MÉTODOS NUMÉRICOS", font=("Arial", 14, "bold")).pack(pady=15)

    tk.Button(root, text="Ecuaciones no lineales", command=submenu_ecuaciones_no_lineales,
              width=25, height=2).pack(pady=5)

    tk.Button(root, text="Sistemas de ecuaciones lineales", command=submenu_sistemas_lineales,
              width=25, height=2).pack(pady=5)

    tk.Button(root, text="Factorización LU", command=submenu_factorizacion_lu,
              width=25, height=2).pack(pady=5)

    tk.Button(root, text="Valores y vectores propios", command=submenu_valores_vectores,
              width=25, height=2).pack(pady=5)

    tk.Button(root, text="Salir", command=root.quit, width=25, height=2).pack(pady=15)

    root.mainloop()


if __name__ == "__main__":
    main()