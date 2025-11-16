'''
    El siguiente programa satisface la ecuación 
    propuesta  f(x) = 3x - (x+2)^2 * e^(-x) 
    por Método de Falsa posición
'''
import math
import pandas as pd
import matplotlib.pyplot as plt

#Funciones a trabajar
def f1(x):
    return (3*x) - pow(x+2, 2) * math.exp(-x)


def leerInputs(): #Entradas para el usuario
    while True:
        aStr = input("Escriba el valor inicial del intervalo a: ")
        bStr = input("Escriba el valor inicial del intervalo b: ")

        #Validar si se reciben entradas numéricas
        try:
          a = float(aStr)
          b = float(bStr)
          if f1(a) * f1(b) >= 0: #validación de signos.
              print("\nIMPORTANTE: Si f(a) y f(b) tienen signos iguales, no procede el método; brinde otros valores.\n")
          else:
              return a, b

        except ValueError:
          print("ERROR: INGRESE ENTRADAS VÁLIDAS.\n")
          
#Método de Falsa Posición
def metodoFalsaPosicion(f, a, b, n = 12): #Se define MF, maximo 12 interaciones.
    iteraciones = []
    aList = []
    bList = [] #se crean celdas tipo excel
    faList = []
    fbList = []
    xnList = []
    fxnList = []

    #Realizar iteraciones con método de Falsa Posición
    for i in range(n):
      fa = f(a)
      fb = f(b)
      if (fb - fa) == 0: #conidicion si hay 0/0
         print("LA DIVISIÓN ENTRE CERO NO ESTÁ DEFINIDA: FIN DE LA ITERACIÓN.")
         break
      xn = (a * fb - b * fa) / (fb - fa)#aproximación a la raíz
      fxn = f(xn) #llamada recursiva, se autoevalua para generar nueva aproximación
      iteraciones.append(i+1)
      aList.append(a)
      bList.append(b) #append, agrega al final de la lista
      
      faList.append(fa)
      fbList.append(fb)
      
      xnList.append(xn)
      fxnList.append(fxn)
      
#Aqui se actualiza el intervalo, sin ello, no existe método
      if fa * fxn < 0:
          b = xn
      elif fa * fxn > 0:
          a = xn
      else:
          # Al multiplicar las funciones evualidas si son  = 0 fin del programa.
          break
      
                           #las lineas de abajo crean las gráficas panda las llama
    df = pd.DataFrame({
        "n": iteraciones,
        "a": aList,
        "b": bList,
        "f(a)": faList,
        "f(b)": fbList,
        "xn": xnList,
        "f(xn)": fxnList
        })
    return df, xnList[-1] #Nos regresa el último valor

#Salida del programa
def mainFP():
    print("==============MÉTODO DE FALSA POSICIÓN==================\n")
    print("========================================================\n")
    print("IMPORTANTE: asegurarse que al evaluar la funcion, lo signos sean distintos.")
    a, b = leerInputs()
    
    dfResul, raiz = metodoFalsaPosicion(f1, a, b, n = 12)
    
    #Imprimir tabla con Pandas
    pd.set_option('display.float_format', '{:.4f}'.format)
    print("\nResultados del método de Falsa Posición:\n")
    print(dfResul.to_string(index=False))
    
    print(f"\nSolución del la ecuación lineal propuesta;  f(x) = 3x - (x+2)^2 * e^(-x) es: \n x ≈ {raiz:.4f}")
                           
    #Gráfica del método
    plt.figure(figsize=(8,5))
    plt.plot(dfResul["n"], dfResul["xn"], marker='*', linestyle='-', color='green')
    plt.title("Convergencia del Método de Falsa Posición", fontsize=14)
    plt.xlabel("Número de iteraciones", fontsize=12)
    plt.ylabel("xn (aprox. de raíz)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

