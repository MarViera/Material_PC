import subprocess

comando = "Get-Process"
lineaPS = "powershell -Executionpolicy ByPass"\
          +"-Command "+ comando
runningProcesses = subprocess.check_output(lineaPS)
print(runningProcesses.decode())

