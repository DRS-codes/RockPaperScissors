import tkinter as tk
from tkinter import PhotoImage
import random

root = tk.Tk()
root.title("Rock Paper Scissors")
root.configure(background="white")
def mymove(move):
    if(move == 1):
        label.config(text="Your move : Rock")
    elif(move == 2):
        label.config(text="Your move : Paper")
    else:
        label.config(text="Your move : Scissors")
    comp = random.choice(range(1,4))
    if(comp == 1):
        label1.config(text="Computer's move : Rock")
    elif(comp == 2):
        label1.config(text="Computer's move : Paper")
    elif(comp == 3):
        label1.config(text="Computer's move : Scissors")
    if(move == comp):
        label2.config(text="Draw")
    else:
        if(comp == 1 and move == 2 or comp == 2 and move == 3 or comp == 3 and move == 1):
            label2.config(text="You win")
        else:
            label2.config(text="Computer wins")
    

label  = tk.Label(root, text="Your move : ", font=20, background="white")
label.grid(row=0, column=1, padx=0, pady=10)

label1  = tk.Label(root, text="Computer's move : ", font=20, background="white")
label1.grid(row=1, column=1, padx=0, pady=5)

image = PhotoImage(file="rock.png")
button = tk.Button(root, image=image, command=lambda: mymove(1), width=150, height=150, font=20)
button.grid(row=2, column=0, padx=40, pady=40)

image2 = PhotoImage(file="paper.png")
button1 = tk.Button(root, image=image2, command=lambda: mymove(2), width=150, height=150, font=20)
button1.grid(row=2, column=1, padx=40, pady=40)

image3 = PhotoImage(file="scissors.png")
button2 = tk.Button(root, image=image3, command=lambda: mymove(3), width=150, height=150, font=20)
button2.grid(row=2, column=2, padx=40, pady=40)

label2  = tk.Label(root, text="Winner ", font=20, background="white")
label2.grid(row=3, column=1, pady=10)


root.mainloop()