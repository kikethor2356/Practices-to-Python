"""
contador=0
miemail=input("Introduce tu email:")
for i in miemail:
	if (i=="@" or i=="."):
		contador=contador+1

if contador==2: 		
	print("Email es correcto")
else:
	print("El email no es correcto")	

for i in["primavera","verano","otoño","invierno"]:
	print("Hola",end=" ")
"""
valido=False

email=input("introduce tu email: ")

for i in range (len (email)):
	if email[i]=="@ and .":
		valido=True	
if valido:
	print("Email correcto")
else:
	print ("email incorrecto")		