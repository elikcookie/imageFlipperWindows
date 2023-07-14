import os
import time
import pyautogui
from PIL import Image

folder_path = r"C:\Users\eliko\OneDrive\Desktop\toflip"
flipped_folder_path = r"C:\Users\eliko\OneDrive\Desktop\flipped"

image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

flipH = pyautogui.locateCenterOnScreen("flipH.png", confidence = 0.9, minSearchTime=5)
saveAsCopy = pyautogui.locateCenterOnScreen("saveAs.png",confidence= 0.9, minSearchTime=5)
savebtn = pyautogui.locateCenterOnScreen("savebtn.png",confidence=0.9, minSearchTime=5)

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
    time.sleep(1)
    
    # Save the flipped image
    pyautogui.click(saveAsCopy)
    time.sleep(1)
    pyautogui.press('tab', presses=6)
    pyautogui.press('enter')
    pyautogui.typewrite(flipped_folder_path)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.click(savebtn)
    time.sleep(1)

    pyautogui.hotkey('alt', 'f4')  # close image viewer
    flipped_image_path = os.path.join(flipped_folder_path, f"flipped_{image_file}")
    image.save(flipped_image_path)
    image.close()

print("Image flipping completed.")