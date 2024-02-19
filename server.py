from flask import Flask, jsonify, request
from flask_cors import CORS

import time
app = Flask(__name__)
CORS(app)

from ScheduleScreen import inputScheduleFunctions
from Graph.Navigation import Navigation

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
        scheduleDictionaryArray, currentDay = displayScheduleFunctions.getSchedule(uid=uid)

        
        return jsonify({'message' : "Schedule successfully recieved" , "scheduleDictionaryArray" : scheduleDictionaryArray, 'currentDay' : currentDay}) , 200







@app.route('/getShortestPath', methods = ['GET'])

def getShortestPath():

    if request.method == "GET":

        uid = request.args.get("uid")



        userLocation = [33.975931, -117.329059, 0.0] 
        destinationBuildingName = "Materials Sci and Engineering" 

        navigationObject : Navigation = Navigation(userLocation, destinationBuildingName)


        navigationDictionary = navigationObject.getShortestPathNodesAndEdges()
        

        navigationDictionary = {

            'nodes' : [
            {
                "name" : 'START LOCATION',
                "location" : ['33.9772220292684', '-117.3288839729353', '319.041168566382']
            },
            {
                "name" : 'INTERSECTION',
                "location": ['33.97722599505837', '-117.327048181778', '323.2461087977744']
            },

            {
                "name" : 'INTERSECTION',
                "location" : ['33.97622239025886', '-117.3270718964966', '319.2197948933198']
            },
            
            {
                 "name" : 'Materials Sci and Engineering',
                 "location": ['33.97622378123113', '-117.3273110476977', '333.6064893163547']
            }
        ],
        
        'edges' : [

            {
                "arrayOfCoordinates" : [[33.97722238313204, -117.3288843282884] , [33.97722693465821, -117.3270470095061]],

            }, 
            
            {
                "arrayOfCoordinates" : [[33.97722684480606, -117.3270457771456], [33.97666268449692, -117.3270477321467], [33.9766302339203, -117.3270697906512], [33.97622268242515, -117.3270711398879]],
    
            },

            {
                "arrayOfCoordinates" : [[33.97622391252066, -117.3273108312102], [33.97622285790032, -117.3270715326373]],
          
            },   
        
        ],

        'time' : 20,

        'length' : 400



        }
        
        

    return jsonify(navigationDictionary)

@app.route('/')
def hello_world():
    return {'name': "Rayyan", "major" : "Computer Science"}

if __name__ == '__main__':
    # Ensure the upload folder exists
    app.run(host="0.0.0.0")
