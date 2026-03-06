import os
import cv2

input_folder = "images"
output_folder = "gray_images"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    img = cv2.imread(os.path.join(input_folder, file))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imwrite(os.path.join(output_folder, file), gray)

print("Converted all images to grayscale")