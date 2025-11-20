import sys
import os

# Rutas para importar Methods (directorio padre)
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_proyecto = os.path.dirname(ruta_actual)
if ruta_proyecto not in sys.path:
    sys.path.insert(0, ruta_proyecto)

#Librerías
import tkinter as tk
import pygame

# Importar ventanas individuales 
# No se usan porque se implementan ventanas de intro antes que ventanas del metodo
from .ventanaFalsaPosicion import ventanaFalsaPosicion
from .ventanaNewton import ventanaNewton
from .ventanaSecante import ventanaSecante
from .ventanaGauss import ventanaGauss
from .ventanaJacobi import ventanaJacobi
from .ventanaGaussSeidel import ventanaGaussSeidel
from .ventanaDoolitle import ventanaDoolittle
from .ventanaCholesky import ventanaCholesky
from .ventanaPotencia import ventanaPotencia
from .ventanaPotenciaInversa import ventanaPotenciaInversa

# Importar intros individuales
from GraphicInterface.Introductions.introFalsaPosicion import introFalsaPosicion
from GraphicInterface.Introductions.introNewton import introNewton
from GraphicInterface.Introductions.introSecante import introSecante
from GraphicInterface.Introductions.introCholesky import introCholesky
from GraphicInterface.Introductions.introGauss import introGauss
from GraphicInterface.Introductions.introJacobi import introJacobi
from GraphicInterface.Introductions.introGaussSeidel import introGaussSeidel
from GraphicInterface.Introductions.introDoolittle import introDoolittle
from GraphicInterface.Introductions.introPotencia import introPotencia
from GraphicInterface.Introductions.introPotenciaInversa import introPotenciaInversa

#            SUBMENÚS
def submenu_ecuaciones_no_lineales():
    sub = tk.Toplevel()
    sub.title("Ecuaciones no lineales")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Falsa Posición", width=20, command= ventanaFalsaPosicion).pack(pady=5)
    tk.Button(sub, text="Newton", width=20, command=ventanaNewton).pack(pady=5)
    tk.Button(sub, text="Secante", width=20, command = ventanaSecante).pack(pady=5)
    # Botón cerrar
    tk.Button(sub, text="Cerrar", font=("Arial", 10),command=sub.destroy).pack(pady=5)


def submenu_sistemas_lineales():
    sub = tk.Toplevel()
    sub.title("Sistemas de Ecuaciones Lineales")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Gauss", width=20, command = ventanaGauss).pack(pady=5)
    tk.Button(sub, text="Jacobi", width=20, command = ventanaJacobi).pack(pady=5)
    tk.Button(sub, text="Gauss-Seidel", width=20, command = ventanaGaussSeidel).pack(pady=5)
     # Botón cerrar
    tk.Button(sub, text="Cerrar", font=("Arial", 10),command=sub.destroy).pack(pady=5)

def submenu_factorizacion_lu():
    sub = tk.Toplevel()
    sub.title("Factorización LU")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Doolittle", width=20, command= ventanaDoolittle).pack(pady=5)
    tk.Button(sub, text="Cholesky", width=20, command= ventanaCholesky).pack(pady=5)
     # Botón cerrar
    tk.Button(sub, text="Cerrar", font=("Arial", 10),command=sub.destroy).pack(pady=5)

def submenu_valores_vectores():
    sub = tk.Toplevel()
    sub.title("Valores y Vectores Propios")
    sub.geometry("300x200")

    tk.Label(sub, text="Métodos disponibles:", font=("Arial", 12)).pack(pady=10)
    tk.Button(sub, text="Potencia", width=20, command= ventanaPotencia).pack(pady=5)
    tk.Button(sub, text="Potencia Inversa", width=20, command= ventanaPotenciaInversa).pack(pady=5)
     # Botón cerrar
    tk.Button(sub, text="Cerrar", font=("Arial", 10),command=sub.destroy).pack(pady=5)

#          MENÚ PRINCIPAL
def mostrar_menu(root):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text="MENÚ DE MÉTODOS NUMÉRICOS",
             font=("Arial", 16, "bold")).pack(pady=15)

    botones = [
        ("Ecuaciones no lineales",lambda root=root: intro_ecuaciones_no_lineales(root)),
        ("Sistemas de ecuaciones lineales", lambda root=root: intro_ecuaciones_lineales(root)),
        ("Factorización LU", lambda root=root: intro_factorizacion_lu(root)),
        ("Valores y vectores propios", lambda root=root: intro_valores_vectores(root))
    ]

    # Crear botones para cada opción
    for texto, comando in botones:
        tk.Button(root, text=texto, width=25, height=2,
                  command=comando).pack(pady=5)

    tk.Button(root, text="Salir", width=25, height=2,
              command=lambda: pantalla_final(root)).pack(pady=15)


