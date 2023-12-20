import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Users\Lenovo\AppData\Local\Tesseract-OCR\tesseract.exe'

# Load image using OpenCV
image = cv2.imread(r'D:\DL projects\OCR\bussiness card.jpg')

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Perform edge detection using Canny
edges = cv2.Canny(blur, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filter contours based on area, aspect ratio, etc., to identify potential text regions

# Loop through potential text regions and extract text using Tesseract OCR
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    text_region = image[y:y+h, x:x+w]
    
    # Perform OCR on the text region
    text = pytesseract.image_to_string(text_region, config='--psm 6')
    print(text)

    # Process the extracted text (e.g., print or store it)

# Display the original image with highlighted text regions
cv2.imshow('Business Card', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
