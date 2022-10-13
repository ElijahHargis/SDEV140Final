from tkinter import *
# Create main window
window = Tk()
window.geometry("700x500")
#Calculating the Total
def calculate():
    # Gets how many entered
    Crankbait=e1.get()
    Spinnerbait=e2.get()
    Senko=e3.get()
    Whopper_Plopper=e4.get()
    Jig=e5.get()
    # Calculates the Total Amount
    total=((int(Crankbait)*7.5)+(int(Spinnerbait)*1.99)+(int(Senko)*5.83)+(int(Whopper_Plopper)*12.99)+(int(Jig)*0.99))
    # Presents the total
    label14=Label(window,text="The total is: $",font="times 18")
    label14.place(x=200,y=300)
    label15=Label(window,text=total,font="times 18")
    label15.place(x=350,y=300)
    label16=Label(window,text="Thank you for your purchase!", font="times 12")
    label16.place(x=275,y=340)
    # Label and button to send user to the survey window
    label17 = Label(window, text="Please make sure to take our survey!", font="times 12")
    label17.place(x=275, y=360)
    b3 = Button(window, text="Survey", width=10, command=window3)
    b3.place(x=520, y=350)
# Called Window 2 for simplicity, Simply closes the program
def window2():
    exit()
# Window for survey
def window3():
    window= Tk()
    window.geometry ("500x350")

    label18 = Label(window, text="How did you find us?", font="times 18")
    label18.place(x=20, y=20)
    e6=Entry(window)
    e6.place(x=20,y=50)

    label19 = Label(window, text="Would you shop with us again?", font="times 18")
    label19.place(x=20, y=80)
    e7=Entry(window)
    e7.place(x=20, y=110)

    label20 = Label(window, text="Would you recommend us to others?", font="times 18")
    label20.place(x=20, y=140)
    e8=Entry(window)
    e8.place(x=20, y=170)

    label21 = Label(window, text="Would you recommend us to others?", font="times 18")
    label21.place(x=20, y=200)
    e9=Entry(window)
    e9.place(x=20,y=230)

    b3 = Button(window, text="Send", width=20, command=window4)
    b3.place(x=100, y=270)

    window.mainloop()
# Window with thank you message, contact info, and button to close
def window4():
    window = Tk()
    window.geometry("300x180")
    label22 = Label(window, text="Thank you for shopping with us!", font="times 15")
    label22.place(x=10, y=20)
    label23 = Label(window, text="Please contact us at 1-888-888-888", font="times 15")
    label23.place(x=10, y=60)
    label24 = Label(window, text="for any other questions or concerns.", font="times 15")
    label24.place(x=10, y=85)
    b4=Button(window, text="Have a good day!",font="times 15", width=20, command=window2)
    b4.place(x=20,y= 120)
    window.mainloop()

# Header
label7=Label(window,text="Hargis Baits",font="times 30 bold")
label7.place(x=350,y=20, anchor="center")

# Items Section
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

# Billing Section
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
e5 =Entry(window)
e5.place(x=20,y=320)

# Button for ordering
b1=Button(window,text="Order",width=20,command=calculate)
b1.place(x=100,y=400)

# Button for closing
b2=Button(window,text="Close",width=20, command=window2)
b2.place(x=400,y=400)

window.mainloop()
