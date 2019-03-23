from tkinter import*
import time;
import random
import tkinter.messagebox
import cv2
import cv2,os
import numpy as np
from PIL import Image
import cv2
import numpy as np
from tkinter import*
import os
import wolframalpha,os
import speech_recognition as sr
import pyttsx3
import io
from tkinter import ttk
import base64
import turtle
import pyaudio
from pygame import mixer
import webbrowser
from time import localtime,strftime
import time

from tkinter import *   ## notice lowercase 't' in tkinter here
from urllib.request import urlopen
from urllib.request import urlopen
import _thread
from tkinter import font
from tkinter import messagebox
import socket
import time
import select
import queue
from gui import*
import threading


from icecream import rahi
root=Tk()

root.geometry("1600x800+0+0")
root.title("Digital Cafe Billing with Face Recognition Security & Comm5uinication System")
root.configure(background="#482F3C")

timepass=Frame(root,width=400,height=400,bg="#f18039",bd=50,relief=SUNKEN)
timepass.pack(side=RIGHT)
#-------------------------simple e basic button-----------------------------
def canteen():
        window1 = Toplevel(root)
        window1.geometry("1600x800+0+0")
        window1.title("Cafe Food Billing System")


        text_input = StringVar()
        operator ="0"

        Tops=Frame(window1,width = 1600,height=50,  bg= "gray", relief = SUNKEN)
        Tops.pack(side=TOP)

        f1=Frame(window1,width = 800, height= 700, bg= "gray", relief = SUNKEN)
        f1.pack(side=LEFT)

        f2=Frame(window1,width = 300,height= 700, bg= "gray", relief = SUNKEN)
        f2.pack(side=RIGHT)
        #===========================time=============================================
        localtime=time.asctime(time.localtime(time.time()))
        #===============================info===========================================
        rahi = Label(Tops, font=("arial",50,"bold"),text="Icecream Cafe 24",fg="steel Blue",bd=10,anchor="w")
        rahi.grid(row=0,column=0)

        rahi = Label(Tops, font=("arial",20,"bold"),text=localtime,fg="steel Blue",bd=10,anchor="w")
        rahi.grid(row=1,column=0)
        #++++++++++++++++++++++++++++variable++++++++++++
        rand=StringVar()
        Fries=StringVar()
        Singara=StringVar()
        Chips=StringVar()
        Seven_up=StringVar()
        Coffea=StringVar()
        Coffea_tea=StringVar()
        Barger=StringVar()
        Sandois=StringVar()
        Biriani=StringVar()
        Cake=StringVar()
        Total=StringVar()



        Fries.set("0")
        Singara.set("0")
        Seven_up.set("0")
        Coffea.set("0")
        Coffea_tea.set("0")
        Barger.set("0")
        Sandois.set("0")
        Biriani.set("0")
        Cake.set("0")
        Chips.set("0")
        #=============================calculator======================================
        def btnClick(numbers):
            global operator
            operator=operator + str(numbers)
            text_input.set(operator)

        def btnClearDisplay():
            global operator
            operator=""
            text_input.set("")

        def btnEqualsInput():
            global operator
            sumup=str(eval(operator))
            text_input.set(sumup)
            operator=""

        def Ref():
            x= random.randint(1,1000)
            randomRef=str(x)
            rand.set(randomRef)

            fries=float(Fries.get())
            singara=float(Singara.get())
            chips=float(Chips.get())
            sevenup=float(Seven_up.get())
            coffea=float(Coffea.get())
            coffeatea=float(Coffea_tea.get())
            barger=float(Barger.get())
            sandois=float(Sandois.get())
            biriani=float(Biriani.get())
            cake=float(Cake.get())

            cost_fries=fries*100.00                  #fries= 120
            cost_singara=singara*5.00                #singara=5
            cost_chips=chips*10.00                    #chips=10
            cost_sevenup=sevenup*30.00                #sevenup=30
            cost_coffea=coffea*20.00                   #coffea=20
            cost_coffea_tea=coffeatea*10.00            #coffeatea=10
            cost_barger=barger*50.00                   #bargar=50
            cost_sandois=sandois*60.00                 #sandois=60
            cost_biriani=biriani*200.00                #biriani=200
            cost_cake=cake*25.00                       #cake=25

            totalcost="Taka",str("%.2f" %(cost_fries + cost_singara +cost_chips+cost_sevenup + cost_coffea + cost_coffea_tea + cost_barger + cost_sandois + cost_biriani + cost_cake))

            Total.set(totalcost)




        def qExit():
            window1.destroy()

        def Reset():
            rand.set("0")
            Fries.set("0")
            Singara.set("0")
            Chips.set("0")
            Seven_up.set("0")
            Coffea.set("0")
            Coffea_tea.set("0")
            Barger.set("0")
            Sandois.set("0")
            Biriani.set("0")
            Cake.set("0")
            Total.set("0")



        txtriya = Entry(f2,font=("arial",20,"bold"),text=text_input,bd=30,insertwidth=4,bg="powder blue", justify="right")
        txtriya.grid(columnspan=4)

        btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=2,column=0)

        btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=("arial",20,"bold"),text="8",bg="powder blue",command=lambda:btnClick(8)).grid(row=2,column=1)

        btn9=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="9",bg="powder blue",command= lambda:btnClick(9)).grid(row=2,column=2)

        btnaddition=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="+",bg="powder blue",command= lambda:btnClick("+")).grid(row=2,column=3)

        btn4=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="4",bg="powder blue",command= lambda:btnClick(4)).grid(row=3,column=0)

        btn5=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="5",bg="powder blue",command= lambda:btnClick(5)).grid(row=3,column=1)

        btn6=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="6",bg="powder blue",command= lambda:btnClick(6)).grid(row=3,column=2)

        btn_subtraction=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="-",bg="powder blue",command= lambda:btnClick("-")).grid(row=3,column=3)

        btn1=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="1",bg="powder blue",command= lambda:btnClick(1)).grid(row=4,column=0)

        btn2=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="2",bg="powder blue",command= lambda:btnClick(2)).grid(row=4,column=1)

        btn3=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="3",bg="powder blue",command= lambda:btnClick(3)).grid(row=4,column=2)

        btnMultiply=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="*",bg="powder blue",command= lambda:btnClick("*")).grid(row=4,column=3)

        btn0=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="0",bg="powder blue",command= lambda:btnClick(0)).grid(row=5,column=0)

        btnClear=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="C",bg="powder blue",command =btnClearDisplay).grid(row=5,column=1)

        btnEqual=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="=",bg="powder blue",command=btnEqualsInput).grid(row=5,column=2)

        btnDivision=Button(f2,padx=16,pady=16,bd=8,fg="black",font=("airal",20,"bold"),text="/",bg="powder blue",command= lambda:btnClick("/")).grid(row=5,column=3)


        #_____________________________





        #______________________________Cantean info__________________________________________________________________________________________________________________________




        lblFries = Label(f1,font=("airal",16,"bold"),text="Large Fries",bd=6,anchor="w")
        lblFries.grid(row=1,column=0)

        txtFries=Entry(f1,font=("airal",16,"bold"),textvariable=Fries,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtFries.grid(row=1,column=1)

        lblSingara = Label(f1,font=("airal",16,"bold"),text="Singara",bd=6,anchor="w")
        lblSingara.grid(row=2,column=0)

        txtSingara=Entry(f1,font=("airal",16,"bold"),textvariable=Singara,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtSingara.grid(row=2,column=1)

        lblSeven_up = Label(f1,font=("airal",16,"bold"),text="7up",bd=6,anchor="w")
        lblSeven_up.grid(row=3,column=0)

        txtSeven_up=Entry(f1,font=("airal",16,"bold"),textvariable=Seven_up,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtSeven_up.grid(row=3,column=1)

        lblCoffea = Label(f1,font=("airal",16,"bold"),text="Coffea",bd=6,anchor="w")
        lblCoffea.grid(row=4,column=0)

        txtCoffea=Entry(f1,font=("airal",16,"bold"),textvariable=Coffea,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtCoffea.grid(row=4,column=1)

        lblChips = Label(f1,font=("airal",16,"bold"),text="Chips",bd=6,anchor="w")
        lblChips.grid(row=5,column=0)

        txtChips=Entry(f1,font=("airal",16,"bold"),textvariable=Chips,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtChips.grid(row=5,column=1)

        lblCoffea_tea = Label(f1,font=("airal",16,"bold"),text="Coffea Tea",bd=6,anchor="w")
        lblCoffea_tea.grid(row=0,column=2)

        txtCoffea_tea=Entry(f1,font=("airal",16,"bold"),textvariable=Coffea_tea,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtCoffea_tea.grid(row=0,column=3)

        lblBarger = Label(f1,font=("airal",16,"bold"),text="Barger",bd=6,anchor="w")
        lblBarger.grid(row=1,column=2)

        txtBarger=Entry(f1,font=("airal",16,"bold"),textvariable=Barger,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtBarger.grid(row=1,column=3)

        lblSandois = Label(f1,font=("airal",16,"bold"),text="Sandois",bd=6,anchor="w")
        lblSandois.grid(row=2,column=2)

        txtSandois=Entry(f1,font=("airal",16,"bold"),textvariable=Sandois,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtSandois.grid(row=2,column=3)

        lblBiriani = Label(f1,font=("airal",16,"bold"),text="Biriani",bd=6,anchor="w")
        lblBiriani.grid(row=3,column=2)

        txtBiriani=Entry(f1,font=("airal",16,"bold"),textvariable=Biriani,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtBiriani.grid(row=3,column=3)

        lblCake = Label(f1,font=("airal",16,"bold"),text="Cake",bd=6,anchor="w")
        lblCake.grid(row=4,column=2)

        txtCake=Entry(f1,font=("airal",16,"bold"),textvariable=Cake,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtCake.grid(row=4,column=3)

        lblTotalcost = Label(f1,font=("airal",16,"bold"),text="Total Cost",bd=6,anchor="w")
        lblTotalcost.grid(row=5,column=2)

        txtTotalcost=Entry(f1,font=("airal",16,"bold"),textvariable=Total,bd=10,insertwidth=4,bg="powder blue",justify="right")
        txtTotalcost.grid(row=5,column=3)


        #----------------------------Button----------------------------------------------
        btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("airal",16,"bold"),width=10,text="Total",bg="powder blue",command = Ref).grid(row=7,column=1)

        btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("airal",16,"bold"),width=10,text="Reset",bg="powder blue",command = Reset).grid(row=7,column=2)

        btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=("airal",16,"bold"),width=10,text="Exit",bg="powder blue",command = qExit).grid(row=7,column=3)




        # def canteen():
#
#         from Source import canteen_managment.py

def chat():

                pass






def cafe_():




        window2=Toplevel(root)
        window2.geometry("1350x750+0+0")
        window2.title("Ice Cream Cafe 24")
        window2.configure(background="steel Blue")

        Tops=Frame(window2,width=1350, height= 100, bd= 14, relief= "raise")
        Tops.pack(side=TOP)

        f1=Frame(window2,width=900,height=650,bd=8,relief="raise")
        f1.pack(side=LEFT)

        f2=Frame(window2,width=440,height=650,bd=8,relief="raise")
        f2.pack(side=RIGHT)


        f1a=Frame(f1,width=900,height=330,bd=8,relief="raise")
        f1a.pack(side=TOP)

        f2a=Frame(f1,width=900,height=320,bd=6,relief="raise")
        f2a.pack(side=BOTTOM)

        ft2=Frame(f2,width=440,height=450,bd=12,relief="raise")
        ft2.pack(side=TOP)

        fb2=Frame(f2,width=400,height=250,bd=16,relief="raise")
        fb2.pack(side=BOTTOM)

        f1aa=Frame(f1a,width=400,height=330,bd=16,relief="raise")
        f1aa.pack(side=LEFT)

        f1ab=Frame(f1a,width=400,height=330,bd=16,relief="raise")
        f1ab.pack(side=RIGHT)

        f2aa=Frame(f2a,width=450,height=330,bd=14,relief="raise")
        f2aa.pack(side=LEFT)


        Tops.configure(background="steel Blue")
        f1.configure(background="steel Blue")
        f2.configure(background="steel Blue")

        #++++++++++++++++++++++++++++++++cost of Iteam++++++++++++++++++++++++++++++++++++++++++
        def CostofItem():

            Item1=float(E_Icecream1.get())
            Item2=float(E_Icecream2.get())
            Item3=float(E_Icecream3.get())
            Item4=float(E_Icecream4.get())
            Item5=float(E_Icecream5.get())
            Item6=float(E_Icecream6.get())
            Item7=float(E_Icecream7.get())
            Item8=float(E_Icecream8.get())
            Item9=float(E_Icecream9.get())
            Item10=float(E_Icecream10.get())
            Item11=float(E_Icecream11.get())
            Item12=float(E_Icecream12.get())
            Item13=float(E_Icecream13.get())
            Item14=float(E_Icecream14.get())
            Item15=float(E_Icecream15.get())
            Item16=float(E_Icecream16.get())

            totalofcost=((Item1 * 10 ) + ( Item2 * 10)+(Item3*10) +(Item4 * 10)+ (Item5 * 10)+(Item6 *10) + (Item7 * 10) + (Item8 *10)+(Item9 * 10)+(Item10 * 10)+(Item11 * 10) +(Item12 * 10)+ \
                       (Item13 * 10) +(Item14 * 10) +(Item15*10) +(Item16 *10))

            costtotal="Taka",str("%.2f"%(totalofcost))
            TotalCost.set(costtotal)




            #===============================functional command==============================
        def qExit():


                window2.destroy()
                return

        def Reset():

            TotalCost.set("")
            txtReceipt.delete("1.0",END)
            E_Icecream1.set("0")
            E_Icecream2.set("0")
            E_Icecream3.set("0")
            E_Icecream4.set("0")
            E_Icecream5.set("0")
            E_Icecream6.set("0")
            E_Icecream8.set("0")
            E_Icecream9.set("0")
            E_Icecream10.set("0")
            E_Icecream11.set("0")
            E_Icecream12.set("0")
            E_Icecream13.set("0")
            E_Icecream14.set("0")
            E_Icecream15.set("0")
            E_Icecream16.set("0")

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)

            txt1.configure(state=DISABLED)
            txt2.configure(state=DISABLED)
            txt3.configure(state=DISABLED)
            txt4.configure(state=DISABLED)
            txt5.configure(state=DISABLED)
            txt6.configure(state=DISABLED)
            txt7.configure(state=DISABLED)
            txt8.configure(state=DISABLED)
            txt9.configure(state=DISABLED)
            txt10.configure(state=DISABLED)
            txt11.configure(state=DISABLED)
            txt12.configure(state=DISABLED)
            txt13.configure(state=DISABLED)
            txt14.configure(state=DISABLED)
            txt15.configure(state=DISABLED)
            txt16.configure(state=DISABLED)


        def Receipt():
            txtReceipt.delete("1.0",END)
            x= random.randint(100,100000)
            randomRef= str(x)
            Receipt_Ref.set("BILL" + randomRef)


            txtReceipt.insert(END,"Items\t\t\t\t\t" + "Cost of Items \n\n")
            txtReceipt.insert(END, "Icecream1 : \t\t\t\t\t" + E_Icecream1.get() + "\n")
            txtReceipt.insert(END,"Icecream2  : \t\t\t\t\t" + E_Icecream2.get() +"\n")
            txtReceipt.insert(END,"Icecream3  : \t\t\t\t\t" + E_Icecream3.get() +"\n")
            txtReceipt.insert(END,"Icecream4  : \t\t\t\t\t" + E_Icecream4.get() +"\n")
            txtReceipt.insert(END,"Icecream5  : \t\t\t\t\t" + E_Icecream5.get() +"\n")
            txtReceipt.insert(END,"Icecream6  : \t\t\t\t\t" + E_Icecream6.get() +"\n")
            txtReceipt.insert(END,"Icecream7  : \t\t\t\t\t" + E_Icecream7.get() +"\n")
            txtReceipt.insert(END,"Icecream8  : \t\t\t\t\t" + E_Icecream8.get() +"\n")
            txtReceipt.insert(END,"Icecream9  : \t\t\t\t\t" + E_Icecream9.get() +"\n")
            txtReceipt.insert(END,"Icecream10  : \t\t\t\t\t" + E_Icecream11.get() +"\n")
            txtReceipt.insert(END,"Icecream12  : \t\t\t\t\t" + E_Icecream12.get() +"\n")
            txtReceipt.insert(END,"Icecream13  : \t\t\t\t\t" + E_Icecream13.get() +"\n")
            txtReceipt.insert(END,"Icecream14 : \t\t\t\t\t" + E_Icecream14.get() +"\n")
            txtReceipt.insert(END,"Icecream15 : \t\t\t\t\t" + E_Icecream15.get() +"\n")
            txtReceipt.insert(END,"Icecream16  : \t\t\t\t\t" + E_Icecream16.get() +"\n")

            txtReceipt.insert(END,"TOTAL COST :\t\t\t\t\t\t " + TotalCost.get() +"\n")
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

        lblInfo=Label(Tops,font=("arial",70,"bold"),text="Cafe Icecream 24",fg="brown",bd=10,)
        lblInfo.grid(row=0,column=0)

        #======= =====================================CheckButton=========================================
        def chkbutton_value():
            if (var1.get()==1):
                txt1.configure(state=NORMAL)
            elif var1.get()==0:
                txt1.configure(state=DISABLED)
                E_Icecream1.set("0")

            if (var2.get()==1):
                txt2.configure(state=NORMAL)
            elif var2.get()==0:
                txt2.configure(state=DISABLED)
                E_Icecream2.set("0")

            if (var3.get()==1):
                txt3.configure(state=NORMAL)
            elif var3.get()==0:
                txt3.configure(state=DISABLED)
                E_Icecream3.set("0")

            if (var4.get()==1):
                txt4.configure(state=NORMAL)
            elif var4.get()==0:
                txt4.configure(state=DISABLED)
                E_Icecream4.set("0")

            if (var5.get()==1):
                txt5.configure(state=NORMAL)
            elif var5.get()==0:
                txt5.configure(state=DISABLED)
                E_Icecream5.set("0")

            if (var6.get()==1):
                txt6.configure(state=NORMAL)
            elif var6.get()==0:
                txt6.configure(state=DISABLED)
                E_Icecream6.set("0")

            if (var7.get()==1):
                txt7.configure(state=NORMAL)
            elif var7.get()==0:
                txt7.configure(state=DISABLED)
                E_Icecream7.set("0")

            if (var8.get()==1):
                txt8.configure(state=NORMAL)
            elif var8.get()==0:
                txt8.configure(state=DISABLED)
                E_Icecream8.set("0")

            if (var9.get()==1):
                txt9.configure(state=NORMAL)
            elif var9.get()==0:
                txt9.configure(state=DISABLED)
                E_Icecream9.set("0")

            if (var10.get()==1):
                txt10.configure(state=NORMAL)
            elif var10.get()==0:
                txt10.configure(state=DISABLED)
                E_Icecream10.set("0")

            if (var11.get()==1):
                txt11.configure(state=NORMAL)
            elif var11.get()==0:
                txt11.configure(state=DISABLED)
                E_Icecream11.set("0")

            if (var12.get()==1):
                txt12.configure(state=NORMAL)
            elif var12.get()==0:
                txt12.configure(state=DISABLED)
                E_Icecream12.set("0")

            if (var13.get()==1):
                txt13.configure(state=NORMAL)
            elif var13.get()==0:
                txt13.configure(state=DISABLED)
                E_Icecream13.set("0")

            if (var14.get()==1):
                txt14.configure(state=NORMAL)
            elif var14.get()==0:
                txt14.configure(state=DISABLED)
                E_Icecream14.set("0")

            if (var15.get()==1):
                txt15.configure(state=NORMAL)
            elif var15.get()==0:
                txt15.configure(state=DISABLED)
                E_Icecream15.set("0")

            if (var16.get()==1):
                txt16.configure(state=NORMAL)
            elif var16.get()==0:
                txt16.configure(state=DISABLED)
                E_Icecream16.set("0")





            #================================================= Variables================

        var1=IntVar()
        var2=IntVar()
        var3=IntVar()
        var4=IntVar()
        var5=IntVar()
        var6=IntVar()
        var7=IntVar()
        var8=IntVar()
        var9=IntVar()
        var10=IntVar()
        var11=IntVar()
        var12=IntVar()
        var13=IntVar()
        var14=IntVar()
        var15=IntVar()
        var16=IntVar()


        Receipt_Ref=StringVar()
        TotalCost=StringVar()


        E_Icecream1=StringVar()
        E_Icecream2=StringVar()
        E_Icecream3=StringVar()
        E_Icecream4=StringVar()
        E_Icecream5=StringVar()
        E_Icecream6=StringVar()
        E_Icecream7=StringVar()
        E_Icecream8=StringVar()
        E_Icecream9=StringVar()
        E_Icecream10=StringVar()
        E_Icecream11=StringVar()
        E_Icecream12=StringVar()
        E_Icecream13=StringVar()
        E_Icecream14=StringVar()
        E_Icecream15=StringVar()
        E_Icecream16=StringVar()


        E_Icecream1.set("0")
        E_Icecream2.set("0")
        E_Icecream3.set("0")
        E_Icecream4.set("0")
        E_Icecream5.set("0")
        E_Icecream6.set("0")
        E_Icecream7.set("0")
        E_Icecream8.set("0")
        E_Icecream9.set("0")
        E_Icecream10.set("0")
        E_Icecream11.set("0")
        E_Icecream12.set("0")
        E_Icecream13.set("0")
        E_Icecream14.set("0")
        E_Icecream15.set("0")
        E_Icecream16.set("0")



        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



        Latta= Checkbutton(f1aa,text="Icecream1 \t",bg="red",variable=var1,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=0,sticky=W)

        Espresso=Checkbutton(f1aa,text="Icecream2 \t",bg="green",variable=var2,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=1,column=0)

        Iced_Late= Checkbutton(f1aa,text="Icecream3 \t",bg="brown",variable=var3,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=2,column=0)

        Vale_Coffee=Checkbutton(f1aa,text="Icecream4 \t",bg="powder blue",variable=var4,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=3,column=0)

        Cappuccino= Checkbutton(f1aa,text="Icecream5 \t",bg="yellow",variable=var5,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=4,column=0)

        African_Coffee=Checkbutton(f1aa,text="Icecream6 \t",bg="blue",variable=var6,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=5,column=0)

        American_Coffee= Checkbutton(f1aa,text="Icecream7 \t",bg="gray",variable=var7,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=6,column=0)

        Iced_Cappuccino=Checkbutton(f1aa,text="Icecream8 \t",bg="orange red",variable=var8,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=7,column=0)

        CoffeeCake= Checkbutton(f1ab,text="Icecream9 \t",bg="salmon1",variable=var9,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=0,column=1)


        Red_Velvet_Cake= Checkbutton(f1ab,text="Icecream10 \t",bg="seaGreen",variable=var10,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=1,column=1)

        Black_Forest_Cake=Checkbutton(f1ab,text="Icecream11 \t",bg="sandy brown",variable=var11,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=2,column=1)

        Boston_Cream_Cake= Checkbutton(f1ab,text="Icecream12 \t",bg="dark olive green",variable=var12,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=3,column=1)

        Lagos_Chocolate_Cake=Checkbutton(f1ab,text="Icecream13 \t",bg="LightPink",variable=var13,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=4,column=1)

        Kilburn_Chocolate_Cake= Checkbutton(f1ab,text="Icecream14 \t",bg="turquoise1",variable=var14,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=5,column=1)

        Carlton_Hill_Cake=Checkbutton(f1ab,text="Icecream15 \t",bg="medium spring green",variable=var15,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=6,column=1)

        Queen_Park_Cake= Checkbutton(f1ab,text="Icecream16 \t",bg="orange",variable=var16,onvalue=1,offvalue=0,
                                  font=("arial",18,"bold"),command=chkbutton_value).grid(row=7,column=1)

            #=======================================Entry for food===============================
        txt1=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream1,state= DISABLED)
        txt1.grid(row=0,column=1)

        txt2=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream2,state= DISABLED)
        txt2.grid(row=1,column=1)

        txt3=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream3,state= DISABLED)
        txt3.grid(row=2,column=1)

        txt4=Entry(f1aa,font=("arial", 16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream4,state= DISABLED)
        txt4.grid(row=3,column=1)

        txt5=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream5,state= DISABLED)
        txt5.grid(row=4,column=1)

        txt6=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream6,state=DISABLED)
        txt6.grid(row=5,column=1)

        txt7=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream7,state= DISABLED)
        txt7.grid(row=6,column=1)

        txt8=Entry(f1aa,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream8,state= DISABLED)
        txt8.grid(row=7,column=1)


        txt9=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream9,state= DISABLED)
        txt9.grid(row=0,column=2)

        txt10=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream10,state= DISABLED)
        txt10.grid(row=1,column=2)

        txt11=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream11,state= DISABLED)
        txt11.grid(row=2,column=2)

        txt12=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream12,state= DISABLED)
        txt12.grid(row=3,column=2)

        txt13=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream13,state= DISABLED)
        txt13.grid(row=4,column=2)

        txt14=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream14,state= DISABLED)
        txt14.grid(row=5,column=2)

        txt15=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream15,state= DISABLED)
        txt15.grid(row=6,column=2)

        txt16=Entry(f1ab,font=("arial",16,"bold"),bd=8,width=6,justify="left",textvariable=E_Icecream16,state= DISABLED)
        txt16.grid(row=7,column=2)
        #___________________________________________________________
        lblTotalCost=Label(f2aa,font=("arial",16,"bold"),text="Total Cost",bd=8)
        lblTotalCost.grid(row=3,column=3)


        txtTotalCost=Entry(f2aa,font=("arial",20,"bold"),bd=8,justify="left",textvariable=TotalCost)
        txtTotalCost.grid(row=3,column=4,sticky=W)


        #=============================information=====================================
        lblReceipt= Label(ft2,font=("arial",12,"bold"),text="Receipt",bd=2).grid(row=0,column=0,sticky=W)

        txtReceipt=Text(ft2, width=59,height=22,fg="saddle brown",bg="white",bd=8,font=("arial",11,"bold"))
        txtReceipt.grid(row=1,column=0)

            #=======================================iteam information====================



            #======================================payment infomation==============

            #=============================Button===================================

        btnTotal= Button(fb2,padx=16,pady=1,bd=4,fg="steel Blue",font=("arial",16,"bold"),width=5,
                            text="Total",command=CostofItem).grid(row=0,column=0)


        btnReceipt=Button(fb2,padx=16,pady=1,bd=4,fg="steel Blue",font=("arial",16,"bold"),width=5,
                              text="Receipt",command=Receipt).grid(row=0,column=1)

        btnReset=Button(fb2,padx=16,pady=1,bd=4,fg="steel Blue",font=("arial",16,"bold"),width=5,
                            text="Reset",command=Reset).grid(row=0,column=2)

        btnExit=Button(fb2,padx=16,pady=1,bd=4,fg="steel Blue",font=("arial",16,"bold"),width=5,
                           text="Exit",command= qExit).grid(row=0,column=3)

