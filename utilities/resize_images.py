import os
from PIL import Image

# Script to resize all images to 224x224 pixels

f = r"D:/Annotated_Data/training_images_1" # Path to directory

os.listdir(f)

# Loop through all files in the directory
for file in os.listdir(f):
    f_img = f+"/"+file # Store image data i variable
    img = Image.open(f_img)
    img = img.resize((224,224)) 
    print(f"Resizing {file}....") # Print to keep track of progress
    img.save(f_img)

print("All Done!")