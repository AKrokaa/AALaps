import time
import subprocess
import tkinter
import customtkinter
import pyautogui

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green



app = customtkinter.CTk()  # Lager boks
app.title("(☞ﾟヮﾟ)☞ AALAPS ☜(ﾟヮﾟ☜)")
app.geometry("390x200")

entry_pass = customtkinter.CTkEntry(master=app,
                        placeholder_text="Passord",
                        width=250,
                        height=25,
                        border_width=2,
                        corner_radius=10,
                        ) 
entry_bruker = customtkinter.CTkEntry(master=app,
                        placeholder_text="Brukernavn",
                        width=250,
                        height=25,
                        border_width=2,
                        corner_radius=10,
                        )       

KnappSkriv = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Skriv",
                                 command=lambda: SkrivPass(check_var_barepass.get(), check_var_sek.get(), Username, LapsPass)
                                 )

label = customtkinter.CTkLabel(app, text="",font=('ariel', 24,'bold'))
label.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)

def theme(x):
    if x == "1":
        customtkinter.set_appearance_mode("dark")
    elif x == "0":
        customtkinter.set_appearance_mode("light")

switch_var = customtkinter.StringVar(value="1")
switch = customtkinter.CTkSwitch(app, text="Light mode", command=lambda: theme(switch_var.get()),
                                 variable=switch_var, onvalue="0", offvalue="1")
switch.place(relx=0.15, rely=0.1, anchor=tkinter.CENTER)

#Dette er custom mode, hvor det blir laget, fjerner og disabler noen bokser
def advanced_mode(x):
    if x == "1":
        label.place_forget()
        KnappFinn.configure("disabled")
        label.configure(state="disabled")
        entry.configure(state="disabled")                        
        entry_pass.place(relx=0.4, rely=0.65, anchor=tkinter.CENTER)                              
        entry_bruker.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
        KnappSkriv.configure(command=lambda: SkrivPass(entry.get(), check_var_sek.get(), entry_bruker.get(), entry_pass.get()))

    elif x == "0":
        label.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER) 
        KnappFinn.configure(state="normal")
        label.configure(state="normal")
        entry.configure(state="normal")
        entry_pass.place_forget()
        entry_bruker.place_forget()

check_var_Advanced = customtkinter.StringVar(value="0")
checkbox_Advanced = customtkinter.CTkCheckBox(app, text="Advanced", command=lambda: advanced_mode(check_var_Advanced.get()),
                                     variable=check_var_Advanced, onvalue="1", offvalue="0")
checkbox_Advanced.place(relx=0.60, rely=0.9, anchor=tkinter.CENTER)

#denne skal finne laps passordet og putte det inn i en variabel (LapsPass)
def FinnPass(AssetTag):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    global LapsPass
    global Username

    if result.returncode == 0:
        LapsPass = result.stdout.strip()
        Username = '.\Administrator'
        label.configure(text=LapsPass)

#Skriver passordet i variablen LapsPass
def SkrivPass(x, y, name, password):
    
    u = str(name)
    p = str(password)

    if y == "1":
        time.sleep(3)
    else:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")

    if x == "0":
        time.sleep(0.5)
        pyautogui.write(u)
        pyautogui.press("tab")
        pyautogui.write(p)
        pyautogui.press("enter")
    elif x == "1":
        time.sleep(0.5)
        pyautogui.write(p)
        pyautogui.press("enter")

check_var_sek = customtkinter.StringVar(value="0")
checkbox_sek = customtkinter.CTkCheckBox(app, text="3 sek",
                                     variable=check_var_sek, onvalue="1", offvalue="0")
checkbox_sek.place(relx=0.16, rely=0.9, anchor=tkinter.CENTER)

check_var_barepass = customtkinter.StringVar(value="0")
checkbox_barepass = customtkinter.CTkCheckBox(app, text="Bare Pass",
                                     variable=check_var_barepass, onvalue="1", offvalue="0")
checkbox_barepass.place(relx=0.34, rely=0.9, anchor=tkinter.CENTER)

#Denne knappen er for å skrive 
KnappSkriv.place(relx=0.85, rely=0.5, anchor=tkinter.CENTER)

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

#dette er slik att boksen looper
app.mainloop()