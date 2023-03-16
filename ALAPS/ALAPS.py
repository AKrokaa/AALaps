import subprocess
import tkinter
import customtkinter



customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # Lager boks
app.geometry("390x240")







#lager søke etter Laps passord knapp
KnappS = customtkinter.CTkButton(master=app,
                                 width=50,
                                 height=32,
                                 border_width=0,
                                 corner_radius=8,
                                 text="SØK!",
                                 
                                 )
KnappS.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER) #plassere Søk knappen i boksen




#Lager Asset Tag input boks
entry = customtkinter.CTkEntry(master=app,
                               placeholder_text="Asset-Tag",
                               width=250,
                               height=25,
                               border_width=2,
                               corner_radius=10,)                               
entry.place(relx=0.4, rely=0.1, anchor=tkinter.CENTER) # plaserer Asset Tag boks








app.mainloop()


#Søker etter Laps passord og putter det i en variabel

def comp(AssetTag):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        return(result.stdout.strip())
    else:
        return("Error, failed to retrieve password.")

ComputerName = input("Input Asset-TAG:\n")
print(comp(ComputerName))