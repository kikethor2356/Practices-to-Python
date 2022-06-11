correo=input("Introduce tu correo")

arroba=correo.count("@")
while("Introduce de nuevo tu mail"):
	if (arroba!=1 or correo.rfind("@")==(len(correo)-1)or correo.find(".com")==0):
		print("Mail incorrecto")

else:
	print("Mail correcto")


imail=input("Introduce tu imail")
arroba=imail.count("@")

if (arroba!=1 or imail.rfind ("@")==(len(imail)-1)or imail.rfind(".com")==0):		
	print("Imail incorrecto")

else:
	print("Imail correcto")	
