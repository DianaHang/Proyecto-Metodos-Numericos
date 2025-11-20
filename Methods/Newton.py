'''
    Este programa implementa la solución que satisface 
    la ecuación 3x - (x+2)^2 * e^(-x) = 0 
    mediante el uso del método de Newton 
'''
import math
import pandas as pd
import matplotlib.pyplot as plt

#Función muestra
def funcion1(x):
    return (3*x) - pow(x+2, 2) * math.exp(-x)

def derivf1(x):
    return 3 - 2*(x+2)*math.exp(-x) + (x+2)**2 * math.exp(-x)
    
#Función para validar inputs numéricos
def leerInput():
    while True:
        #Solicitar input muestra
        x0Str = input("Escriba el valor inicial de tu entrada x0: ")
        #Validar si se recibe una entrada numérica
        try:
          return float(x0Str)
        except ValueError:
          print("Error: La entrada debe ser un número válido.\n")

#Método de Newton
def metodoNewton(f, derivada, x0, n = 10):
    # Listas para crear un Data Drame (df)
    iteraciones = []
    xList = []
    fList = []
    derivList = []
    
    xn = x0
    
    #Realizar iteraciones con método de Newton
    for i in range(n):
      f = funcion1(xn)
      deriv = derivada(xn)
      
      #Validar no división por cero
      if deriv == 0:
         print("La derivada escero, no se puede continuar con el método.")
         break
      
      #Almacenar datos en las listas del DF
      iteraciones.append(i+1)
      xList.append(xn)
      fList.append(f)
      derivList.append(deriv)
      
      #Actualizar valor de xn
      xn = xn - f / deriv
      
    #Creacion del Data Frame
    df = pd.DataFrame({
        "n": iteraciones,
        "xn": xList,
        "f(xn)": fList,
        "f'(xn)": derivList
        })
    
    #Mostrar el Data Frame hasta el último valor
    return df, xList[-1]

#Main
def mainNewton():
    print("***MÉTODO DE NEWTON***\n")
    x0 = leerInput()
    dfResul, raiz = metodoNewton(funcion1, derivf1, x0, n = 10)
    #Imprimir tabla con Pandas
    pd.set_option('display.float_format', '{:.4f}'.format)
    print("\nResultados del método de Newton-Raphson:\n")
    print(dfResul.to_string(index=False))

    print(f"\nLa solución aproximada para la función f(x) = 3x - (x+2)^2 * e^(-x) es: \n x ≈ {raiz:.4f}")

    # GRÁFICA PARA CONVERGENCIA DEL MÉTODO

    plt.figure(figsize=(8,5))
    plt.plot(dfResul["n"], dfResul["xn"], marker='o', linestyle='-', color='teal')
    plt.title("Convergencia del Método de Newton", fontsize=14)
    plt.xlabel("Número de iteraciones", fontsize=12)
    plt.ylabel("xn", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()