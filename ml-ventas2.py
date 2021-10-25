import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# El campo edad = edad del cliente, cantidad = cantidad de personas que iban con esa persona, la columna vehiculo = si llegó o no en un vehículo particular, la columna pago se refiere a su forma de pago (efectivo, tarjeta de credito, débito o vales), y por último la columna monto que indica cuánto compró.
ventas = pd.read_csv("datasets/ventas2.csv")
objetivo = "importe"
independientes = ventas.drop(columns=['importe']).columns

modelo = LinearRegression()
modelo.fit(X=ventas[independientes], y=ventas[objetivo])

ventas["importe_prediccion"] = modelo.predict(ventas[independientes])
preds = ventas[["importe", "importe_prediccion"]].head(50)

# persona de 41 años, solo, en su propio vehículo y pagando en efectivo
talvez = modelo.predict([[47,3,1,1]])
print ("Importe de compra: ")
print (np.round(talvez,1) ,"€")

preds.plot(kind='bar',figsize=(18,8))
plt.grid(linewidth='2')
plt.grid(linewidth='2')
plt.grid(None)
plt.show()