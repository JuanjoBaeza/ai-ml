import numpy as np
import matplotlib.pyplot as plt

# reshape(-1, 1) formatea la matriz a n filas (arange) y 1 columna
x = np.arange(8).reshape(-1, 1) 
print(x)
print('\n')

# arrange (nº elementos) seguido de reshape crea matrices de N filas x M columnas  
x = np.arange(8).reshape(2, 4) # 8 elementos en una matriz de 2 filas x 4 col
print(x)
print('\n')

x = np.array([1, 3, 5, 7])
y = np.array([ 6, 3, 9, 5 ])

plt.plot(x, y, 'o')

m, b = np.polyfit(x, y, 1)

plt.plot(x, m*x + b)

plt.plot([1, 2, 3], [1, 2, 3])

print('\n')

########################### Matrices ##########################

n = 2
m = 4

matriz = [[0] * m] * n # Una matriz nula de n x m valores
print(matriz)
print('\n')

matriz[0][1] = 10 # Modifica solo el valor (0,1) ?? Mal modifica
print(matriz)
print('\n')

for i in range(0, n):
  matriz[i] = [0] * m # Una matriz nula de n x m valores
  print(matriz)
  print('\n')

matriz[0][1] = 10 # Modifica solo el valor (0,1)
print(matriz)