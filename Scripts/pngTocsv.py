# Enable the base env in conda
# Convert images from .png to .csv for all shape_*.png files in directory

from PIL import Image
import numpy as np
import pandas as pd
import os
import glob

def convert_png_to_csv(png_file, csv_file):
    """Convert a single PNG file to CSV format with proper structure"""
    try:
        # Load the image and convert to numpy array
        img = Image.open(png_file)
        img_array = np.array(img)
        
        # Get image dimensions
        height, width = img_array.shape[:2]
        
        # Create lists to store pixel data
        x_coords = []
        y_coords = []
        pixel_values = []
        
        # Extract pixel coordinates and values
        for y in range(height):
            for x in range(width):
                x_coords.append(x)
                y_coords.append(y)
                
                # Handle different image formats
                if len(img_array.shape) == 3:  # Color image (RGB/RGBA)
                    # Convert RGB to a single value or use grayscale
                    if img_array.shape[2] == 3:  # RGB
                        pixel_val = np.mean(img_array[y, x])  # Convert to grayscale
                    else:  # RGBA
                        pixel_val = np.mean(img_array[y, x, :3])  # Ignore alpha, convert to grayscale
                else:  # Grayscale image
                    pixel_val = img_array[y, x]
                
                pixel_values.append(pixel_val)
        
        # Create DataFrame with the expected column structure
        df = pd.DataFrame({
            'x': x_coords,
            'y': y_coords,
            'Object': pixel_values
        })
        
        # Save to CSV
        df.to_csv(csv_file, index=False)
        
        print(f"Successfully converted: {png_file} -> {csv_file}")
        print(f"  Image size: {width}x{height}, Total pixels: {len(df)}")
        return True
    
    except Exception as e:
        print(f"Error converting {png_file}: {str(e)}")
        return False

def convert_png_to_csv_binary(png_file, csv_file, threshold=128):
    """
    Alternative: Convert PNG to CSV with binary classification
    Useful for shape detection where you want to classify pixels as shape/background
    """
    try:
        # Load the image and convert to numpy array
        img = Image.open(png_file).convert('L')  # Convert to grayscale
        img_array = np.array(img)
        
        # Get image dimensions
        height, width = img_array.shape
        
        # Create lists to store pixel data
        x_coords = []
        y_coords = []
        object_labels = []
        
        # Extract pixel coordinates and classify as shape (1) or background (0)
        for y in range(height):
            for x in range(width):
                x_coords.append(x)
                y_coords.append(y)
                
                # Binary classification: 1 if pixel is darker than threshold (likely shape)
                object_label = 1 if img_array[y, x] < threshold else 0
                object_labels.append(object_label)
        
        # Create DataFrame with the expected column structure
        df = pd.DataFrame({
            'x': x_coords,
            'y': y_coords,
            'Object': object_labels
        })
        
        # Save to CSV
        df.to_csv(csv_file, index=False)
        
        print(f"Successfully converted: {png_file} -> {csv_file}")
        print(f"  Image size: {width}x{height}, Shape pixels: {sum(object_labels)}")
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
    
    # Ask user which conversion method to use
    print("\nChoose conversion method:")
    print("1. Grayscale values (default)")
    print("2. Binary classification (shape detection)")
    
    choice = input("Enter choice (1 or 2, default=1): ").strip()
    use_binary = choice == '2'
    
    if use_binary:
        threshold = input("Enter threshold for binary classification (0-255, default=128): ").strip()
        try:
            threshold = int(threshold) if threshold else 128
        except ValueError:
            threshold = 128
        print(f"Using binary classification with threshold: {threshold}")
    
    # Convert each PNG file to CSV
    successful_conversions = 0
    failed_conversions = 0
    
    for png_file in png_files:
        # Generate corresponding CSV filename
        base_name = os.path.splitext(os.path.basename(png_file))[0]
        csv_file = os.path.join(current_dir, f"{base_name}.csv")
        
        # Convert the file using chosen method
        if use_binary:
            success = convert_png_to_csv_binary(png_file, csv_file, threshold)
        else:
            success = convert_png_to_csv(png_file, csv_file)
        
        if success:
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
