from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import os

# ← Add this line
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

# single file upload
# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return "No file uploaded", 400
#     file = request.files['file']
#     if file.filename == '':
#         return "No selected file", 400

#     filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#     file.save(filepath)

#     text = pytesseract.image_to_string(Image.open(filepath))
    
#     return render_template('result.html', extracted_text=text)

# multiple file upload
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'files' not in request.files:
        return "No files uploaded", 400

    files = request.files.getlist('files')
    if not files:
        return "No files selected", 400

    extracted_texts = []

    for file in files:
        if file.filename == '':
            continue
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        # OCR
        text = pytesseract.image_to_string(Image.open(filepath))
        extracted_texts.append({'filename': file.filename, 'text': text})

    return render_template('result.html', extracted_texts=extracted_texts)


if __name__ == "__main__":
    app.run(debug=True)
