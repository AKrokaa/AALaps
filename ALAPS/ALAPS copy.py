import time
import subprocess
import tkinter
import customtkinter
import pyautogui

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
customtkinter.load_color_theme_from_file(".\dark-blue.json")



app = customtkinter.CTk()
app.title("(☞ﾟヮﾟ)☞ AALAPS ☜(ﾟヮﾟ☜)")
app.geometry("390x200")





def theme(x):
    if x == "Dark":
        customtkinter.set_appearance_mode("dark")
    elif x == "Light":
        customtkinter.set_appearance_mode("light")
    elif x == "Kristoffer":
        customtkinter.set_appearance_mode("Kristoffer")



optionmenu_var = customtkinter.StringVar(value="Dark")
optionmenu = customtkinter.CTkOptionMenu(app, values=["Dark", "Light","Kristoffer"],
                                         command=theme,
                                         variable=optionmenu_var

                                         )
optionmenu.set("Dark")



optionmenu.place(relx=0.2, rely=0.1, anchor=tkinter.CENTER)



app.mainloop()