Set-Location $PSScriptRoot
# Python Executable Definition
$Python = "python.exe"


# Python Scrip that I wish to execute
$Script = Join-Path $PSScriptRoot "pyExif.py"
$Carpeta = Join-Path $PSScriptRoot "imagenes"


$files = Get-ChildItem -Path $Carpeta -Filter *.jpg
$jpegList = $files.FullName | Format-Table -HideTableHeaders
#Write-Host $jpegList
$jpegList | & $Python $Script
