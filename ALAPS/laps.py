import subprocess
import tkinter
import pyautogui

# Define the tkinter window
app = tkinter.Tk()
app.geometry("390x200")

# Function to find the LAPS password and display it in a label
def FinnPass(AssetTag, label):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    global LapsPass

    if result.returncode == 0:
        LapsPass = result.stdout.strip()
        label.config(text=LapsPass)
    else:
        LapsPass = "Error, failed to retrieve password."

# Function to write the LAPS password to the screen
def SkrivPass():
    FinnPass(entry.get(), label) # Call FinnPass to retrieve the password
    pyautogui.keyDown("alt")
    pyautogui.press("tab")
    pyautogui.keyUp("alt")
    pyautogui.write('.\Administrator')
    pyautogui.press("tab")
    pyautogui.write(LapsPass)
    pyautogui.press("enter")

# Create the search button
KnappFinn = tkinter.Button(master=app,
                           width=8,
                           height=1,
                           text="SØK!",
                           command=lambda: FinnPass(entry.get(), label)
                           )
KnappFinn.place(relx=0.85, rely=0.1, anchor=tkinter.CENTER)

# Create the write button
KnappSkriv = tkinter.Button(master=app,
                            width=8,
                            height=1,
                            text="Skriv!",
                            command=SkrivPass
                            )
KnappSkriv.place(relx=0.85, rely=0.4, anchor=tkinter.CENTER)

# Create the Asset Tag entry box
entry = tkinter.Entry(master=app)
entry.place(relx=0.4, rely=0.1, anchor=tkinter.CENTER)

# Create the password label
label = tkinter.Label(app, text="", font=('comic sans', 24, 'bold'))
label.place(relx=0.4, rely=0.4, anchor=tkinter.CENTER)

# Start the tkinter event loop
app.mainloop()
