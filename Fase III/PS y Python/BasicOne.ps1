# Python Executable Definition
$Python = "python.exe"

# Python Scrip that I wish to execute
$Script = "C:\Users\marle\OneDrive\Documentos\GitHub\Material_PC\Fase III\PS y Python\BasicOne.py"

Write-Host "Pass a String to Python"
#$Message = "Hello Python - Hello Universe"
$Message = @("Hello Python", "Hello Universe", 
"Bye Python", "Bye Universe")

$Message | & $Python $Script