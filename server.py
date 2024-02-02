from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
CORS(app)

# Configuration




from ScheduleScreen import inputScheduleFunctions

@app.route('/upload', methods=['POST'])
def file_upload():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    file = request.files['file']

    
    if file.filename == '':
        return jsonify({'message': 'No file selected for uploading'}), 400


    # Start
    
    file_content = file.read()

    # print(file_content)

    userID = "fake"

    inputScheduleFunctions.inputSchedule(userID=userID, file_content=file_content)
    

    return jsonify({'message': 'File successfully uploaded'}), 200

@app.route('/')
def hello_world():
    return {'name': "Rayyan", "major" : "Computer Science"}

if __name__ == '__main__':
    # Ensure the upload folder exists
    app.run(host="0.0.0.0")
