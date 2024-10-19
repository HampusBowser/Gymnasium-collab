#importerar, skapar och konfiguerar själva window:et
from tkinter import*
window = Tk()
window.geometry("320x500")
window.title("Miniräknare")
window.configure(bg="#9ED2C6")
window.resizable(0, 0)

#Uppdaterar writingbox 
expression = "" 
def click(number): 
    global expression
    expression = expression + str(number) 
    input_text.set(expression)

#Ändrar variablerna i en widget till string
input_text = StringVar()

#Det som skrivs ut i string, själva rutan
writingbox = Entry(window, font=('Comic Sans MS', 20, 'bold'), textvariable=input_text, state=DISABLED, width=15, )
writingbox.grid(row=0, column=0, columnspan=200, padx=10, pady=10)

#Kollar errors, om inga finns så räknar och skrivs resultatet ut i writingbox. Om errors finns skriver ut att det inte går.
def equal():
    try: 
        global expression

        total = str(eval(expression))

        input_text.set(total)
        expression = ""

    except: 

        input_text.set(" error ")
        expression = ""

#Tömmer writingbox, sätter string-variabeln till inget
def clear():
    global expression
    expression = ""
    input_text.set("")

#Avslutar programmet
def exiting():
    window.quit()

#rad 1 - knappar
clear = Button(window, text="C", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=clear)
clear.grid(row=1, column=0)
exit = Button(window, text="Exit",height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=exiting).grid(row=1, column=1)
modulus = Button(window, text= "%", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=lambda: click("%")).grid(row=1, column=2)
division = Button(window, text= "/", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=lambda: click("/")).grid(row=1, column=3)

#rad 2 - knappar
multiplication = Button(window, text="*", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=lambda: click("*")).grid(row=2,column=3)
number9 = Button(window,text="9", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(9)).grid(row=2,column=2)
number8 = Button(window,text="8", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(8)).grid(row=2,column=1)
number7 = Button(window,text="7", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(7)).grid(row=2,column=0)

#rad 3 - knappar
minus = Button(window, text="-", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=lambda: click("-")).grid(row=3,column=3)
number6 = Button(window,text="6", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(6)).grid(row=3,column=2)
number5 = Button(window,text="5", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(5)).grid(row=3,column=1)
number4 = Button(window,text="4", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(4)).grid(row=3,column=0)

#rad 4 - knappar
plus = Button(window, text="+", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", command=lambda: click("+")).grid(row=4,column=3)
number3 = Button(window,text="3", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(3)).grid(row=4,column=2)
number2 = Button(window,text="2", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(2)).grid(row=4,column=1)
number1 = Button(window,text="1", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(1)).grid(row=4,column=0)

#rad 5 - knappar
number0= Button(window,text="9", height=5, width=10, activebackground="#54BAB9", bg="#F7ECDE", cursor = "heart", command = lambda: click(0)).grid(row=5,column=0)
enter = Button(window,text="Enter", height=5, width=22, activebackground="#54BAB9", bg="#F7ECDE", command=equal).grid(row=5,column=1, columnspan=3)


window.mainloop()
 