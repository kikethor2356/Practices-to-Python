class coche():

	def desplazamiento(self):
		print("Me desplazo en cuatro ruedas")

class moto():
	def desplazamiento(self):
		print("Me desplazo en dos ruedas")

class Camion():
	def desplazamiento(self):
		print("Me desplazo en seis ruedas")


def desplazamiento_vehiculo(vehiculo):
	vehiculo.desplazamiento()

miVehiculo=coche()

desplazamiento_vehiculo(miVehiculo)






