from tkinter import *

#window
window=Tk()
window.title("Snögubbe")
window.geometry("600x600")
window.resizable(False, False)

#main-canvas
main = Canvas(window, width=600, height=600, bg="lightblue")
main.pack(pady=20,padx=20)

#text
main.create_text(100,70, text="God Jul", font=("Times New Roman", 24), fill="red")

#snowman structure
#smallest
main.create_oval(220, 180, 380, 30, fill='white', outline="")
#middle
main.create_oval(200, 340, 400, 150, fill='white', outline="")
#biggest
main.create_oval(180, 300, 420, 550, fill='white', outline="")

#eyes and nose
main.create_oval(250,100,280,70, fill="black")
main.create_oval(320,100,350,70, fill="black")
main.create_oval(250,94,270,76, fill="white")
main.create_oval(320,94,340,76, fill="white")


#buttons
#upper
main.create_oval(280, 200, 320, 240, fill="black")
main.create_oval(280, 250, 320, 290, fill="black")

#lower
main.create_oval(280, 430, 320, 470, fill="black")
main.create_oval(280, 380, 320, 420, fill="black")
main.create_oval(280, 330, 320, 370, fill="black")

#right arm and fingers
main.create_line(400,250,500,300, width=5)
main.create_line(500,300,540,290, width=5)
main.create_line(500,300,540,310, width=5)
main.create_line(500,300,540,330, width=5)

#left arm and fingers
main.create_line(200,250,100,300, width=5)
main.create_line(100,300,60,290, width=5)
main.create_line(100,300,60,310, width=5)
main.create_line(100,300,60,330, width=5)



#run
window.mainloop()