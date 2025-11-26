# tablaScrollable.py
import tkinter as tk
from tkinter import ttk
import pandas as pd

def mostrar_tabla(df, titulo="Tabla de resultados", decimals: int = 5, format_cols_prefix='x'):
    """
    Muestra un DataFrame en una ventana Tkinter Treeview.

    Args:
        df: pandas.DataFrame con los datos a mostrar.
        titulo: título de la ventana.
        decimals: cantidad de decimales a mostrar en las columnas formateadas.
        format_cols_prefix: si es una cadena (ej. 'x'), se formatean las columnas cuyo nombre comience
            por ese prefijo; si es una lista/tupla, se formatean exactamente esas columnas; si es
            cualquier otro valor (p. ej. None), se formatean todas las columnas numéricas.

    Ejemplos:
        mostrar_tabla(df, decimals=5, format_cols_prefix='x')  # sólo x1, x2, ...
        mostrar_tabla(df, decimals=3, format_cols_prefix=['x1', 'x2'])  # sólo x1 y x2
        mostrar_tabla(df, decimals=4, format_cols_prefix=None)  # todas las columnas numéricas
    """
    win = tk.Toplevel()
    win.title(titulo)
    win.geometry("700x500")

    # Frame contenedor
    frame = ttk.Frame(win)
    frame.pack(fill=tk.BOTH, expand=True)

    # Tabla
    tabla = ttk.Treeview(frame, show="headings")
    tabla.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Scrollbar vertical
    scroll_y = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tabla.yview)
    scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
    tabla.configure(yscrollcommand=scroll_y.set)

    # Scrollbar horizontal
    scroll_x = ttk.Scrollbar(win, orient=tk.HORIZONTAL, command=tabla.xview)
    scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
    tabla.configure(xscrollcommand=scroll_x.set)

    # Prepare a display copy converted to strings for formatting
    df_display = df.copy()

    # Decide which columns to format: by prefix if format_cols_prefix is a string,
    # by list if a list/tuple is passed, or else any float columns
    if isinstance(format_cols_prefix, str):
        cols_to_format = [c for c in df_display.columns if c.startswith(format_cols_prefix)]
    elif isinstance(format_cols_prefix, (list, tuple)):
        cols_to_format = [c for c in df_display.columns if c in format_cols_prefix]
    else:
        cols_to_format = [c for c in df_display.columns if pd.api.types.is_float_dtype(df_display[c])]

    # Format only these columns as strings rounded to `decimals` places
    for c in cols_to_format:
        df_display[c] = df_display[c].map(lambda v: f"{v:.{decimals}f}" if pd.notnull(v) else "")

    # Encabezados
    tabla["columns"] = list(df_display.columns)

    for col in df_display.columns:
        tabla.heading(col, text=col)
        tabla.column(col, width=120, anchor=tk.CENTER)

    # Insertar datos fila por fila
    for _, row in df_display.iterrows():
        # Ensure values are string - Treeview renders text
        tabla.insert("", tk.END, values=[str(v) for v in list(row)])

    win.mainloop()
