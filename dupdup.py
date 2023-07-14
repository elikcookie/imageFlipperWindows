import pyautogui
import time

hori = pyautogui.locateCenterOnScreen("hori_flip.png")
pyautogui.click(hori)
time.sleep(3)
save_copy = pyautogui.locateCenterOnScreen("save_copy.png")
pyautogui.click(save_copy)