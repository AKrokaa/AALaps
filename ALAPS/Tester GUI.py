
#Tester GUI ting her

import tkinter
import customtkinter
from tkinter import *
import pyautogui

#Boxen
root = Tk()
root.title("Adrian_Laps")
root.geometry("300x200")
root.config(bg="gray")

Rute1 = LabelFrame(root, text="LAPS PASSORD 1", padx=35,pady=10, bg="gray", fg="blue")
Rute1.place(x=10,y=10)


Rute2 = LabelFrame(root, text="LAPS PASSORD 2", padx=35,pady=10, bg="gray", fg="blue")
Rute2.place(x=10,y=100)

#input1
e1 = Entry(Rute1)
e1.grid(row=0,column=0)
#skriv 1
def myClick():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.write('.\Administrator')
    pyautogui.press("tab")
    pyautogui.write(e1.get())
    pyautogui.press("enter")
myButton1 = Button(Rute1, text="Skriv1", command=myClick, fg="green", padx=20)
myButton1.grid(row=0,column=2)

#input2
e2 = Entry(Rute2)
e2.grid(row=0, column=0)
#skriv 2
def myClick():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.write('.\Administrator')
    pyautogui.press("tab")
    pyautogui.write(e2.get())
    pyautogui.press("enter")
myButton2 = Button(Rute2, text="Skriv2", command=myClick, fg="green", padx=20)
myButton2.grid(row=0, column=1)








root.mainloop()


#Søker etter Laps passord og putter det i en variabel