# -------------------------------------------
# ------- Using PyAutoGUI ------
# --- To open vscode
# --- install clangd from extension
# --- install c++ testmate  from extension
# --- install c++ helper  from extension
# --- install cmake  from extension
# --- install cmake tools  from extension
# -------------------------------------------
import pyautogui
import time

pyautogui.hotkey("win")
time.sleep(1)
pyautogui.write("vis")
time.sleep(1)
pyautogui.hotkey("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "shift", "x")
time.sleep(1)

pyautogui.write("clangd")
time.sleep(3)
pyautogui.click(263, 217)
time.sleep(5)
pyautogui.doubleClick(284, 144)
pyautogui.press("backspace")
time.sleep(1)

pyautogui.write("c++ testmate")
time.sleep(3)
pyautogui.click(269, 221)
time.sleep(8)
pyautogui.doubleClick(225, 141)
pyautogui.press("backspace")
time.sleep(1)

pyautogui.write("helper")
time.sleep(3)
pyautogui.click(267, 220)
time.sleep(8)
pyautogui.tripleClick(280, 141)
pyautogui.press("backspace")
time.sleep(1)

pyautogui.write("cmake")
time.sleep(3)
pyautogui.click(267, 217)
time.sleep(15)
pyautogui.doubleClick(276, 142)
pyautogui.press("backspace")
time.sleep(1)

pyautogui.write("cmake tools")
time.sleep(3)
pyautogui.click(252, 220)
time.sleep(15)

print("DONE")
