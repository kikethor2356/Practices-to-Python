from tkinter import*

raiz=Tk()

raiz.title("Ventana de pruebas")

#raiz.resizable(1,1)

raiz.iconbitmap("descarga.ico")

#raiz.geometry("650*350")

raiz.config(bg="red")
raiz.config(bd=55)
raiz.config(relief="groove")
raiz.config(cursor="hand2")

miFrame=Frame()
#miFrame.pack(side="left", anchor="s")
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="green")
miFrame.config(width="650", height="350")
miFrame.config(bd=45)
miFrame.config(relief="sunken ")
miFrame.config(cursor="pirate")
raiz.mainloop()
