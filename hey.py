import os
import cv2

def process_images(input_dir, output_dir, target_size=(300, 300)):
    """Apply blur and edge detection to images in input_dir and save to output_dir."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    processed_count = 0
    
    for filename in os.listdir(input_dir):
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        file_path = os.path.join(input_dir, filename)
        img = cv2.imread(file_path)

        if img is None:
            print(f"Skipping (could not read): {filename}")
            continue

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Resize image
        resized = cv2.resize(gray, target_size)

        # Apply blur
        blur_img = cv2.GaussianBlur(resized, (5, 5), 0)

        # Edge detection
        edges = cv2.Canny(blur_img, 50, 150)

        # Save with a standardized name
        new_filename = f"processed_{processed_count:03d}.jpg"
        save_path = os.path.join(output_dir, new_filename)
        cv2.imwrite(save_path, edges)

        print(f"Processed: {filename} -> {new_filename}")
        processed_count += 1

    print(f"Finished processing {processed_count} images.")

if __name__ == "__main__":
    process_images("images", "bw_images")