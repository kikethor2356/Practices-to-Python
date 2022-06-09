
edad=-3

if 0<edad<100:
	print("edad es correcta ")
else:
	print("edad no es correcta")	

#Concatenaciones con variables 

salario_presidente=int(input("Indroduce el salario del presidente"))
print("salario presidente:"+ str(salario_presidente))

salario_director=int(input("Indroduce el salario del director"))
print("salario director:"+ str(salario_director))

salario_jefe_area=int(input("Indroduce el salario del jefe de area"))
print("salario jefe de area:"+ str(salario_jefe_area))

salario_administrativo=int(input("Indroduce el salario de administrativo"))
print("salario administrativo:"+ str(salario_administrativo))

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo va bien en esta empresa")
else:
	print("Algo huele mal en esta empresa")	


print("PROGRAMA DE BECAS 2022")
distancia_escuela=int(input("Introduce la distancia en KM"))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos que tienes"))
print(numero_hermanos)

salrio_familiar=int(input("Introduce el salario anual bruto"))
print(salrio_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salrio_familiar<=20000:
	print("Tienes derecho a beca")
else:
		print("No tienes derecho a beca")	

#CONDICIONALES IN,AND,OR
print("asignaturas 2022")
print("Asignaturas optativas: Informatica grafica - Pruebas de software -Usabilidad y accesibilidad")		
opcion=input("Escribe la asignatura escogida:")
asignatura=opcion.lower()
if asignatura in ("informatica grafica","pruebas de software","usabilidad y accesibilidad "):
	print("Asignatura elegida " + asignatura)

else:
	print("La asiganatura no esta contemplada")	




