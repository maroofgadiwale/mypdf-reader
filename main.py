# Program:
from flask import *
from pdf_read import read_file
import os

flag = 0
uploaded = False
my_file = None

# Flask code:
app = Flask(__name__)

# Set the upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')  # Full path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Loading home route:
@app.route("/")
def home():
    global uploaded
    return render_template("index.html",val = uploaded)

# Reading a file:
def read_data(file):
    if uploaded:
        read_file(file)

# For uploading pdf:
@app.route('/upload', methods=['POST'])
def upload_pdf():
    global uploaded,my_file
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        my_file = file.filename
        uploaded = True
        read_data(my_file)
        return redirect(url_for('home'))

    return "Invalid file type. Please upload a PDF"


if __name__ == "__main__":
    app.run(debug = True)