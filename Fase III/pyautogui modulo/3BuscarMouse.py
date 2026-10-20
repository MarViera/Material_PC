import pyautogui

input()
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: '+str(x).rjust(4)+' Y: '+\
                      str(y).rjust(4)
        print(positionStr, end='')
        print ("\n")
except KeyboardInterrupt:
    print('\n')
    pyautogui.click(x=x, y =y, clicks = 1)

