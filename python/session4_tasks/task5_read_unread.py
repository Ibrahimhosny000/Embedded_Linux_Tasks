# -----------------------------------------------------------------------------
# ---------                                                          --------
# Using “Pyautogui” to open Emails and change Emails from unread to read:-
# ---------                                                          --------
# -----------------------------------------------------------------------------

import pyautogui
import time

# while True:
#     x, y = pyautogui.position()
#     print(x, y)

pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("firefox")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(5)
pyautogui.hotkey("ctrl", "t")
time.sleep(2)
pyautogui.write("gmail.com")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(7)
pyautogui.click(834, 139)
time.sleep(1)
pyautogui.write("label:unread")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(1)
pyautogui.click(380, 256)
time.sleep(1)
pyautogui.hotkey("down")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(5)
pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("vis")
time.sleep(1)
pyautogui.hotkey("enter")
print("marked your mail from unread yo read")
