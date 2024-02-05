from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from ScheduleScreen import inputScheduleFunctions

@app.route('/upload', methods=['POST'])
def uploadSchedule():


    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    if 'uid' not in request.form:
        return jsonify({'message': 'No uid part in the request'}), 400
    
    file = request.files['file']
    uid : str = request.form['uid']



    # Start
    
    file_content = file.read()

    inputScheduleFunctions.inputSchedule(userID=uid, file_content=file_content)
    

    return jsonify({'message': 'File successfully uploaded'}), 200


from ScheduleScreen import displayScheduleFunctions

@app.route('/displaySchedule', methods= ['GET'])

def getScheduleInfo():

    if request.method == "GET":

        print("YAY")
        uid = request.args.get('uid')
        scheduleDictionary = displayScheduleFunctions.getSchedule(uid=uid)

        return jsonify({'message' : "Schedule successfully recieved" , "scheduleDictionary" : scheduleDictionary}) , 200

@app.route('/')
def hello_world():
    return {'name': "Rayyan", "major" : "Computer Science"}

if __name__ == '__main__':
    # Ensure the upload folder exists
    app.run(host="0.0.0.0")