#######################################################VOICE RECOGNITION #################################################################################
def voice_command():
        try:





                window5=Toplevel(root)
                window5.configure(background="steel Blue")
                window5.title("Artificial Intellegence - Icecream")
                window5.state('zoomed')
                #________________________________calling function____________________
                def quit():
                        window5.destroy()
                        return

                def update_text(userinput_text):
                        print ("update text")
                        label_input['text']=userinput_text

                def get_answer(question):
                        def speak(text):
                            engine = pyttsx3.init()
                            engine.say(text)
                            update_text(text)
                            engine.runAndWait()



                        app_id='' # wolframalpha app ID



                        if ("restart") in question:
                            pass

                        if ("exit") in question:

                                rand = ['Goodbye Sir', 'Icecream powering off in 3, 2, 1, 0']
                                speak(rand)
                                quit()
                        if ('hello') in question or ('hi') in question:
                                rand = ('Wellcome to icecream intelligence project. At your service sir.')
                                speak(rand)
                        if ('thanks') in question or ('tanks') in question or ('thank you') in question:
                                    rand = ['You are wellcome', 'no problem']
                                    speak(rand)
                        if  ("ice cream") in question or("icecream")in question or ("Icecream")in question:

                                speak('Yes Sir? ,What can I doo for you sir?')

                        if  ('how are you') in question or ('and you') in question or ('are you okay') in question:
                                    rand = ['Fine thank you']
                                    speak(rand)
                        if  ('*') in question:
                                    rand = ['Be polite please']
                                    speak(rand)
                        if ('your name') in question:
                                    rand = ['My name is Icecream, at your service sir']
                                    speak(rand)
                        if ('.com') in question :
                                    rahi = ['Opening' + question]
                                    Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
                                    speak(rahi)
                                    webbrowser.get(Chrome).open('http://www.'+question)
                                    print ('')
                        if  ("where")  in question:
                                    query = question
                                    stopwords = ['google', 'maps']
                                    querywords = query.split()
                                    resultwords  = [word for word in querywords if word.lower() not in stopwords]
                                    result = ' '.join(resultwords)
                                    Chrome = ("C:/Program Files (x86)/Google/Firefox/Application/firefox.exe %s")
                                    webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
                                    rand = [result+'on google maps']
                                    speak(rand)
                        if ('install') in question:
                                    query = question
                                    stopwords = ['install']
                                    querywords = query.split()
                                    resultwords  = [word for word in querywords if word.lower() not in stopwords]
                                    result = ' '.join(resultwords)
                                    rand = [('installing '+result)]
                                    speak(rand)
                                    os.system('python -m pip install ' + result)
                        if ('sleep mode') in question:
                                    rand = ['good night']
                                    speak(rand)
                                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                        if ('what time') in question:
                                    tim = strftime("%X", localtime())
                                    rand = [tim]
                                    speak(rand)
                        if  ("online") in question:
                                    speak("yes sir,Icecream is now in Active")
                                    speak("Starting all system application")
                                    speak("installing all divers")
                                    speak("every diver is installed")
                                    speak("all system have been started")
                                    speak("now I am online sir")
                        if ("Internet") in question:
                                internetexplorer()
                        if ("Firefox") in question:
                                    speak(" I heard you")
                                    speak("finding firefox application")
                                    speak("configuring all required files")
                                    speak("starting mozilla firefox")
                                    os.system("start firefox.exe")
                        if ("Notepad") in question:
                                    speak("ok sir")
                                    speak("requested application is text editor")
                                    speak("joining required files")
                                    speak("starting notepad")
                                    os.system("start notepad.exe")
                        if ("python")in question:

                                    speak("start python.exe")
                                    speak("python is opening")
                                    os.system("start python.exe")

                        if ("find") in question:
                            speak("start chrome.exe")
                            speak("what do i search for you sir")
                            webbrowser.open_new_tab("http://google.com/?q=%s"%question)
                            speak("okay searching")
                        if ("open") in question:
                                speak("opening gallary")
                                os.startfile("c:/users/zanja/Desktop/Icecream\dataSet")
                        if ("madarchod") in question:
                                speak("apni madarchot sir, akta mechiner sathe vhalo babohar korun")









                        if question=="who are you" or question=="what is your name":
                                speak("I am Icecream, I am a Artificial Intellegence")

                        else:


                                try:

                                    client = wolframalpha.Client(app_id)
                                    res = client.query(question)
                                    for pod in res.pods:

                                        for sub in pod.subpods:
                                            print(sub)
                                                # print(next(res.results).text)
                                        print ('$$$$$$$$$$$$$$$$$$$$$$$')

                                        print(next(res.results).text)
                                        speak=next(res.results).text
                                except:
                                        speak("Say something")



                def audio():
                        doss=os.getcwd()

                        button_activate['text']="IceCream Activated."
                        button_activate['state']='disabled'
                        pb.start()
                        while True:
                                def speak(text):
                                    engine = pyttsx3.init()
                                    engine.say(text)
                                    update_text(text)
                                    engine.runAndWait()
                                    # Record Audio
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                    audio = r.adjust_for_ambient_noise(source)

                                    print("Say something!")
                                    speak("Welcome to Team IceCream Intellegence Project")
                                    userinput="Welcome to Team IceCream Intellegence Project"
                                    speak("How can I help you , sir?")
                                    userinput="How can I help you,sir?"
                                    userinput= "Say Something..."
                                    update_text(userinput)
                                    audio = r.listen(source)

                                    # Speech recognition using Google Speech Recognition
                                try:

                                        # tanother API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

                                    userinput=r.recognize_google(audio)
                                    print("You said: " + userinput)
                                    update_text(userinput)

                                    get_answer(userinput)


                                except sr.UnknownValueError:
                                    print("Google Speech Recognition could not understand audio")
                                    userinput="Google Speech Recognition could not understand audio"
                                except sr.RequestError as e:
                                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                                    userinput="Could not request results from Google Speech Recognition service; {0}".format(e)
                                # update_text(userinput)
                def performanceBoost():
                                # update_text("Activating voice recognization...")
                        t1=_thread.start_new_thread( update_text, ("Say Something..", ) )
                        t2=_thread.start_new_thread( audio,())

                frame1=Frame(window5,height=330, width=660,borderwidth=2,relief=RIDGE,bg='#030719',highlightbackground='white')
                frame1.pack()
                frame1.place(relx=0.3, rely=0.4)

                label_input=Label(frame1, text="",font='Verdana 8 bold',fg='#0C90F2',bg='#030719', wraplength=600)
                label_input.pack(anchor=W)
                label_input.place(relx=0.5, rely=0.5, anchor=CENTER)


                button_activate=Button(window5,text="Activate",command=performanceBoost,width=15,justify='center',borderwidth=4,font='Verdana 8 bold')
                button_activate.pack(anchor=W)
                button_activate.place(relx=0.5, rely=0.2, anchor=CENTER)

                pb = ttk.Progressbar(frame1, orient="horizontal", length=660, mode="determinate")
                pb.pack()
                pb.place(rely=0.95)



        except:
                messagebox.showinfo("Warning","First please secure Internet connection")

