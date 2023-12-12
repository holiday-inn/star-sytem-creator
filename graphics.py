import tkinter as tk 
from tkinter import *
from tkinter import ttk


window = tk.Tk()
window.geometry("640x480")
window.configure(background="#2a0134")
window.title("T-Town Veterinary Dental Clinic Database")

label1 = tk.Label(window,text="Star System Generator",background="#5a1876",font = 15)
label2 = tk.Button(window,text="Look",background="#5a1876",font = 15)
label3 = tk.Button(window,text="Generate",background="#5a1876",font = 15)


databox = tk.Label(window,background="#5a1876",width = 60,height = 22)
arrowprev = tk.Button(window,text="< Previous",relief=GROOVE,width=29,background="#5a1876")
arrownex = tk.Button(window,text="Next >",relief=GROOVE,width=29,background="#5a1876")

label1.place(x=210,y=30)
label2.place(x=20,y=100)
label3.place(x=80,y=100)
databox.place(x =180,y = 90)
arrownex.place(x=393,y=424)
arrowprev.place(x=180,y=424)


data = ["Name","Size","Atmosphere","Hydration","Population","Government","Law","Technology","Starport","Naval Base exists","Scout exists","Gas giant exists","Planetoids exist"]


def click(e):
    button = []
    for i in data:
        button.append(tk.Button(window, text = f"{i}",background="#5a1876"))
        tal = data.index(i)
        if tal%2 == 0:
            button[data.index(i)].place(x=195,y=((data.index(i)+1)*15)+150,width = 100)
        else:
            button[data.index(i)].place(x=305,y=(data.index(i)*15)+150,width = 100)

label2.bind("<Button-1>",click)


window.mainloop()