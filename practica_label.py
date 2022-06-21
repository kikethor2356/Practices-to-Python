from tkinter import*

root=Tk()
root.title("Halo Mater Chief")
root.iconbitmap("descarga.ico")
root.config(bg="red")
root.config(bd=55)
root.config(relief="groove")
root.config(cursor="hand2")

miFrame=Frame(root, width=500, height=400)
#miFrame.pack(side="left", anchor="s")
miFrame.pack(fill="y", expand="True")
miFrame.config(bg="green")
miFrame.config(width="650", height="350")
miFrame.config(bd=45)
miFrame.config(relief="groove")
miFrame.config(cursor="pirate")
miImagen=PhotoImage(file="Halo.gif")



miLabel=Label(miFrame,image=miImagen).place(x=140 ,y=100)



root.mainloop()