class Coche():
#condtructor
	def __init__(self):
#propiedades
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enmarcha=False
#Comportamiento
	def arrancar(self, arrancamos):
		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			chequeo=self.__chequeo_interno()

		if(self.__enmarcha and chequeo):
			return"El coche esta en enmarcha"
		elif(self.__enmarcha and chequeo==False):
			return"Algo ha ido mal en el chequeo no podemos arrancar"
		else:
			return"El coche esta parado"	

	def estado(self):
		print("el coche tiene", self.__ruedas, "ruedas.Un ancho de",self.__anchoChasis,
			"y un largo de", self.__largoChasis)

	def __chequeo_interno(self):
		print("realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok"and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False		

#instancia		
micoche=Coche()


print(micoche.arrancar(True))
print(micoche.estado())
print("A continuacion el segundo objeto")

#instancia
micoche2=Coche()

print(micoche2.arrancar(False))
print(micoche2.estado())
