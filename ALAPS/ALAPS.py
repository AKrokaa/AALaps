import subprocess
import tkinter
import customtkinter
import pyautogui

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # Lager boks
app.title("(☞ﾟヮﾟ)☞ AALAPS ☜(ﾟヮﾟ☜)")
app.geometry("390x200")

label = customtkinter.CTkLabel(app, text="",font=('comic sans', 24,'bold'))
label.place(relx=0.4, rely=0.7, anchor=tkinter.CENTER)

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
def SkrivPass():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.write('.\Administrator')
    pyautogui.press("tab")
    pyautogui.write(LapsPass)
    pyautogui.press("enter")



#Denne knappen er for å skrive 
KnappSkriv = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Print",
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



app.mainloop()