def cctv():

        def capture():
                import capture
        def trainer():
                import train_face

        def recognition():
                import recognition






        def EXIT():
            window7.destroy()
        def open():
            os.startfile("c:/users/zanja/Desktop/Icecream\dataSet")



        #making frames
        window7=Toplevel(root)
        window7.minsize(width=600,height=400)

        f2 = Frame(window7,width=600, heigh=400 ,bd=20,bg='#a0db8e',relief=SUNKEN)
        f2.pack(side=LEFT)






        #making label



        #making buttons

        btn0 = Button(window7,padx=16,pady=8 , fg='black', font=('arail',16,'bold'),
                                             width=15, text='Capture Face', bg='red',command = capture).place(x=50,y=100)

        btn1 = Button(window7,padx=16,pady=8, fg='black', font=('arail',16,'bold'),
                                             width=15, text='Save Faces', bg='red2',command = trainer).place(x=50,y=200)


        btn2 = Button(window7,padx=16,pady=8, fg='black', font=('arail',16,'bold'),
                                             width=15, text='Start Detection', bg='red',command = recognition).place(x=325,y=100)

        btn3 = Button(window7,padx=16,pady=8 , fg='black', font=('arail',16,'bold'),
                                             width=10, text='Exit', bg='red2',command = EXIT).place(x=350,y=300)

        btn3 = Button(window7,padx=16,pady=8,fg='black',font=('arail',16,'bold'),
                                             width=15, text='Gellary', bg='red2',command = open).place(x=325,y=200)


