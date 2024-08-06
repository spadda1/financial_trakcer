from PIL import Image
import pytesseract

def extract_text(image_path):
    # Open an image file
    image = Image.open(image_path)
    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)
    return text

if __name__ == "__main__":
    # Path to your receipt image
    image_path = "payment.jpg"
    # Extract text from the image
    extracted_text = extract_text(image_path)
    # Print the extracted text
    print(extracted_text)
