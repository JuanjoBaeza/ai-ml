# Algoritmo de cuadrados medios

semilla = input("Escriba semilla: ")

tam1 = len(semilla)

print("Cantidad de dígitos: ", tam1)

numero1 = int(semilla)

for i in range(10):
	numero2 = numero1**2
	snumero2 = str(numero2)
    
	tam2 = len(snumero2)
	primerc = int((tam2 - tam1) / 2)
 
	snumero3 = snumero2[primerc:primerc+tam1]
	print ("{}.  {}".format(i,snumero3))
	numero1 = int(snumero3)