from io import open 

archivo_text=open("archivo.txt","r+")
 #w=write, r=read and a=appen r+=lectura y escritura

archivo_text.seek(len(archivo_text.readline()))

#archivo_text.write("Comienzo del texto")
#print (archivo_text.readlines())

lista_texto=archivo_text.readlines()

lista:lista_texto[1]="Esta liena ha sido incluida desde el exterior\n"

archivo_text.seek(0)
archivo_text.writelines(lista_texto)
archivo_text.close()

"""
lineas_texto=archivo_text.readlines()

archivo_text.close()

print(lineas_texto[0])



texto=archivo_text.read()

archivo_text.close()
print (texto)

frase="Estupendo dia para estudiar Python \n el lunes"

archivo_text.write(frase)

archivo_text.close()
"""