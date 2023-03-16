
#Tester GUI ting her

import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # Lager boks
app.geometry("390x240")

def button_event():
    print("button pressed")

button = customtkinter.CTkButton(master=root_tk, text="CTkButton", command=button_event)
button.pack(padx=20, pady=10)

app.mainloop()


#Søker etter Laps passord og putter det i en variabel