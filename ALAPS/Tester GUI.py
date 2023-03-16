
#Tester GUI ting her

import tkinter
import customtkinter


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


app = customtkinter.CTk()  # Lager boks
app.geometry("390x240")


text_var = tkinter.StringVar(value="CTkLabel")

label = customtkinter.CTkLabel(master=app,
                               textvariable=text_var,
                               width=120,
                               height=25,
                               fg_color=("white", "gray75"),
                               corner_radius=8)
label.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)




app.mainloop()


#Søker etter Laps passord og putter det i en variabel