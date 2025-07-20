#enable the base env in conda
#convert the images from .png to .csv
from PIL import Image
import numpy as np
import csv
import os
import glob

#img = np.array(Image.open("cylinder.png"))
#with open("cylinder.csv", "w", newline="") as csvfile:
#    writer = csv.writer(csvfile, delimiter=",")
#    writer.writerows(img)
# Enable the base env in conda
# Convert images from .png to .csv for all shape_*.png files in directory


def convert_png_to_csv(png_file, csv_file):
    """Convert a single PNG file to CSV format"""
    try:
        # Load the image and convert to numpy array
        img = np.array(Image.open(png_file))
        
        # Write to CSV file
        with open(csv_file, "w", newline="") as csvfile:
            writer = csv.writer(csvfile, delimiter=",")
            writer.writerows(img)
        
        print(f"Successfully converted: {png_file} -> {csv_file}")
        return True
    
    except Exception as e:
        print(f"Error converting {png_file}: {str(e)}")
        return False

def main():
    # Get current directory
    current_dir = os.getcwd()
    
    # Find all PNG files matching the pattern "shape_*.png"
    png_pattern = os.path.join(current_dir, "shape_*.png")
    png_files = glob.glob(png_pattern)
    
    if not png_files:
        print("No PNG files matching pattern 'shape_*.png' found in current directory")
        return
    
    print(f"Found {len(png_files)} PNG files to convert:")
    for file in png_files:
        print(f"  - {os.path.basename(file)}")
    
    # Convert each PNG file to CSV
    successful_conversions = 0
    failed_conversions = 0
    
    for png_file in png_files:
        # Generate corresponding CSV filename
        # Extract filename without extension and add .csv
        base_name = os.path.splitext(os.path.basename(png_file))[0]
        csv_file = os.path.join(current_dir, f"{base_name}.csv")
        
        # Convert the file
        if convert_png_to_csv(png_file, csv_file):
            successful_conversions += 1
        else:
            failed_conversions += 1
    
    # Print summary
    print(f"\nConversion Summary:")
    print(f"  - Successful: {successful_conversions}")
    print(f"  - Failed: {failed_conversions}")
    print(f"  - Total: {len(png_files)}")

if __name__ == "__main__":
    main()
