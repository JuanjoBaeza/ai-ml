import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

peliculas = pd.read_csv("datasets/movies2.csv")
datos_numericos = peliculas.select_dtypes(np.number)
datos_numericos = peliculas.select_dtypes(np.number).fillna(0)

objetivo = "ventas"
#las variables independientes serian todas las demas menos ventas
independientes = datos_numericos.drop(columns=objetivo).columns

modelo = LinearRegression()
modelo.fit(X=datos_numericos[independientes], y=datos_numericos[objetivo])
	
peliculas["ventas_prediccion"] = modelo.predict(datos_numericos[independientes])

print (peliculas[["titulo", "ventas", "ventas_prediccion"]].head())