#   PANTALLAS DE PRESENTACIÓN
def mostrar_introduccion(root):
    for w in root.winfo_children():
        w.destroy() # Limpia la ventana principal

    texto = (
        "Bienvenido al programa de Métodos Numéricos.\n\n"
        "En este software podrás aplicar distintos métodos para resolver:\n"
        "- Ecuaciones no lineales.\n"
        "- Sistemas de ecuaciones lineales.\n"
        "- Factorización LU.\n"
        "- Cálculo de valores y vectores propios.\n\n"
        "Presiona 'Continuar' para acceder al menú principal."
    )

    tk.Label(root, text="Introducción",
             font=("Arial", 16, "bold")).pack(pady=10)
    tk.Message(root, text=texto, width=600, font=("Arial", 12)).pack(expand=True, fill="both", padx=20, pady=10)

    tk.Button(root, text="Continuar", width=20, height=2,
              command=lambda: mostrar_menu(root)).pack(pady=15)


def mostrar_portada(root):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text="MÉTODOS NUMÉRICOS",
             font=("Arial", 20, "bold")).pack(expand=True)

    tk.Button(root, text="Continuar", width=20,
              height=2, command=lambda: mostrar_introduccion(root)).pack(pady=30)

#Funcion para mostrar las introducciones
def mostrar_ventana_intro(root, titulo, texto, accion_continuar):
    for w in root.winfo_children():
        w.destroy()

    tk.Label(root, text=titulo, font=("Arial", 18, "bold")).pack(pady=15)
    tk.Message(root, text=texto, width=600, font=("Arial", 12)).pack(
        expand=True, fill="both", padx=20, pady=10
    )
    #boton para continuar
    tk.Button(root, text="Continuar", width=20, height=2,
              command=accion_continuar).pack(pady=20)
    #Boton para regresar al menú principal
    tk.Button(root, text="Regresar al Menú Principal", width=25, height=2,
              command=lambda: mostrar_menu(root)).pack(pady=10)
    
#-------------------------------------------------   
#Funciones para la introduccion de los 4 submenús 
#-------------------------------------------------
def intro_ecuaciones_no_lineales(root):
    texto = (
        "En este módulo podrás resolver ecuaciones no lineales\n"
        "usando métodos numéricos clásicos como:\n\n"
        "- Falsa Posición\n"
        "- Newton\n"
        "- Secante\n\n"
        "Haz clic en continuar para abrir el submenú.\n"
        "Haz clic en regresar para volver al menú principal."
    )
    mostrar_ventana_intro(root, "Ecuaciones No Lineales", texto,
                          lambda: submenu_ecuaciones_no_lineales())

def intro_ecuaciones_lineales(root):
    texto = (
        "En este módulo podrás resolver sistemas de ecuaciones lineales\n"
        "usando métodos numéricos clásicos como:\n\n"
        "- Gauss\n"
        "- Jacobi\n"
        "- Gauss-Seidel\n\n"
        "Haz clic en continuar para abrir el submenú.\n"
        "Haz clic en regresar para volver al menú principal."
    )
    mostrar_ventana_intro(root, "Sistemas de Ecuaciones Lineales", texto,
                          lambda: submenu_sistemas_lineales())

def intro_factorizacion_lu(root):
    texto = (
        "En este módulo podrás resolver sistemas de ecuaciones lineales\n"
        "usando métodos numéricos clásicos como:\n\n"
        "- Doolittle\n"
        "- Cholesky\n\n"
        "Haz clic en continuar para abrir el submenú.\n"
        "Haz clic en regresar para volver al menú principal."
    )
    mostrar_ventana_intro(root, "Factorización LU", texto,
                          lambda: submenu_factorizacion_lu())
    
def intro_valores_vectores(root):
    texto = (
        "En este módulo podrás resolver sistemas de ecuaciones lineales\n"
        "usando métodos numéricos clásicos como:\n\n"
        "- Potencia\n"
        "- Potencia Inversa\n\n"
        "Haz clic en continuar para abrir el submenú.\n"
        "Haz clic en regresar para volver al menú principal."
    )
    mostrar_ventana_intro(root, "Valores y Vectores Propios", texto,
                          lambda: submenu_valores_vectores())
#------------------------------------------------------------------------------

#Funcion para mostrar la pantalla final (agradecimientos) 
def pantalla_final(root):
    mostrar_ventana_intro(
        root,
        "¡Gracias por usar el sistema!\n",
        "Este software fue desarrollado por estudiantes de MAC.\n"
        "\tDerechos reservados UNAM.©\n\n"
        "\n\n"
        "Presiona 'Continuar' para salir\n",
        lambda: root.quit()
    )

#             MAIN
def main():
    #Inicializar pygame para la música de fondo
    pygame.mixer.init()
    ruta_musica = os.path.join(ruta_proyecto, "Assets",     "Rivendell - Howard Shore.mp3")
    if os.path.exists(ruta_musica):
        pygame.mixer.music.load(ruta_musica)
        pygame.mixer.music.play(-1) #Reproducir en bucle

    # Configuración de la ventana principal
    root = tk.Tk()
    root.title("Métodos Numéricos")
    root.geometry("700x500")
    root.minsize(500, 400)

    mostrar_portada(root)
    root.mainloop()