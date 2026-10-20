import pyautogui, subprocess, time
msg = input("Qué quieres escribir? ")
subprocess.call(["cmd", "/c", "start", "/max",
                 'C:\\Windows\\System32\\notepad.exe'])
time.sleep(2)
pyautogui.click(100,100)
pyautogui.typewrite(msg)
time.sleep(3)
pyautogui.press('enter') 
pyautogui.press('tab')
pyautogui.typewrite('Bye!')
pyautogui.keyDown('ctrl') 
pyautogui.keyDown('s')#g
pyautogui.keyUp('s')#g
pyautogui.keyUp('ctrl')
time.sleep(2)
pyautogui.typewrite('PC2_61EJ25.txt')
pyautogui.press('enter')
#Las siguientes líneas son necesarias si queremos
#sobrescribir un archivo existente
pyautogui.press('tab')
pyautogui.press('enter')
#Mensaje
#   Bye!











