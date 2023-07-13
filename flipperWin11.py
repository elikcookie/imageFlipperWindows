import os
import time
import pyautogui
from PIL import Image

folder_path = r"C:\Users\eliko\OneDrive\Desktop\toflip"

image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    os.startfile(image_path)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'e')  # image editor shortcut
    time.sleep(2)
    
    # Flip image horizontally
    pyautogui.press('tab', presses=16)
    pyautogui.press('enter')
    time.sleep(2)
    
    # Save the flipped image
    pyautogui.press('tab', presses=8)
    pyautogui.press('down')
    pyautogui.press('tab',_pause = True)
    pyautogui.press('enter')
    time.sleep(2)
    
    pyautogui.hotkey('alt', 'f4')  # close image viewer


print("Image flipping completed.")
