import os
import keyboard
import time
import mouse
import getpass
import psutil
import sys
import pygetwindow

os.system('cls')

#Gitting the user name

#Move the script to the startup folder

#open run
keyboard.press_and_release('win+r')
time.sleep(0.3)

#typing oculus.exe path
keyboard.write('"C:\Program Files\Oculus\Support\oculus-client\OculusClient.exe"')
time.sleep(0.1)

#opens it
keyboard.press_and_release('enter')
time.sleep(0.1)
mouse.move(0,0)
time.sleep(3)
win = pygetwindow.getWindowsWithTitle('Oculus')[0]
win.maximize()


#Checks if oculus is running
Check = "OculusClient.exe" in (p.name() for p in psutil.process_iter())

if Check == True:
    print("Oculus is running")
    mouse.move(74, 360)
    mouse.click(button='left')
    time.sleep(0.3)
else:
    print("Oculus is not running")
    sys.exit()


#Click on beta tab
mouse.move(753, 170)
mouse.click(button='left')
time.sleep(0.3)


#Click on AirLink
mouse.move(1123, 497)
mouse.click(button='left')
time.sleep(0.3)


#Close the window
mouse.move(1895, 20)
mouse.click(button='left')
mouse.move(960, 540)