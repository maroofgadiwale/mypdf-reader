from flask import Flask, render_template, request, redirect, url_for
from pdf_read import read_file
import os

flag = 0
uploaded = False
my_file = None

# Flask app
app = Flask(__name__)

# Use /tmp/ instead of uploads/
UPLOAD_FOLDER = "/tmp"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the /tmp/ directory exists (this is just a safety check, usually not needed for /tmp/)
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Home route
@app.route("/")
def home():
    global uploaded
    return render_template("index.html", val=uploaded)

# Read file function
def read_data(file_path):
    if uploaded:
        read_file(file_path)  # Pass full file path

# Upload PDF route
@app.route('/upload', methods=['POST'])
def upload_pdf():
    global uploaded, my_file

    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']

    if file.filename == '':
        return "No selected file"

    if file and file.filename.endswith('.pdf'):
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)  # Save in /tmp/
        my_file = filepath  # Store full path
        uploaded = True
        read_data(my_file)  # Pass full file path
        return redirect(url_for('home'))

    return "Invalid file type. Please upload a PDF"

if __name__ == "__main__":
    app.run(debug=True)
