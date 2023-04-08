import PIL
import os
from PIL import Image

f = r"D:/Annotated_Data/training_images_1"

os.listdir(f)

for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((224,224))
    print(f"Resizing {file}....")
    img.save(f_img)

print("Sakkyo")