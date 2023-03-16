import subprocess

def comp(x):
    computer_name = x # Replace with the actual computer name
    command = "powershell Get-AdmPwdPassword -ComputerName " + computer_name + " | Select-Object ComputerName, Password, ExpirationTimestamp"

    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    print(output.decode('utf-8'))

AT = input("Input Asset-TAG:\n")
comp(AT)