########################################################################################################################################################
                                                           #START FOR COMMUINICATION
###########################################################################################################################################################

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




#now function for cafe_food
rahi=Button(timepass,padx=20,pady=10,fg="brown",font=("arial",20,"bold"),width=15,text="light1 off",bg="orange red").grid(row=3,column=0)



cctv=Button(timepass,padx=20,pady=10,fg="brown",font=("arial",20,"bold"),width=15,text="CCTV",bg="orange red",command=cctv).grid(row=0,column=1)

chat=Button(timepass,padx=20,pady=10,fg="brown",font=("arial",20,"bold"),width=15,text="Communication",bg="orange",command=chat).grid(row=1,column=1)

playgame=Button(timepass,padx=20,pady=10,fg="brown",font=("arial",20,"bold"),width=15,text="Voice Command",bg="orange red",command=voice_command).grid(row=2,column=1)

cafe_food=Button(cafe,padx=20,pady=10,fg="brown",font=("arial",20,"bold"),width=15,text="Cafe Food",bg="orange red",command = canteen).grid(row=0,column=0)


cafe_drink=Button(cafe,padx=20,pady=10,fg="brown",font=("arial",20,"bold"),width=15,text="Cafe Icecream",bg="orange red",command = cafe_).grid(row=4,column=0)





#____________________________Frame___________________________________________



title=Frame(root,width=1600,height=200,bg="#f18039",bd=50,relief=SUNKEN)
title.pack(side=TOP)

cafe=Frame(root,width=400,height=400, bg="#f18039",bd=50,relief=SUNKEN)
cafe.pack(side=LEFT)






title= Label(root,font=("arial",70,"bold"),text=("Icecream Cafe 24"),fg="#ff0000",bd=20,anchor="w")
title.grid(row=0,column=0)

root.mainloop()
