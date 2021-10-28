import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression 

# función f(x) = 0.1*x + 1.25 + 0.2*Ruido_Gaussiano [ y = w·x + b ]
def f(x):  
    np.random.seed(42)
    y = 0.1*x + 1.25 + 0.2*np.random.randn(x.shape[0])
    return y

# generamos valores x de 0 a 20 en intervalos de 0.5
x = np.arange(0, 20, 0.5) 

# calculamos y a partir de la función que hemos generado
y = f(x)

plt.scatter(x,y,label='data', color='blue')
plt.title('Datos')

#### Hasta aqui el dibujo de la Regresión Lineal ####

# creamos una instancia de LinearRegression
regresion_lineal = LinearRegression()

# instruimos a la regresión lineal que aprenda de los datos (x,y)
regresion_lineal.fit(x.reshape(-1,1), y) 

# vemos los parámetros que ha estimado la regresión lineal
print('Valor w = ' + str(regresion_lineal.coef_) + ', Valor b = ' + str(regresion_lineal.intercept_))

# vamos a predicir y = regresion_lineal(5)
nuevo_x = np.array([5]) 
prediccion = regresion_lineal.predict(nuevo_x.reshape(-1,1))
print('Valor de y =' + str(prediccion) + ' para un valor de x=5')