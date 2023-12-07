from flask import Flask, render_template, request
import pytesseract
import os
from PIL import Image
import datetime
pytesseract.pytesseract.tesseract_cmd=r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe" #Bu kısmı kendi bilgisayarınızda güncelleyin
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Dosya yüklemek için POST isteği
@app.route('/', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(filename)
        extracted_text = ocr(filename)
        dosya = os.stat(filename)
        olususm = datetime.datetime.fromtimestamp(dosya.st_ctime)
        erisim = datetime.datetime.fromtimestamp(dosya.st_atime) 
        degisism = datetime.datetime.fromtimestamp(dosya.st_mtime) 
        boyut = f"{dosya.st_size}"
        dosya_adi = f"{filename}"
        ersism_tarihi = f"{erisim}"
        olusum_tarihi = f"{olususm}"
        degisism = f"{degisism}"
        

        os.remove(filename)


        return render_template('index.html', text=extracted_text,
                               dosayadi=dosya_adi,
                               erisim_tarihi=ersism_tarihi,
                               dosya_olusum_tarihi=olusum_tarihi,
                               dosya_boyutu = boyut,
                               degsism =degisism ) 

    return render_template('index.html')

def ocr(filename):
    image = Image.open(filename)
    image.show()
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text


if __name__ == '__main__':
    app.run(debug=True)
    app = Flask(__name__, template_folder="templates")

