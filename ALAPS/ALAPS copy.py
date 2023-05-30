import time
import subprocess
import tkinter
import customtkinter
import pyautogui

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("(☞ﾟヮﾟ)☞ AALAPS ☜(ﾟヮﾟ☜)")
app.geometry("390x200")

check_var_sek = customtkinter.StringVar(value="0")
check_var_barepass = customtkinter.StringVar(value="0")
check_var_Advanced = customtkinter.StringVar(value="0")

def theme(x):
    if x == "Dark":
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_color_theme("green")
    elif x == "Light":
        customtkinter.set_appearance_mode("light")
        customtkinter.set_color_theme("blue")
    elif x == "Kristoffer":
        customtkinter.set_appearance_mode("Kristoffer")
        customtkinter.set_color_theme("dark-blue")

def advanced_mode(x):
    if x == "1":
        label.place_forget()
        KnappFinn.configure("disabled")
        entry.configure(state="disabled")
        entry_pass.place(relx=0.4, rely=0.65, anchor=tkinter.CENTER)
        entry_bruker.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
        KnappSkriv.configure(
            command=lambda: SkrivPass(
                check_var_barepass.get(), check_var_sek.get(), entry_bruker.get(), entry_pass.get()
            )
        )
    elif x == "0":
        label.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
        KnappFinn.configure(state="normal")
        entry.configure(state="normal")
        entry_pass.place_forget()
        entry_bruker.place_forget()
        KnappSkriv.configure(
            command=lambda: SkrivPass(check_var_barepass.get(), check_var_sek.get(), ".\Administrator", LapsPass)
        )

def FinnPass(AssetTag):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    global LapsPass

    if result.returncode == 0:
        LapsPass = result.stdout.strip()
        label.configure(text=LapsPass)

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


entry_pass = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Passord",
    width=250,
    height=25,
    border_width=2,
    corner_radius=10,
    show="*",
)

entry_bruker = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Brukernavn",
    width=250,
    height=25,
    border_width=2,
    corner_radius=10,
)

entry = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Asset-Tag",
    width=250,
    height=25,
    border_width=2,
    corner_radius=10,
)

KnappSkriv = customtkinter.CTkButton(
    master=app,
    width=50,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Skriv",
    command=lambda: SkrivPass(
        check_var_barepass.get(), check_var_sek.get(), ".\Administrator", LapsPass
    ),
)

KnappFinn = customtkinter.CTkButton(
    master=app,
    width=50,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Søk!",
    command=lambda: FinnPass(entry.get()),
)

optionmenu_var = customtkinter.StringVar(value="Dark")
optionmenu = customtkinter.CTkOptionMenu(
    app,
    values=["Light", "Dark", "Kristoffer"],
    command=lambda: theme(optionmenu_var.get()),
    variable=optionmenu_var,
)

checkbox_sek = customtkinter.CTkCheckBox(
    app, text="3 sek", variable=check_var_sek, onvalue="1", offvalue="0"
)

checkbox_barepass = customtkinter.CTkCheckBox(
    app, text="Bare Pass", variable=check_var_barepass, onvalue="1", offvalue="0"
)

checkbox_Advanced = customtkinter.CTkCheckBox(
    app,
    text="Advanced",
    command=lambda: advanced_mode(check_var_Advanced.get()),
    variable=check_var_Advanced,
    onvalue="1",
    offvalue="0",
)

label = customtkinter.CTkLabel(app, text="", font=("ariel", 24, "bold"))

checkbox_Advanced.place(relx=0.5965, rely=0.9, anchor=tkinter.CENTER)
entry.place(relx=0.4, rely=0.25, anchor=tkinter.CENTER)
label.place(relx=0.4, rely=0.5, anchor=tkinter.CENTER)
optionmenu.place(relx=0.2, rely=0.1, anchor=tkinter.CENTER)
checkbox_sek.place(relx=0.16, rely=0.9, anchor=tkinter.CENTER)
checkbox_barepass.place(relx=0.34, rely=0.9, anchor=tkinter.CENTER)
KnappSkriv.place(relx=0.85, rely=0.5, anchor=tkinter.CENTER)
KnappFinn.place(relx=0.85, rely=0.25, anchor=tkinter.CENTER)

app.mainloop()