import flask
from flask import request, jsonify
from flask_cors import CORS


# Initialize Flask app
app = flask.Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Car Price Prediction API!"


# Run the app
if __name__ == '__main__':
    app.run(debug=True, threaded=True)
