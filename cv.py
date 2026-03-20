import os
import cv2

def convert_to_grayscale(input_dir, output_dir):
    """Batch convert images to grayscale."""
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_dir, filename)
            img = cv2.imread(image_path)
            
            if img is not None:
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                cv2.imwrite(os.path.join(output_dir, filename), gray_img)
                print(f"Successfully converted: {filename}")
            else:
                print(f"Failed to read: {filename}")

if __name__ == "__main__":
    convert_to_grayscale("images", "gray_images")
    print("Batch processing complete.")
if __name__ == "__main__":
    convert_to_grayscale("images", "gray_images")
    print("Batch processing complete.")