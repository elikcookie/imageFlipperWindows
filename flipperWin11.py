import os
from PIL import Image, ImageOps

folder_path = r"C:\Users\eliko\OneDrive\Desktop\toflip"
flipped_folder_path = r"C:\Users\eliko\OneDrive\Desktop\flipped"

image_files = [file for file in os.listdir(folder_path) if file.lower().endswith(('.png', '.jpg', '.jpeg'))]

for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    image = Image.open(image_path)

    image_flip = ImageOps.mirror(image)
    image_flip.save(flipped_folder_path + "\\" + image_file, quality=95)


print("Image flipping completed.")
