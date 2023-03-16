import subprocess
import tkinter as tk
from tkinter import messagebox
import os

# Function to check if the program is run as administrator
def is_admin():
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

# Function to retrieve the LAPS password for a computer
def retrieve_laps_password():
    # Get the computer name from the GUI entry
    computer_name = computer_entry.get()

    # Check if the program is run as administrator
    if not is_admin():
        messagebox.showerror("Error", "This program must be run as administrator.")
        return

    # Run the PowerShell command to retrieve the LAPS password
    command = "powershell Get-AdmPwdPassword -ComputerName " + computer_name
    try:
        output = subprocess.check_output(command, shell=True)
        password = output.decode('utf-8').split("\n")[1].split(":")[1].strip()
        # Write out the password to the GUI text widget
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, ".\Administrator\t")
        output_text.insert(tk.END, password)
    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "Could not retrieve LAPS password for " + computer_name)

# Create the GUI window
root = tk.Tk()
root.title("Retrieve LAPS Password")

# Add a label and entry for the computer name
computer_label = tk.Label(root, text="Computer Name:")
computer_label.grid(row=0, column=0, padx=5, pady=5)
computer_entry = tk.Entry(root)
computer_entry.grid(row=0, column=1, padx=5, pady=5)

# Add a button to retrieve the LAPS password
retrieve_button = tk.Button(root, text="Retrieve Password", command=retrieve_laps_password)
retrieve_button.grid(row=0, column=2, padx=5, pady=5)

# Add a text widget to display the output
output_text = tk.Text(root, width=30, height=1)
output_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Start the GUI main loop
root.mainloop()