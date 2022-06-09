""""
i=1
while i<=10:
	print("ejecucion"+ str(i))
	i=i+1
print("Termino la ejecucion")	

edad=int(input("introduce una edad "))
while edad<5 or edad> 100:
	print("Has introducido la edad negativa ")
	edad=int(input("introduce una edad "))

print("Gracias por colaborar ")
print("Edad de usuario "+ str(edad))	
"""
import math
print ("Programa de calculo de raiz cuadrada")
numero=int(input("introduce numero"))

intentos =0
while numero<0:
	print("No se puede ejecutar")
	if intentos==2:
		print ("Has hecho demasiados intentos ")
		break;

	numero=int(input("introduce numero"))	
	if numero<0:
		intentos=intentos+1
if intentos <2:
	solucion =math.sqrt(numero)
	print("La raiz cuadrada de "+ str(numero)+ "es"+ str(solucion))		
