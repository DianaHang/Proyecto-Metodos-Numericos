%matplotlib inline 
#El siguiente programa resuelve el sistema Ax=b
#Por factorizaciónn de Cholesky y lo resuelve.
import numpy as np #biblioteca para matemáticas
import matplotlib.pyplot as plt#biblioteca gráfica
import math
from numpy.linalg import LinAlgError #Importamos esto por si acaso, aunque sepamos que funciona


def plot_simple_matrix(matrix, title):#Función para graficar MATRICES
    #hace el grid para la matriz
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('green')
    n = matrix.shape[0]

    for i in range(n): #bucle for para los renglones
        for j in range(n):#bucle for para las columnas
            val = matrix[i, j]
            #bucle if si y solo si hay raices que sí las hay
            if np.isclose(val, math.sqrt(2)):
                text_value = r"$\sqrt{2}$" 
            else:
                text_value = f"{val:g}"
            
            ax.text(j, i, text_value, ha="center", va="center", color='white',
                    fontsize=16, weight="bold")#fuente del texto 
            
    ax.set_xticks(np.arange(n+1) - 0.5, minor=True)
    ax.set_yticks(np.arange(n+1) - 0.5, minor=True) #lineas para trazar el texto
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    ax.tick_params(which='both', length=0, bottom=False, left=False,
                   labelbottom=False, labelleft=False) #elimina las lineas para más homogeneidad
    ax.set_ylim(n - 0.5, - 0.5) #límies de las gráficas
    ax.set_xlim(-0.5, n - 0.5)  #límies de las gráficas
    for spine in ax.spines.values(): #para darle forma cuadrada
        spine.set_visible(False) #quita los bordes para que no se vean como cajas

    ax.set_title(title, fontsize=14, pad=20)#fuente para las gráficas

def plot_simple_vector(vector, title):#Función para graficar VECTORES
    #Se hace un vector columna para la solución
    fig, ax = plt.subplots(figsize=(2, 5)) 
    ax.set_facecolor('green')
    
    n = vector.shape[0] 

    for i in range(n): #Bucle para los renglones
        val = vector[i]
        text_value = f"{val:g}"
        
        ax.text(0, i, text_value, ha="center", va="center", color='white',
                fontsize=16, weight="bold")
            
    ax.set_xticks(np.arange(2) - 0.5, minor=True) 
    ax.set_yticks(np.arange(n+1) - 0.5, minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    ax.tick_params(which='both', length=0, bottom=False, left=False,
                   labelbottom=False, labelleft=False)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xlim(-0.5, 0.5) 
    for spine in ax.spines.values():
        spine.set_visible(False)

    ax.set_title(title, fontsize=14, pad=20)
    
#Matriz a trabajar
A_original = np.array([[4.0, 2.0, 2.0],
                       [2.0, 2.0, 0.0],
                       [2.0, 0.0, 4.0]])

# Vector de resultados de tu foto
b = np.array([1.0, 2.0, 3.0]) #vector de coeficientes del sistema original

#Inicia la Factorización de Cholesky
print("="*50)
print("***Factorización por el método de Cholesky***")
print("="*50)

try:#función para manejar errores
    L = np.linalg.cholesky(A_original)#función módulo cholesky función
    L_T = L.T#Función matriz transpuesta
    
    print("\n¡Factorización exitosa! Gráficas en proceso")

    plot_simple_matrix(A_original, " Matriz A") #función para ejecutar la matriz para la gráfica
    plot_simple_matrix(L, "Matriz L")#para graficar la matriz L
    plot_simple_matrix(L_T, "Matriz L^T")#Grafica la matriz L transpuesta

    print("\nFactorización exitosa. Gráficas generadas.")

    #Solución del sistema por factorización
    print("\n***Resolviendo el sistema Ax = b ***")
    print(f"Vector b (resultados): {b}") #Cambié 'solución X' por 'b'

    # Paso 1: Resolver Ly = b (Sustitución progresiva)
    y = np.linalg.solve(L, b)

    # Paso 2: Resolver L^T * x = y (Sustitución regresiva)
    x = np.linalg.solve(L_T, y)

    print(f"\nSolución (vector x): {np.round(x, 4)}")#solución redondeada

    plot_simple_vector(x, "Vector Solución X: ")#prepara el vector solución

    print("\n=== Comprobación si el sistema es correcto ===")
    verificacion = np.dot(A_original, x)
    print(f"Comprobación (A * x) = {np.round(verificacion, 4)}")
    
  
    if np.allclose(verificacion, b):#Condicional si el sistema es correcto. 
        # Función Numpy (np.allclose):
        # La comprobación es el resultado que obtuvo el programa al multiplicar A * x
        # b es el vector de constantes orignales. ([1.0, 2.0, 3.0]).
        print("¡El resultado es correcto!")
    else:
        print("El resultado es incorrecto.")

except LinAlgError as e:
    # Este bloque es por si la matriz falla (aunque la nuestra no)
    print(f"\n*** ¡FALLO DEL MÉTODO! ***")
    print(f"Error: {e}")
    plot_simple_matrix(A_original, "Sistema Original - Matriz (FALLIDA)")


print("\nFin de la Factorización por el Método de Choleski.")