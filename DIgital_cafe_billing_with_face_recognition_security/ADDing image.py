from tkinter import*
app=Tk()
app.title("IceCream")
fname=Canvas(bg="black",height=600,width=900)
fname.pack(side=TOP)

image1=PhotoImage(file="Untitled-1.gif")
image=fname.create_image(200,50,image=image1)
fname.pack()
app.mainloop()
