from tkinter import*
import webbrowser
import cv2
import tensorflow
import numpy
import keras
#import dlib
from cafe1 import cafe
from voice_recognition import voice_command
from connect import chat

import _thread
from tkinter import *
 
import socket
import time
import select
import queue
from gui import*
import threading
from final_demostration.cctv import face
from tkinter import*

from capture import cap
from train_face import train
from recognition import recognize

###################################### CONNECTION#########################

def chat():
        ENCODING = 'utf-8'
        HOST = socket.gethostbyname(socket.gethostname())
        PORT = 8888


        class Client(threading.Thread):
            def __init__(self, host, port):
                super().__init__(daemon=True, target=self.run)

                self.host = host
                self.port = port
                self.sock = None
                self.connected = self.connect_to_server()
                self.buffer_size = 1024

                self.queue = queue.Queue()
                self.lock = threading.RLock()

                self.login = ''
                self.target = ''
                self.login_list = []

                if self.connected:
                    self.gui = GUI(self)
                    self.start()
                    self.gui.start()
                    # Only gui is non-daemon thread, therefore after closing gui app will quit

            def connect_to_server(self):
                """Connect to server via socket interface, return (is_connected)"""
                try:
                    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    self.sock.connect((str(self.host), int(self.port)))
                except ConnectionRefusedError:
                    print("Server is inactive, unable to connect")
                    messagebox.showinfo("Server not Activate","Please wait for Active Server")
                    return False
                return True

            def run(self):
                """Handle client-server communication using select module"""
                inputs = [self.sock]
                outputs = [self.sock]
                while inputs:
                    try:
                        read, write, exceptional = select.select(inputs, outputs, inputs)
                    # if server unexpectedly quits, this will raise ValueError exception (file descriptor < 0)
                    except ValueError:
                        print('Server error')

                        self.sock.close()
                        break

                    if self.sock in read:
                        with self.lock:
                            try:
                                data = self.sock.recv(self.buffer_size)
                            except socket.error:
                                print("Socket error")

                                self.sock.close()
                                break

                        self.process_received_data(data)

                    if self.sock in write:
                        if not self.queue.empty():
                            data = self.queue.get()
                            self.send_message(data)
                            self.queue.task_done()
                        else:
                            time.sleep(0.05)

                    if self.sock in exceptional:
                        print('Server error')

                        self.sock.close()
                        break

            def process_received_data(self, data):
                """Process received message from server"""
                if data:
                    message = data.decode(ENCODING)
                    message = message.split('\n')

                    for msg in message:
                        if msg != '':
                            msg = msg.split(';')

                            if msg[0] == 'msg':
                                text = msg[1] + ' >> ' + msg[3] + '\n'
                                print(msg)
                                self.gui.display_message(text)

                                # if chosen login is already in use
                                if msg[2] != self.login and msg[2] != 'ALL':
                                    self.login = msg[2]

                            elif msg[0] == 'login':
                                self.gui.main_window.update_login_list(msg[1:])

            def notify_server(self, action, action_type):
                """Notify server if action is performed by client"""
                self.queue.put(action)
                if action_type == "login":
                    self.login = action.decode(ENCODING).split(';')[1]
                elif action_type == "logout":
                    self.sock.close()

            def send_message(self, data):
                """"Send encoded message to server"""
                with self.lock:
                    try:
                        self.sock.send(data)
                    except socket.error:
                        self.sock.close()



        # Create new client with (IP, port)
        if __name__ == '__main__':
            Client(HOST, PORT)
 
 


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

 
root = Tk()

lbl=Label(root,font=("arial",20,"bold"),text="Online works")
lbl.place(x=300,y=200)

lb2=Label(root,font=("arial",10,"bold"),text="",bg="black",width=30)
lb2.place(x=300,y=250)
new = 1
url = "http://192.168.43.188:8123/states"

def openweb():
    webbrowser.open(url,new=new)

Btn = Button(root,font=("arial",20),text = "Home Automotion",command=openweb)
Btn.place(x=300,y=300)

url1 = "http://127.0.0.1:5000"

def openweb1():
    webbrowser.open(url1,new=new)

Btn = Button(root,font=("arial",20),text = "Neural Network Security",command=openweb1)
Btn.place(x=300,y=350)





root.geometry("1400x700")
root.title("Digital Cafe Billing With Face Recognition Security & Communication System")

label=Label(root,font=("arial",50,"bold"),text=("Cafe IceCream 249"))
label.pack()
Bill=Button(root,font=("arial",20),text=("Billing") ,command=cafe )
Bill.place(x=1100,y=250)

cctv=Button(root,font=("arial",20),text=("CCTV"),command=face)
cctv.place(x=1100,y=300)
voice_command=Button(root,font=('arial',20),text=("Voice Command"),command=voice_command,)
voice_command.place(x=1100,y=350)
Connect=Button(root,font=('arial',20),text=("Connect"),command=chat)
Connect.place(x=1100,y=400)




Help=Button(root,font=('arial',10),text=("help?"))
Help.place(x=1300,y=0)
about=Button(root,font=('arial',10),text=("About"))
about.place(x=5,y=670)

root.mainloop()
