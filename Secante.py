'''
    Este programa implementa la solución que satisface 
    la ecuación 3x - (x+2)^2 * e^(-x) = 0 
    mediante el uso del método de la Secante
'''

import math
import pandas as pd
import matplotlib.pyplot as plt

#Definir una de las funciones
def f1(x):
    return (3*x) - pow(x+2, 2) * math.exp(-x)

def f2(x):
    return math.cos(x) + 2 * math.sin(x) + pow(x, 2)

def f3(x):
    return math.log(abs(x-1)) + math.cos(x-1)

#Función para validar inputs numéricos
def leerInput():
    while True:
        for i in range(0,1):
            #Solicitar inputs muestra
            xStr = input(f"Escriba el valor inicial de la entrada x{i}: ")
            #Validar si se recibe una entrada numérica
            try:
              return float(xStr)
            except ValueError:
              print("Error: La entrada debe ser un número válido.\n")

#Método de la Secante
def metodoSecante(f, x0, x1, n=20):
  datos = []  # Lista para almacenar los resultados
    
  # Cabeceras
  print("\n n |     xn    |   f(xn)")
  print("-----------------------------")

  # Bucle de iteraciones
  for i in range(1, n + 1):
        fx0 = f(x0)
        fx1 = f(x1)

        # Validar división por cero
        if fx1 - fx0 == 0:
            print(f"Error: División entre cero en la iteración {i}. No se puede continuar.")
            break

        # Aplicar la fórmula de la secante
        xn = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        fxn = f(xn)

        # Mostrar resultados por consola
        print(f"{i:2d} | {x0:10.6f} | {x1:10.6f} | {xn:10.6f} | {fxn:10.6f}")

        # Guardar datos para el DataFrame
        datos.append([i, x0, x1, xn, fxn])

        # Actualizar valores
        x0, x1 = x1, xn

  # Crear el DataFrame con los resultados
  df = pd.DataFrame(datos, columns=["n", "x0", "x1", "xn", "f(xn)"])
  return df

#main
def main():
    print("***MÉTODO DE LA SECANTE***\n")
    x0, x1 = leerInput()
    
    # Ejecutar método
    raiz = metodoSecante(f1, x0, x1, n=10)
    
    # Mostrar DataFrame completo
    df_resultados = raiz
    print("\nTabla de resultados:")
    print(df_resultados)
    pd.set_option('display.float_format', '{:.4f}'.format)
    print("\nResultados del método de la Secante:\n")
    print(df_resultados.to_string(index=False))
    
    # Mostrar valor final
    raiz = df_resultados["xn"].iloc[-1]
    print(f"\nLa solución aproximada es: x ≈ {raiz:.6f}")
    print(f"\nf(x) ≈ {f1(raiz):.6f}")
    
    # Gráfica para mostrar la convergencia del método
    plt.figure(figsize=(8, 5))
    plt.plot(df_resultados["n"], df_resultados["xn"], marker='*', linestyle='-', color='green')
    plt.title("Convergencia del método de la Secante", fontsize=14)
    plt.xlabel("Número de iteraciones", fontsize=12)
    plt.ylabel("Aproximación xn", fontsize=12)
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()