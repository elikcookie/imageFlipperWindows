import os
import time
import pyautogui
from PIL import Image

folder_path = r"C:\Users\eliko\OneDrive\Desktop\toflip"
flipped_folder_path = r"C:\Users\eliko\OneDrive\Desktop\flipped"

image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)
    os.startfile(image_path)
    time.sleep(5)
    
    # pyautogui.hotkey('ctrl', 'e')
    # time.sleep(5)  
    
    hori = pyautogui.locateCenterOnScreen("hori_flip.png")
    pyautogui.click(hori)

    save_copy = pyautogui.locateCenterOnScreen("save_copy.png")
    pyautogui.click(save_copy)
    time.sleep(5)   

    pyautogui.typewrite(flipped_folder_path)
    pyautogui.press('enter')
    time.sleep(3)  # Increased delay
    
    pyautogui.hotkey('alt', 'f4')
    pyautogui.press('enter')
    time.sleep(3)  # Increased delay

print("Image flipping completed.")
