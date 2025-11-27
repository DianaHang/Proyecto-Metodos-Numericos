# tablaScrollable.py
import tkinter as tk
from tkinter import ttk
import pandas as pd

def mostrar_tabla(df, titulo="Tabla de resultados", decimals: int = 5, format_cols_prefix='x'):
    """
    Muestra un DataFrame en una ventana Tkinter Treeview con mejor estilo visual.
    """

    win = tk.Toplevel()
    win.title(titulo)
    win.geometry("750x520")

    # ---------- ESTILO MEJORADO ----------
    style = ttk.Style()
    style.theme_use("clam")   # "clam" soporta colores y bordes


    # Celdas normales
    style.configure(
        "Treeview",
        background="#76B4F3",
        foreground="black",
        font=("Segoe UI", 10),
        rowheight=26,
        borderwidth=1,
        bordercolor="#000000",
        relief="solid",
        columnborderwidth=1,
        columnbordercolor="#000000"
    )

    # Encabezados
    style.configure(
        "Treeview.Heading",
        background="#003366",    # Azul oscuro
        foreground="white",
        font=("Segoe UI", 10, "bold"),
        borderwidth=1,
        relief="raised"
    )

    # Colores alternados
    style.map(
        "Treeview",
        background=[("selected", "#048a04")],
        foreground=[("selected", "white")]
    )

    # Frame contenedor
    frame = ttk.Frame(win, borderwidth=1, relief="solid")
    frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    tabla = ttk.Treeview(frame, show="headings")
    tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbars
    scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    tabla.configure(yscrollcommand=scroll_y.set)

    scroll_x = ttk.Scrollbar(win, orient=tk.HORIZONTAL, command=tabla.xview)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
    tabla.configure(xscrollcommand=scroll_x.set)

    # ---------- FORMATO DEL DATAFRAME ----------
    df_display = df.copy()

    if isinstance(format_cols_prefix, str):
        cols_to_format = [c for c in df_display.columns if c.startswith(format_cols_prefix)]
    elif isinstance(format_cols_prefix, (list, tuple)):
        cols_to_format = [c for c in df_display.columns if c in format_cols_prefix]
    else:
        cols_to_format = [c for c in df_display.columns if pd.api.types.is_float_dtype(df_display[c])]

    for c in cols_to_format:
        df_display[c] = df_display[c].map(lambda v: f"{v:.{decimals}f}" if pd.notnull(v) else "")

    tabla["columns"] = list(df_display.columns)

    for col in df_display.columns:
        tabla.heading(col, text=col)
        tabla.column(col, width=120, anchor=tk.CENTER)

    # ---------- INSERTAR DATOS CON COLORES ----------
    for index, (_, row) in enumerate(df_display.iterrows()):
        tags = ("evenrow",) if index % 2 == 0 else ("oddrow",)
        tabla.insert("", tk.END, values=list(row.values), tags=tags)

    # Colores alternados
    tabla.tag_configure("evenrow", background="#ffffff")  # Gris claro
    tabla.tag_configure("oddrow", background="#448DD6")   


