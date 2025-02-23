import easyocr
import pytesseract
import cv2
import os

def extract_text_with_easyocr(image_path):
    reader = easyocr.Reader(['en'], gpu=False)
    result = reader.readtext(image_path, detail=0)
    return "\n".join(result).strip()

def extract_text_with_tesseract(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text.strip()

def extract_text_from_image(image_path, ocr_choice):
    try:
        if not os.path.exists(image_path):
            return f"Error: File {image_path} does not exist."
        
        if ocr_choice == '1':
            return extract_text_with_easyocr(image_path)
        elif ocr_choice == '2':
            return extract_text_with_tesseract(image_path)
        else:
            return "Invalid OCR choice. Please select either 1 or 2."
    except Exception as e:
        return f"Error: {e}"

def process_images_in_folder(folder_path, ocr_choice):
    if not os.path.exists(folder_path):
        print(f"Error: Folder {folder_path} does not exist.")
        return
    
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg'))]
    if not image_files:
        print("No valid image files found in the folder.")
        return
    
    for filename in image_files:
        image_path = os.path.join(folder_path, filename)
        extracted_text = extract_text_from_image(image_path, ocr_choice)
        print(f"Extracted Text from {filename}:{extracted_text}\n")

def main():
    folder_path = input("Enter the path to the folder containing images: ").strip()
    print("Choose OCR engine:")
    print("1. EasyOCR")
    print("2. Tesseract OCR")
    ocr_choice = input("Enter your choice (1 or 2): ").strip()
    process_images_in_folder(folder_path, ocr_choice)

if __name__ == "__main__":
    main()
