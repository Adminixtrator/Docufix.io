import os
from flask import Flask, render_template, request
import requests
import pytesseract as pt
from PIL import Image
from PIL import ImageFilter

#pt.pytesseract.tesseract_cmd = '/app/.apt/usr/bin/tesseract'
#pt.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

# import our OCR function

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    img = _get_image(filename)
    img.filter(ImageFilter.SHARPEN)
    #img = Image.open(filename)
    text = pt.image_to_string(img)  # We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
    return text
 


# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/fileUpload.html')
def fileUpload():
    return render_template('fileUpload.html')


@app.route('/paraphrase.html')
def paraphrase():
    return render_template('paraphrase.html')


@app.route('/plagiarismChecker.html')
def plagiarismchecker():
    return render_template('plagiarismchecker.html')


@app.route('/faq.html')
def faq():
    return render_template('faq.html')

@app.route('/fileDuplicate.html')
def fileDuplicate():
    return render_template('fileDuplicate.html')


@app.route('/grammarChecker.html')
def grammarChecker():
    return render_template('grammarChecker.html')


@app.route('/header&footer.html')
def headerfooter():
    return render_template('header&footer.html')


@app.route('/disclaimer.html')
def disclaimer():
    return render_template('disclaimer.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/checkout.html')
def checkout():
    return render_template('checkout.html')


@app.route('/about_us.html')
def about_us():
    return render_template('about_us.html')


@app.route('/404_error.html')
def error():
    return render_template('404_error.html')


@app.route('/privacy.html')
def privacy():
    return render_template('privacy.html')


@app.route('/profile.html')
def profile():
    return render_template('profile.html')


@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/teampage.html')
def teampage():
    return render_template('teampage.html')

@app.route('/teampage-2.html')
def teampage_2():
    return render_template('teampage-2.html')

@app.route('/teampage-3.html')
def teampage_3():
    return render_template('teampage-3.html')

@app.route('/teampage-4.html')
def teampage_4():
    return render_template('teampage-4.html')

@app.route('/teampage-5.html')
def teampage_5():
    return render_template('teampage-5.html')

@app.route('/teampage-6.html')
def teampage_6():
    return render_template('teampage-6.html')

@app.route('/teampage-7.html')
def teampage_7():
    return render_template('teampage-7.html')

@app.route('/teampage-8.html')
def teampage_8():
    return render_template('teampage-8.html')

@app.route('/termsOfService.html')
def termsOfService():
    return render_template('termsOfService.html')

@app.route('/why-use-docufix.html')
def why_use_docufix():
    return render_template('why-use-docufix.html')


@app.route('/imageScanner.html', methods=['GET', 'POST'])
def imageScanner():
    if request.method == 'POST':
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('imageScanner.html', msg='No file selected')
        file1 = request.files['file']
        # if no file is selected
        if file1.filename == '':
            return render_template('imageScanner.html', msg='No file selected')

        if file1 and allowed_file(file1.filename):

            # call the OCR function on it
            extracted_text = ocr_core(file1)

            # extract the text and display it
            return render_template('imageScanner.html',
                                   msg='Successfully processed',
                                   extracted_text=extracted_text)
    elif request.method == 'GET':
        return render_template('imageScanner.html')


if __name__ == '__main__':
    app.run()
