%matplotlib inline 
import numpy as np #biblioteca para matemáticas, matrices y vectores.
import matplotlib.pyplot as plt#biblioteca gráfica
import math
import scipy.linalg # scipy.linag, para álgebra Lineal. 
# Importa el módulo 'linalg' (Linear Algebra) de la biblioteca SciPy.
# Lo usamos porque su función 'lu()' es excelente para la 
# factorización LU con pivoteo (PA=LU).


def plot_simple_matrix(matrix, title):#Función para graficar MATRICES
    #hace el grid para la matriz
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.set_facecolor('green')#color del fondo facecolor
    n = matrix.shape[0]#numero de filas 

    for i in range(n): #bucle for para los renglones
        for j in range(n):#bucle for para las columnas
            val = matrix[i, j] #valores numéricos i, j. 
            # Formato para mostrar números de forma limpia
            text_value = f"{val:g}" if abs(val) > 1e-10 else "0"
            
            ax.text(j, i, text_value, ha="center", va="center", color='white',
                    fontsize=16, weight="bold")#fuente del texto y sangría
            
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
    fig, ax = plt.subplots(figsize=(2, 5)) # Imagen, 2 de alto, 5 de ancho. 
    ax.set_facecolor('green')
    
    n = vector.shape[0] #obtiene número de filas, dimensión de la matriz

    for i in range(n): #Bucle para los renglones iniciando en i 
        val = vector[i]
        text_value = f"{val:g}"# Formatea el valor como texto.****
        
        ax.text(0, i, text_value, ha="center", va="center", color='white',# Escribe el texto en la posición (0, i). (Columna 0, fila i)
                fontsize=16, weight="bold")#Coloca el título de las matrices correspondientes
        
            
    ax.set_xticks(np.arange(2) - 0.5, minor=True) # Dibuja la cuadrícula (horizontal y vertical).
    ax.set_yticks(np.arange(n+1) - 0.5, minor=True)
    ax.grid(which='minor', color='black', linestyle='-', linewidth=2)

    ax.tick_params(which='both', length=0, bottom=False, left=False, #retira los ejes
                   labelbottom=False, labelleft=False)
    ax.set_ylim(n - 0.5, -0.5)
    ax.set_xlim(-0.5, 0.5) #límites de los gráficos 
    for spine in ax.spines.values():#recorta los bordes
        spine.set_visible(False)

    ax.set_title(title, fontsize=14, pad=20)
#Matriz a trabajar
A_original = np.array([[4.0, 2.0, 2.0],
                       [2.0, 2.0, 0.0],
                       [2.0, 0.0, 4.0]])

# Vector de resultados
b = np.array([1.0, 2.0, 3.0]) 

#Factorización del método Doolittle

print("="*50)
print("***Factorización por el Método LU (Doolittle)***")
print("="*50)

try:#NOTA: linea para el pivoteo
    # scipy.linalg.lu() implementa la factorización PA=LU
    # P = Matriz de permutación (pivoteo)
    # L = Matriz triangular inferior (unitaria si P=I)
    # U = Matriz triangular superior
    P, L, U = scipy.linalg.lu(A_original)#pivoteo

    # Graficamos las matrices resultantes
    plot_simple_matrix(A_original, " Matriz A")
    plot_simple_matrix(P, "Matriz P (Permutación)")
    plot_simple_matrix(L, "Matriz L (Inferior)")
    plot_simple_matrix(U, "Matriz U (Superior)")

    print("\nFactorización exitosa. Gráficas generadas.")

    print("\n***Resolviendo el sistema Ax = b (mediante PAx = Pb)***")
    
    # Cálculo del vector P*b (b permutado)
    b_permutado = np.dot(P, b)#vector original
    print(f"Vector b (original): {b}")
    print(f"Vector Pb (permutado): {b_permutado}")

    
    y = np.linalg.solve(L, b_permutado)#Resolver L*y = P*b (Sustitución progresiva)
    #NOTA: (np.linalg.solve es eficiente para matrices triangulares)

    x = np.linalg.solve(U, y)#Resolver Ux = y (Sustitución regresiva)

    print(f"\nSolución (vector x): {np.round(x, 4)}")#solución redondeada a 4 cifras como en el curso

    plot_simple_vector(x, "Vector Solución X: ")#prepara el vector solución

    print("\n=== Comprobación del sistema ===")
    verificacion = np.dot(A_original, x)#Por álgebra lineal la matriz A*x
    print(f"Comprobación (A * x) = {np.round(verificacion, 4)}")
    print(f"Original (vector b) = {b}")
    
  
    if np.allclose(verificacion, b): #If para comparar si la solución es correcta
        print("¡El resultado es correcto!")
    else:
        print("El resultado es incorrecto.")
#Las siguientes lineas sirven para reciclar el código, para futuros anális
#No son necesarias, pero se agregan por contención. 
except Exception as e:
    # Captura de error más general
    print(f"\n*** ¡FALLO DEL MÉTODO! ***")
    print(f"Error: {e}")
    plot_simple_matrix(A_original, "Sistema Original - Matriz (FALLIDA)")


print("\nFin de la Factorización por el Método LU.")