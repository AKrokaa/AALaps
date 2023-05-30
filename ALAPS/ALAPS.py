import time
import subprocess
import tkinter
import customtkinter
import pyautogui

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # lager main boks
app.title("(☞ﾟヮﾟ)☞ AALAPS ☜(ﾟヮﾟ☜)") # tittelen på toppen
app.geometry("390x200") # størrelsen på boksen

# status på bokser, startverdi velges her.
check_var_sek = customtkinter.StringVar(value="0")
check_var_barepass = customtkinter.StringVar(value="0")
check_var_Advanced = customtkinter.StringVar(value="0")

# function for å endre tema
def theme(x):
    if x == "Dark":
        customtkinter.set_appearance_mode("dark")
    elif x == "Light":
        customtkinter.set_appearance_mode("light")
    elif x == "Kristoffer":
        customtkinter.set_appearance_mode("Kristoffer")


# advanced_mode gir mulighet for å legge inn eget brukernavn og passord
def advanced_mode(x):
    if x == "1":
        label.place_forget()
        KnappFinn.configure("disabled")
        entry.configure(state="disabled")                        
        entry_pass.place(relx=0.4, rely=0.65, anchor=tkinter.CENTER)                              
        entry_bruker.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
        KnappSkriv.configure(command=lambda: SkrivPass(check_var_barepass.get(), check_var_sek.get(), entry_bruker.get(), entry_pass.get()))

    elif x == "0":
        label.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER) 
        KnappFinn.configure(state="normal")
        entry.configure(state="normal")
        entry_pass.place_forget()
        entry_bruker.place_forget()
        KnappSkriv.configure(command=lambda: SkrivPass(check_var_barepass.get(), check_var_sek.get(), '.\Administrator', LapsPass))

# sender inn assettag igjennom en powershell kommando og stripper den ned helt til det er kun LAPS-passord, og setter verdien i variabelen "LapsPass"
def FinnPass(AssetTag):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    global LapsPass

    if result.returncode == 0:
        LapsPass = result.stdout.strip()
        label.configure(text=LapsPass)

# skriver passordet i variablen LapsPass, utifra om "3 sek" og "Bare Pass" er huket av.
def SkrivPass(x, y, name, password):
    if y == "1":
        time.sleep(3)
    else:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        pyautogui.keyUp("alt")

    if x == "0":
        time.sleep(0.5)
        pyautogui.write(str(name))
        pyautogui.press("tab")
        pyautogui.write(str(password))
        pyautogui.press("enter")
    elif x == "1":
        time.sleep(0.5)
        pyautogui.write(str(password))
        pyautogui.press("enter")

# advanced_mode: selv-input felt av eget passord
entry_pass = customtkinter.CTkEntry(master=app,
                                    placeholder_text="Passord",
                                    width=250,
                                    height=25,
                                    border_width=2,
                                    corner_radius=10,
                                    show="*"
                                    )
 
# advanced_mode: selv-input felt av eget brukernavn
entry_bruker = customtkinter.CTkEntry(master=app,
                                      placeholder_text="Brukernavn",
                                      width=250,
                                      height=25,
                                      border_width=2,
                                      corner_radius=10,
                                      )       

# input-felt for Asset-Tag
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Asset-Tag",
                               width=250,
                               height=25,
                               border_width=2,
                               corner_radius=10,
                               )

# knapp for å kalle på "SkrivPass"
KnappSkriv = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Skriv",
                                 command=lambda: SkrivPass(check_var_barepass.get(), check_var_sek.get(), ".\Administrator", LapsPass)
                                )

# knapp for FinnPass funksjonen
KnappFinn = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Søk!",
                                 command=lambda: FinnPass(entry.get())
                                 )

# bryter for light-mode og dark-mode (dark-mode standard)                                      )


optionmenu_var = customtkinter.StringVar(value="Dark")
optionmenu = customtkinter.CTkOptionMenu(app,values=["Light", "Dark","Kristoffer"],
                                         command=lambda: theme(optionmenu_var),
                                         variable=optionmenu_var)


# checkbox for om SkrivPass skal vente 3sek før den kjører
checkbox_sek = customtkinter.CTkCheckBox(app, 
                                         text="3 sek",
                                         variable=check_var_sek, 
                                         onvalue="1", offvalue="0"
                                         )

# checkbox for om SkrivPass skal ikke printe ut ./Administrator eller selv-input brukernavn
checkbox_barepass = customtkinter.CTkCheckBox(app, 
                                              text="Bare Pass",
                                              variable=check_var_barepass, 
                                              onvalue="1", offvalue="0"
                                              )

# checkbox for å huke av om advanced_mode funksjonen skal gjennomføres. (selv-input av brukernavn og passord)
checkbox_Advanced = customtkinter.CTkCheckBox(app, 
                                              text="Advanced", 
                                              command=lambda: advanced_mode(check_var_Advanced.get()),
                                              variable=check_var_Advanced, 
                                              onvalue="1", offvalue="0"
                                              )
                           
# viser LAPS passordet.
label = customtkinter.CTkLabel(app, 
                               text="",
                               font=('ariel', 24,'bold')
                               )

# plassering av alle felt, brytere og knapper.
checkbox_Advanced.place(relx=0.5965, rely=0.9, anchor=tkinter.CENTER)
entry.place(relx=0.4, rely=0.25, anchor=tkinter.CENTER) # plaserer Asset Tag boks
label.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
optionmenu.place(relx=0.2, rely=0.1, anchor=tkinter.CENTER)
checkbox_sek.place(relx=0.16, rely=0.9, anchor=tkinter.CENTER)
checkbox_barepass.place(relx=0.34, rely=0.9, anchor=tkinter.CENTER) #Denne knappen er for å skrive 
KnappSkriv.place(relx=0.85, rely=0.5, anchor=tkinter.CENTER) #Lager Asset Tag input boks
KnappFinn.place(relx=0.85, rely=0.25, anchor=tkinter.CENTER) #plassere Søk knappen i boksen

# dette er slik att boksen looper

#Test

app.mainloop() 