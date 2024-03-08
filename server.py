from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



from Authentication import signin

@app.route('/getUID' , methods=["GET"])
def getUID():
    # Using request.args.get for GET request query parameters
    phoneNumber = request.args.get('phoneNumber')
    if not phoneNumber:
        return jsonify({'message': 'Missing phone number'}), 400

    phoneNumber = "+1" + phoneNumber
    # Assuming signin.getUID is a function that exists and works correctly
    success, data = signin.getUID(phoneNumber)
    
    if success:
        uid = data  # Assuming you do something with uid here
        return jsonify({'uid': uid}), 200
    else:
        message = data
        return jsonify({'message': message}), 200
        

    
    
    return jsonify({'message' : f'Got UID {uid} from user with phone number {phoneNumber}'}), 200  


from ScheduleScreen import inputScheduleFunctions

@app.route('/upload', methods=['POST'])
def uploadSchedule():


    

    if 'file' not in request.files:
        return jsonify({'message': 'No file part in the request'}), 400

    if 'uid' not in request.form:
        return jsonify({'message': 'No uid part in the request'}), 400
    
    file = request.files['file']
    uid : str = request.form['uid']


    print(f"User with uid {uid} is requesting to upload their schedule")
    
    # Start
    
    file_content = file.read()

    inputScheduleFunctions.inputSchedule(userID=uid, file_content=file_content)
    

    return jsonify({'message': 'File successfully uploaded'}), 200


from ScheduleScreen import displayScheduleFunctions

from ScheduleScreen import deleteScheduleFunctions

@app.route('/removeSchedule', methods=['GET'])
def removeSchedule():
    if request.method == "GET":
        
        
        uid = request.args.get('uid')

        print(f"User with uid {uid} is requesting to delete their schedule")


        deleteScheduleFunctions.deleteSchedule(uid)

        return jsonify({'message': 'Schedule successfully deleted'}), 200
    

@app.route('/displaySchedule', methods= ['GET'])

def getScheduleInfo():

    if request.method == "GET":
        
        
        uid = request.args.get('uid')

        print(f"User with uid {uid} is requesting to display their schedule")


        scheduleDictionaryArray = displayScheduleFunctions.getSchedule(uid=uid)

        validSchedule = False
        for eachDay in scheduleDictionaryArray:
            if len(eachDay) >= 1:
                validSchedule = True
                break
        
        if validSchedule:
            return jsonify({'message' : "Schedule successfully recieved" , "scheduleDictionaryArray" : scheduleDictionaryArray}) , 200
        else:
            return jsonify({'message' : "No schedule exists" , "scheduleDictionaryArray" : None}) , 400


from Graph.Navigation import Navigation

@app.route('/getShortestPath', methods = ['GET'])

def getShortestPath():


    userLocation2 = [33.97898832695682, -117.3281625439988, 336.1064619679466]
		
    # userLocation3 = [33.97933637566715, -117.3274747670374, 324.056714825594]
    # userLocation27 = [33.97496349102106, -117.3276715484908,322.0736351996588]
    # userLocation30 = [33.97571667778362, -117.3286881329295,317.4348304680136] 

    # userLocation31 = [33.97574694711781, -117.3289767658347,329.8933058297193] 
    userLocation37 = [33.97488141666391, -117.3286340179911,318.9579109074609]
    userLocation56 = [33.97304235807492,-117.3289763431564,325.5321034647867]

    userLocation49 = [33.97333329408798,-117.3277204388097,322.828737781892]

    userLocation98 = [33.97203958907053,-117.3301287489703,321.8734107055374]
    if request.method == "GET":

        uid = request.args.get("uid")

        latitude = request.args.get("latitude")
        longitude = request.args.get("longitude")
        altitude = request.args.get("altitude")

        userLocation = [latitude, longitude, altitude]
        destinationBuildingName = request.args.get("classBuildingName")     
        
   

        navigationObject : Navigation = Navigation(userLocation, destinationBuildingName)

        navigationObject.setClosestNodeToUser()
        navigationObject.setBuildingNodes()
        navigationDictionary = navigationObject.getShortestPathNodesAndEdges()
        

        # navigationDictionary = {

        #     'nodes' : [
        #     {
        #         "name" : 'START LOCATION',
        #         "location" : ['33.9772220292684', '-117.3288839729353', '319.041168566382']
        #     },
        #     {
        #         "name" : 'INTERSECTION',
        #         "location": ['33.97722599505837', '-117.327048181778', '323.2461087977744']
        #     },

        #     {
        #         "name" : 'INTERSECTION',
        #         "location" : ['33.97622239025886', '-117.3270718964966', '319.2197948933198']
        #     },
            
        #     {
        #          "name" : 'Materials Sci and Engineering',
        #          "location": ['33.97622378123113', '-117.3273110476977', '333.6064893163547']
        #     }
        # ],
        
        # 'edges' : [

        #     {
        #         "arrayOfCoordinates" : [[33.97722238313204, -117.3288843282884] , [33.97722693465821, -117.3270470095061]],
        #         "time" : 20
        #         "length" : 10
        #     }, 
            
        #     {
        #         "arrayOfCoordinates" : [[33.97722684480606, -117.3270457771456], [33.97666268449692, -117.3270477321467], [33.9766302339203, -117.3270697906512], [33.97622268242515, -117.3270711398879]],
        #           "time" : 20
        #           "length" : 10
        #     },

        #     {
        #         "arrayOfCoordinates" : [[33.97622391252066, -117.3273108312102], [33.97622285790032, -117.3270715326373]],
        #         "time" : 20
        #         "length" : 10          
        #     },   
        
        # ],

        # 'totalTime' : 3.45,

        # 'totalLength' : 400



        # }
        
        

    return jsonify(navigationDictionary)

@app.route('/')
def hello_world():
    return {'name': "Rayyan", "major" : "Computer Science"}

if __name__ == '__main__':
    # Ensure the upload folder exists
    app.run(host="0.0.0.0")
