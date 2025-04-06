import os
import shutil

# Define source and destination directories
source_dir = r"C:\Users\clint\Desktop\Lifecycle_RA\Data\Compressed_Images"
dest_dir = r"C:\Users\clint\Desktop\Lifecycle_RA\Data\Processed\Sorted_Images"

# List of target image files to find and copy
target_files = [
    "06_2019_plot_3_See_the_Average_Retail_Selling_Price_3-5_Year-Old_.png",
    "07_2019_plot_3_See_the_Average_Retail_Selling_Price_3-5_Year-Old_.png",
    "11_2019_plot_3.png"
]

print(f"Searching for target files in: {source_dir}")
print(f"Will copy to: {dest_dir}")

# Ensure destination directory exists
if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)
    print(f"Created destination directory: {dest_dir}")

# Search for and copy the files
found_files = 0
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file in target_files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_dir, file)
            
            # Copy file, replacing if it exists
            shutil.copy2(source_path, dest_path)
            
            print(f"Copied: {file}")
            print(f"  From: {source_path}")
            print(f"  To: {dest_path}")
            
            found_files += 1

print(f"\nOperation complete: {found_files}/{len(target_files)} files copied.")
if found_files < len(target_files):
    print("Warning: Some files were not found in the source directory.")
