from tkinter import*
window = Tk()
window.geometry("700x500")

#Calculating the Total
def calculate():
    Crankbait=e1.get()
    Spinnerbait=e2.get()
    Senko=e3.get()
    Whopper_Plopper=e4.get()
    Jig=e5.get()
    total=((int(Crankbait)*7.5)+(int(Spinnerbait)*1.99)+(int(Senko)*5.83)+(int(Whopper_Plopper)*12.99)+(int(Jig)*0.99))
    label14=Label(window,text="The total is: $",font="times 18")
    label14.place(x=300,y=400)
    label15=Label(window,text=total,font="times 18")
    label15.place(x=450,y=400)



label7=Label(window,text="Hargis Baits",font="times 30 bold")
label7.place(x=350,y=20, anchor="center")

#Items Section
label1=Label(window,text="Inventory",font="times 28 bold")
label1.place(x=500,y=60)

label2=Label(window,text="Crankbait                  $7.50",font="times 18")
label2.place(x=430,y=110)

label3=Label(window,text="Spinnerbait                $1.99",font="times 18")
label3.place(x=430,y=150)

label4=Label(window,text="Senko                         $5.83",font="times 18")
label4.place(x=430,y=190)

label5=Label(window,text="Whopper Plopper    $12.99",font="times 18")
label5.place(x=430,y=220)

label6=Label(window,text="Jig                              $0.99",font="times 18")
label6.place(x=430,y=250)

#Billing Section

label8=Label(window,text="Select the items you want to order", font="times 20 bold")
label8.place(x=10,y=70)

label9=Label(window,text="Crankbait", font="times 18")
label9.place(x=20,y=120)
e1=Entry(window)
e1.place(x=20,y=150)

label10=Label(window,text="Spinnerbait", font="times 18")
label10.place(x=200,y=120)
e2=Entry(window)
e2.place(x=200,y=150)

label11=Label(window,text="Senko", font="times 18")
label11.place(x=20,y=200)
e3=Entry(window)
e3.place(x=20,y=230)

label12=Label(window,text="Whopper Plopper", font="times 18")
label12.place(x=200,y=200)
e4=Entry(window)
e4.place(x=200,y=230)

label13=Label(window,text="Jig", font="times 18")
label13.place(x=20,y=290)
e5=Entry(window)
e5.place(x=20,y=320)

b1=Button(window,text="Order",width=20,command=calculate)
b1.place(x=100,y=400)

window.mainloop()