
# Python Executable Definition
$Python = "python.exe"


# Python Scrip that I wish to execute
$Script = "pyExif.py"


$files = Get-ChildItem "C:\Users\Mar\Downloads\images\*.jpg" 
$jpegList = $files | Select-Object FullName | Format-Table -HideTableHeaders
#Write-Host $jpegList
$jpegList | & $Python $Script
