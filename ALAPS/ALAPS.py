import subprocess
import tkinter
import customtkinter
import pyautogui




customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # Lager boks
app.geometry("390x200")

LapsPass = "Dette er ett passord"


#denne skal finne laps passordet og putte det inn i en variabel (LapsPass)
def FinnPass():
    print(entry.get())


#Skriver passordet i variablen LapsPass
def SkrivPass():
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.write('.\Administrator')
    pyautogui.press("tab")
    pyautogui.write(LapsPass)
    pyautogui.press("enter")




#lager søke etter Laps passord knapp
KnappFinn = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="SØK!",
                                 command=FinnPass
                                 )
KnappFinn.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER) #plassere Søk knappen i boksen




#Denne knappen er for å skrive 
KnappSkriv = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Skriv!",
                                 command=SkrivPass
                                 )
KnappSkriv.place(relx=0.85, rely=0.4, anchor=tkinter.CENTER)






#Lager Asset Tag input boks
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Asset-Tag",
                               width=250,
                               height=25,
                               border_width=2,
                               corner_radius=10,
                               )                               
entry.place(relx=0.4, rely=0.1, anchor=tkinter.CENTER) # plaserer Asset Tag boks





#Label som viser lapspassordet
label = customtkinter.CTkLabel(app, text=LapsPass, fg_color="green",font=('comic sans', 24,'bold'))
label.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)





app.mainloop()


#Søker etter Laps passord og putter det i en variabel

#def comp(AssetTag):
 #   command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
  #  result = subprocess.run(command, shell=True, capture_output=True, text=True)
   # 
    #if result.returncode == 0:
    #    return(result.stdout.strip())
    #else:
     #   return("Error, failed to retrieve password.")

#ComputerName = input("Input Asset-TAG:\n")
#print(comp(ComputerName))