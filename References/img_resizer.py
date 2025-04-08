import os
import cv2
import numpy as np

# Directory containing images
image_dir = r"C:\Users\clint\Desktop\Lifecycle_RA\Data\Processed\Sorted_Images"
# Directory to save processed images
output_dir = r"C:\Users\clint\Desktop\Lifecycle_RA\Data\Processed\Cropped_Images"

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Global variables for mouse callback
clicked_y = None
click_done = False

# Mouse callback function
def mouse_callback(event, x, y, flags, param):
    global clicked_y, click_done
    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_y = y
        click_done = True
        print(f"Point clicked at y = {y}")

def process_images():
    global clicked_y, click_done
    
    # Get list of all image files
    image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    if not image_files:
        print("No image files found in the directory.")
        return
    
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mouse_callback)
    
    for image_file in image_files:
        image_path = os.path.join(image_dir, image_file)
        image = cv2.imread(image_path)
        
        if image is None:
            print(f"Could not open or find the image: {image_file}")
            continue
        
        # Display the image
        cv2.imshow("Image", image)
        print(f"Processing image: {image_file}")
        
        # Ask user if they want to keep or delete
        while True:
            response = input("Do you want to keep (k) or delete (d) this image? ").lower()
            if response in ['k', 'd']:
                break
            print("Invalid input. Please enter 'k' for keep or 'd' for delete.")
        
        if response == 'd':
            print(f"Skipping {image_file}")
            cv2.waitKey(1)  # Small delay to refresh the window
            continue
        
        # User wants to keep the image, ask for a click point
        print("Please click a point on the image to define the crop line.")
        clicked_y = None
        click_done = False
        
        while not click_done:
            cv2.imshow("Image", image)
            key = cv2.waitKey(100)  # Check for click every 100ms
            if key == 27:  # ESC key to exit
                return
        
        # Crop the image keeping only the portion below the Y coordinate
        cropped_image = image[clicked_y:, :]
        
        # Show the cropped result briefly
        cv2.imshow("Cropped Result", cropped_image)
        cv2.waitKey(1000)  # Show for 1 second
        
        # Save the cropped image
        output_path = os.path.join(output_dir, f"cropped_{image_file}")
        cv2.imwrite(output_path, cropped_image)
        print(f"Saved cropped image to {output_path}")
    
    cv2.destroyAllWindows()
    print("All images processed.")

if __name__ == "__main__":
    process_images()
