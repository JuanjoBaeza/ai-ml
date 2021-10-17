import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# Formula:                Grados_Farenhait = Grados_Celsius x 1.8 + 32
# Formula función lineal: Y = m·x + b

celsius   = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenhait = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

capa   = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.1),
    loss = 'mean_squared_error'
)
print("Comenzando entrenamiento modelo...")
historial = modelo.fit(celsius, farenhait, epochs=1000, verbose=False)
print("Modelo entrenado")

plt.xlabel("Entrenamientos")
plt.ylabel("Pérdia")
plt.plot(historial.history["loss"])

resultado = modelo.predict([40])
print("El resultado es " + str(resultado) + " fahrenhait!")