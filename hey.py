import os
import cv2

input_folder = "images"
output_folder = "bw_images"

# create output folder if not exists
if not os.path.exists(output_folder):
    os.mkdir(output_folder)

count = 0

for file in os.listdir(input_folder):

    file_path = os.path.join(input_folder, file)

    # skip non-image files
    if not file.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    img = cv2.imread(file_path)

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # resize image
    resized = cv2.resize(gray, (300, 300))

    # apply blur
    blur = cv2.GaussianBlur(resized, (5,5), 0)

    # edge detection
    edges = cv2.Canny(blur, 50, 150)

    # new filename
    new_name = f"processed_{count}.jpg"

    save_path = os.path.join(output_folder, new_name)

    cv2.imwrite(save_path, edges)

    print(f"Processed: {file}")

    count += 1

print("All images processed successfully!")