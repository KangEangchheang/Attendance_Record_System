import os
import flask
from flask import request, jsonify
from flask_cors import CORS


# Initialize Flask app
app = flask.Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'saved_faces'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
    
def allowed_file(filename):
    """Check if the file has an allowed extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return "Welcome to the Car Price Prediction API!"


@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if a file is included in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    custom_filename = request.form.get('file_name')  # This is a string

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Check if the file has an allowed extension
    if not allowed_file(file.filename):
        return jsonify({'error': 'File type not allowed'}), 400

    # Save the file to the upload folder
    filename = os.path.join(app.config['UPLOAD_FOLDER'], custom_filename)
    file.save(filename)

    return jsonify({'message': 'File uploaded successfully', 'filename': custom_filename}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
