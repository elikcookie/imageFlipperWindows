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
    pyautogui.hotkey('ctrl', 'e')
    time.sleep(2)
    pyautogui.click(x=200, y=200)
    time.sleep(2)
    pyautogui.click(x=300, y=300)
    time.sleep(2)
    pyautogui.hotkey('alt', 'f4')
    flipped_image_path = os.path.join(folder_path, f"flipped_{image_file}")
    image.save(flipped_image_path)
    image.close()

print("Image flipping completed.")
