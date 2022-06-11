#nombreUsuario=input("introduce tu nombre de usuario:")
#print("El nombre de usuario es:", nombreUsuario.capitalize()) 


edad=input("Introduce la edad:")

#print(edad.isdigit())
while(edad.isdigit()==False):
	print("Por favor, introduce un valor numerico")

if (int(edad)<18):
	print("No puedes pasar")
else:
	print("Puedes pasar")