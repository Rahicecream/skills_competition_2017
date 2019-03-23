from tkinter import*
from capture import cap
from train_face import train
from recognition import recognize

def face():
    root=Tk()
    root.geometry("600x400")
    root.title("face recognition window")

    label=Label(root,font=('arial',20),text="Face Recognition system")
    add_person=Button(root,font=('arial',15,"bold"),text="add new face",height=1,command=cap)
    add_person.place(x=50,y=150)

    train_face=Button(root,font=('arial',15,"bold"),text="Load new faces",command=train)
    train_face.place(x=50,y=200)

    divider=Label(root,text="",bg="black",height=30,width=1)
    divider.place(x=300,y=100)

    recognition=Button(root,font=('arial',15,"bold"),text="Start Recognition",height=1,command=recognize)
    recognition.place(x=350,y=150)


     
    label.pack()
    root.mainloop()
