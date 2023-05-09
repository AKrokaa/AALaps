"""





"""

import time
import subprocess
import tkinter
import customtkinter
import pyautogui

customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # Lager boks
app.title("(☞ﾟヮﾟ)☞ AALAPS ☜(ﾟヮﾟ☜)")
app.geometry("390x200")

label = customtkinter.CTkLabel(app, text="",font=('comic sans', 24,'bold'))
label.place(relx=0.4, rely=0.7, anchor=tkinter.CENTER)

def theme(x):
    if x == 1:
        customtkinter.set_appearance_mode("dark")
    elif x == 0:
        customtkinter.set_appearance_mode("light")

#denne skal finne laps passordet og putte det inn i en variabel (LapsPass)
def FinnPass(AssetTag):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    global LapsPass

    if result.returncode == 0:
        LapsPass = result.stdout.strip()
        label.configure(text=LapsPass)
    else:
        label.configure(text="Error, failed to retrieve password.")


#Skriver passordet i variablen LapsPass
def SkrivPass(x, y):
    
    if y == 1:
        time.sleep(3)
    else:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")

    if x == 1:
        pyautogui.write('.\Administrator')
        pyautogui.press("tab")
        pyautogui.write(LapsPass)
        pyautogui.press("enter")
    elif x == 0:
        pyautogui.write(LapsPass)
        pyautogui.press("enter")

#Denne knappen er for å skrive 
KnappSkriv = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Skriv",
                                 command=SkrivPass
                                 )
KnappSkriv.place(relx=0.85, rely=0.7, anchor=tkinter.CENTER)

#Lager Asset Tag input boks
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Asset-Tag",
                               width=250,
                               height=25,
                               border_width=2,
                               corner_radius=10,
                               )                               
entry.place(relx=0.4, rely=0.25, anchor=tkinter.CENTER) # plaserer Asset Tag boks

#lager søke etter Laps passord knapp
KnappFinn = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Søk!",
                                 command=lambda: FinnPass(entry.get())
                                 )
KnappFinn.place(relx=0.85, rely=0.25, anchor=tkinter.CENTER) #plassere Søk knappen i boksen

def checkbox_event():
    print("checkbox toggled, current value:", check_var_sek.get())

check_var_sek = customtkinter.StringVar(value="off")
checkbox_sek = customtkinter.CTkCheckBox(app, text="3 sek", command=checkbox_event,
                                     variable=check_var_sek, onvalue="on", offvalue="off")
checkbox_sek.place(relx=0.16, rely=0.9, anchor=tkinter.CENTER)


def checkbox_event():
    print("checkbox toggled, current value:", check_var_barepass.get())

check_var_barepass = customtkinter.StringVar(value="off")
checkbox_barepass = customtkinter.CTkCheckBox(app, text="Bare Pass", command=checkbox_event,
                                     variable=check_var_barepass, onvalue="on", offvalue="off")
checkbox_barepass.place(relx=0.34, rely=0.9, anchor=tkinter.CENTER)


#dette er slik att boksen looper
app.mainloop()