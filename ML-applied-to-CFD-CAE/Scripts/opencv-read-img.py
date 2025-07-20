import cv2
import easyocr
import pandas as pd
import numpy as np

# Set the path to the Tesseract executable (based on your system)
#pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'  # ← update this if different

# Load the image using OpenCV
image = cv2.imread('/home/gadalf/Python/Machine_learning_Deep_learning/input/pg1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# Apply adaptive thresholding for binarization
thresh = cv2.adaptiveThreshold(blurred, 255, 
                               cv2.ADAPTIVE_THRESH_MEAN_C, 
                               cv2.THRESH_BINARY_INV, 
                               21, 15)

# Optional: dilate to connect broken text lines
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
dilated = cv2.dilate(thresh, kernel, iterations=1)

# Compute vertical projection to detect column gap
vertical_sum = np.sum(dilated, axis=0)
mid_x = len(vertical_sum) // 2

# Heuristic: split into two halves
left_col = image[:, :mid_x]
right_col = image[:, mid_x:]

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

def ocr_and_group(image_column):
    results = reader.readtext(image_column)
    lines = []
    current_line = []
    last_y = None

    for (bbox, text, confidence) in results:
        top_left = bbox[0]
        y = top_left[1]

        if last_y is None or abs(y - last_y) < 15:
            current_line.append(text)
        else:
            lines.append(current_line)
            current_line = [text]
        last_y = y

    if current_line:
        lines.append(current_line)
    return lines

# OCR on each column
left_lines = ocr_and_group(left_col)
right_lines = ocr_and_group(right_col)

# Combine both columns side-by-side (row-wise)
max_len = max(len(left_lines), len(right_lines))
combined_lines = []

for i in range(max_len):
    left = ' '.join(left_lines[i]) if i < len(left_lines) else ''
    right = ' '.join(right_lines[i]) if i < len(right_lines) else ''
    combined_lines.append([left, right])

# Save to CSV
df = pd.DataFrame(combined_lines, columns=['Left Column', 'Right Column'])
df.to_csv('pg1_two_columns.csv', index=False)