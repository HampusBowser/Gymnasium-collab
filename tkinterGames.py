from tkinter import*
from tkinter  import messagebox

#Själva windown till programmet
window = Tk()
window.geometry("1000x600")
window.title("(づ￣ 3￣)づ")
window.configure(bg="#abbd9a")

#gameslistan till uppgiftenn
gamelist = ["Call of Duty", "Skyrim", "Overwatch", "GTA", "Castlevania", "Resident Evil", "HALO", "Battlefield", "Gears of War", "FallOut"]

def searchgame():
    if str(searchbar.get()) in gamelist:
        finns.configure(text="Den finns i listan", bg="green", fg="white")
    else:
        finns.configure(text="Nej den finns inte i listan,"
                             "Vill du lägga till den?", bg="red", fg="white")
        ja = Button(window, text="Lägg till", height=3, width=10, activebackground="#8fc98f", command = ja_val)
        ja.place(y=150, x=420)
        nej = Button(window, text="Nej", height=3, width=10, activebackground="#8fc98f", command= nej_val)
        nej.place(y=150, x=520)
def ja_val():
    gamelist.append(str(searchbar.get()))
    disabled()
def nej_val():
    disabled()
def skrivUt():
    messagebox.showinfo("Listan", " , ".join(gamelist))

def amountgames():
    numberofgames = len(gamelist)
    messagebox.showinfo("Spel", str(numberofgames))

def alphabeticalOrder():
    gamelist.sort()
    messagebox.showinfo("Alfabetisk ordning", " , ".join(gamelist))





#searchbaren
searchbar = Entry(window)
searchbar.place(y = 70, x = 440)

#PRINTLIST
printList = Button(window, text="Printa listan", height=10, width=20, activebackground="#8fc98f", command=skrivUt)
printList.place(y = 400, x = 100)

#COUNTLIST
countList = Button(window, text="Antal spel", height=10, width=20, activebackground="#8fc98f", command=amountgames)
countList.place(y = 400, x = 435)
#ALPHABECTICALORDER
order = Button(window, text="Ordna listan", height=10, width=20, activebackground="#8fc98f", command = alphabeticalOrder)
order.place(y = 400, x = 770)

#Sök knappen för att kunna klicka "sök"
search = Button(window, text="Sök", height=3, width=10, activebackground="#8fc98f", command=searchgame)
search.place(y=48, x=585)


finns = Label(window, bg="#abbd9a")
finns.place(y=120, x=400)


def disabled():
    ja_button = Button(window, text="Lägg till", height=3, width=10, activebackground="#8fc98f", state=DISABLED)
    nej_button = Button(window, text="Nej", height=3, width=10, activebackground="#8fc98f", state = DISABLED)
    ja_button.place(y=150, x=420)
    nej_button.place(y=150, x=520)

ja_button = Button(window, text="Lägg till", height=3, width=10, activebackground="#8fc98f", state=DISABLED)
nej_button = Button(window, text="Nej", height=3, width=10, activebackground="#8fc98f", state = DISABLED)
ja_button.place(y=150, x=420)
nej_button.place(y=150, x=520)



mainloop()