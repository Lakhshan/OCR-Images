# OCR Text Extraction from Images

## 📌 Overview  
This Python script extracts text from multiple `.jpg` and `.jpeg` images in a folder using **Optical Character Recognition (OCR)**.  
The user can choose between two OCR engines:  

✅ **EasyOCR** – Supports multiple languages, better accuracy for some cases.  
✅ **Tesseract OCR** – Fast and widely used open-source OCR engine.  

---

## ⚡ Features  
- 🔹 Extracts text from multiple images in a folder  
- 🔹 Supports **EasyOCR** and **Tesseract OCR**  
- 🔹 Works with `.jpg` and `.jpeg` images  
- 🔹 Converts images to grayscale for better OCR accuracy (Tesseract)  

---

## 🛠 Installation  

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2️⃣ Install Dependencies
Ensure you have Python 3 installed (python3 --version). Then, install the required libraries:
```bash
pip install easyocr opencv-python pytesseract
```
### 3️⃣ Install Tesseract OCR (if using Tesseract)
Windows: Download & Install Tesseract


🚀 Usage
Run the Script
```bash
python ocr_script.py
```
Input Steps:
1️⃣ Enter the folder path containing the images.
2️⃣ Choose an OCR engine:

1 → EasyOCR

2 → Tesseract OCR

3 → The script will process all .jpg and .jpeg images in the folder and display the extracted text

## Output:
- With EasyOCR
  ```
  Enter the path to the folder containing images: Task1
  Choose OCR engine:
  1. EasyOCR
  2. Tesseract OCR
  Enter your choice (1 or 2): 1
  Using CPU. Note: This module is much faster with a GPU.
  Extracted Text from capchas (1).jpeg:NRSVR

  Using CPU. Note: This module is much faster with a GPU.
  Extracted Text from capchas (2).jpeg:IcTT TX5

  Using CPU. Note: This module is much faster with a GPU.
  Extracted Text from display (1).jpg:1/16

  Using CPU. Note: This module is much faster with a GPU.
  Extracted Text from display (2).jpg:AUTO
  AC
  668

  Using CPU. Note: This module is much faster with a GPU.
  Extracted Text from display (3).jpg:acoccu
  ```
  
- With Tesseract OCR
  ```
  Enter the path to the folder containing images: Task1
  Choose OCR engine:
  1. EasyOCR
  2. Tesseract OCR
  Enter your choice (1 or 2): 2
  Extracted Text from capchas (1).jpeg:

  Extracted Text from capchas (2).jpeg:

  Extracted Text from display (1).jpg:

  Extracted Text from display (2).jpg:

  Extracted Text from display (3).jpg:b

  \4
  ```
  
## Conclusion:
From EasyOCR and Tesseract OCR ,EasyOCR give a better response with Captcha and Numerical Values but is not fully accurate 
  


