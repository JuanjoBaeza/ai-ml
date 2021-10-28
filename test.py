import numpy as np

# arrange (nº elementos) seguido de reshape crea matrices de N filas x M columnas  
x = np.arange(40).reshape(4, 10) # 40 elementos en una matriz de 4 filas x 10 col
print(x)