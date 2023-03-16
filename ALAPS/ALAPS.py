import subprocess

def comp(AssetTag):
    command = f"powershell -Command \"$password = (Get-AdmPwdPassword -ComputerName {AssetTag}).Password; Write-Output $password\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    if result.returncode == 0:
        return(result.stdout.strip())
    else:
        return("Error, failed to retrieve password.")

ComputerName = input("Input Asset-TAG:\n")
print(comp(ComputerName))