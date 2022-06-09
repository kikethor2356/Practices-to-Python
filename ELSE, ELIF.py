print("verificacion de acceso")
nota_usuario=int(input("Introduce tu nota: "))
if nota_usuario<5:
 	print("Reprobado")
elif nota_usuario<6:
	print("Aprobado")
elif nota_usuario<8:	
	print("Notables")

else:	
	print("sobresaliente")

