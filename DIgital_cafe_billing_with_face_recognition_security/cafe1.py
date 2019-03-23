from tkinter import*
import time
import random
#-------------------------simple e basic button-----------------------------

def cafe():




        window2=Tk()
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
 
