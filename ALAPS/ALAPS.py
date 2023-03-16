import subprocess

def comp(x):
    computer_name = x # Replace with the actual computer name
    command = "powershell Get-AdmPwdPassword -ComputerName " + computer_name 

    output = subprocess.check_output(command, shell=True)
    print(output.decode('utf-8'))

AT = input("Input Asset-TAG:\n")
comp(AT)