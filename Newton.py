'''
    Este programa implementa la solución que satisface 
    las ecuaciones 3x - (x+2)^2 * e^(-x) = 0 
    mediante el uso del método de Newton 
'''
import math
import pandas as pd
import matplotlib.pyplot as plt

#Función muestra
def f1(x):
    return (3*x) - pow(x+2, 2) * math.exp(-x)

def f2(x):
    return math.cos(x) + 2 * math.sin(x) + pow(x, 2)

def f3(x):
    return math.log(abs(x-1)) + math.cos(x-1)

def derivf1(x):
    return 3 - 2*(x+2)*math.exp(-x) + (x+2)**2 * math.exp(-x)
  
def derivf2(x):
    return - math.sin(x) + 2 * math.cos(x) + 2*x

def derivf3(x):
    return 1 / (x - 1) - math.sin(x - 1)
  
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
      f = f1(xn)
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
def main():
    print("***MÉTODO DE NEWTON***\n")
    x0 = leerInput()
    dfResul, raiz = metodoNewton(f1, derivf1, x0, n = 10)
    
    #Imprimir tabla con Pandas
    pd.set_option('display.float_format', '{:.4f}'.format)
    print("\nResultados del método de Newton:\n")
    print(dfResul.to_string(index=False))
    
    print(f"\nLa solución aproximada para la función f(x) = 3x - (x+2)^2 * e^(-x) es: \n x ≈ {raiz:.6f}")
    print(f"\n f(x) ≈ {f1(raiz):.6f}")
    
    # Gráfica para mostrar convergencia del método
    plt.figure(figsize=(8,5))
    plt.plot(dfResul["n"], dfResul["xn"], marker='*', linestyle='-', color='green')
    plt.title("Convergencia del Método de Newton", fontsize=14)
    plt.xlabel("Número de iteraciones", fontsize=12)
    plt.ylabel("Aproximación xn", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()
    
if __name__ == "__main__":
    main()