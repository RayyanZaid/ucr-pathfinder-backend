from enum import Enum
import xml.etree.ElementTree as ET
import re



class NodeType(Enum):

    BUILDING = 1
    ROOM = 2
    INTERSECTION = 3
    PARKING_LOT = 4
    LIVINGAREA = 5
    RECREATION = 6

stringToEnum = {
    "BUILDING" : NodeType.BUILDING,
    "INTERSECTION" : NodeType.INTERSECTION,
    "PARKING_LOT" : NodeType.PARKING_LOT,
    "LIVIINGAREA" : NodeType.LIVINGAREA,
    "RECREATION" : NodeType.RECREATION,
    "ROOM" : NodeType.ROOM
}


class Node:

    def __init__(self, name : str, nodeID: str, location : list, type : NodeType) -> None:
        
        self.name = name

        self.nodeID = nodeID
                            # latitude, longitude, altitude
        self.location : list = location

        self.type : NodeType = type


        # list of Edge objects
        self.edges : list = []

    def addEdge(self, edge):

        self.edges.append(edge)


# BuildingNode and RoomNode inherit from Node
        
class BuildingNode(Node):
    
    def __init__(self, name: str, nodeID: str, location: list, type: NodeType, buildingName : str):

        super().__init__(name, nodeID, location, type)
        
        self.buildingName = buildingName
        self.roomNodeIDs : list[str] = []
        

    def addRoom(self,nodeID : str):

        self.roomNodeIDs.append(nodeID)


class RoomNode(Node):
    def __init__(self, name: str, nodeID: str, location: list, type: NodeType, roomName: str, buildingName: str):
        super().__init__(name, nodeID, location, type)

        self.roomName = roomName
        self.buildingName = buildingName
        

class AutomateNodeCreation:

    def __init__(self, googleEarthFilePath) -> None:
        
        self.filePath = googleEarthFilePath

    
    def parse_info_from_name(self, nameFromGoogleEarth) -> str:
        # Check for EDGE case
        if nameFromGoogleEarth.startswith("EDGE"):
            return "No match found."

        # Define regex patterns for each naming convention
        patterns = {
            "BUILDING": re.compile(r"^BUILDING_([^_]+)_(\d+)$"),

                            # ex. ROOM_B118_Bourns Hall_178
            "ROOM" : re.compile(r"ROOM_([^_]+)_([^_]+)_(\d+)"),
            "INTERSECTION": re.compile(r"^(\d+)$"),
            "PARKINGLOT": re.compile(r"^PARKINGLOT_([^_]+)_(\d+)$"),
            "LIVINGAREA": re.compile(r"^LIVINGAREA_([^_]+)_(\d+)$"),
            "RECREATION": re.compile(r"^RECREATION_([^_]+)_(\d+)$"),
        }

        # Attempt to match each pattern

        nodeID : str
        nodeName : str
        nodeType : NodeType

        didMatch = False
        
        for key, pattern in patterns.items():

            match = pattern.match(nameFromGoogleEarth)


            if match:

                didMatch = True
                nodeType : NodeType = key

                if key == "INTERSECTION":
                    
                    nodeID =  match.group(1)
                    nodeName = "INTERSECTION"
                    


                elif key == "ROOM":

                    roomName = match.group(1)
                    buildingName = match.group(2)
                    nodeID = match.group(3)

                    return {

                        "nodeName" : f"{buildingName} {roomName}",
                        "roomName" : roomName,
                        "buildingName" : buildingName,
                        "nodeID" : nodeID,
                        "nodeType" : nodeType
                    }


                elif key == "BUILDING":

                    buildingName = match.group(1)
                    nodeName = buildingName
                    nodeID = match.group(2)

                    return {

                    "nodeName" : nodeName,
                    "buildingName" : buildingName,
                    "nodeID" : nodeID,
                    "nodeType" : nodeType
                }

                else:
                    # For other types, extract name and markerID
                    nodeName = match.group(1)
                    nodeID = match.group(2)
                

                break

        if didMatch:

            return {
                    "nodeName" : nodeName,
                    "nodeID" : nodeID,
                    "nodeType" : nodeType
                }
            
        return "No match found."

    def createNodesFromKml(self) -> list[Node]:

        ns = {'kml': 'http://www.opengis.net/kml/2.2'}

        tree = ET.parse(self.filePath)
        root = tree.getroot()



        nodes : list[Node] = []

        buildingNameToRooms : dict[str, list[str]] = dict()

        # Find all placemarks in the KML file
        for placemark in root.findall('.//kml:Placemark', ns):
            nameFromGoogleEarth = placemark.find('kml:name', ns)
            if nameFromGoogleEarth is not None:
                nameFromGoogleEarth = nameFromGoogleEarth.text
            else:
                nameFromGoogleEarth = "No Name"


            nodeInformation = self.parse_info_from_name(nameFromGoogleEarth)
            

            # For the marker name : 1

            # info is a dictionary that looks like this:
            
            # {
            #   nodeName : INTERSECTION 1,
            #   nodeType : 'INTERSECTION',
            #   nodeID : '1',
            # }




            



            # Create Node object

            if nodeInformation != 'No match found.':
                
                nodeName = nodeInformation["nodeName"]

                nodeID = nodeInformation["nodeID"]

                # Extracting the coordinates
                
                coordinates = placemark.find('.//kml:coordinates', ns)
                if coordinates is not None:
            
                    coord_text = coordinates.text.strip()

                    # Coordinates are provided as longitude,latitude,altitude
                    longitude, latitude, altitude = coord_text.split(',')

                    # print(f"Name: {name}, Coordinates: Latitude {latitude}, Longitude {longitude}")
                else:
                    print(f"Name: {nodeName} has no coordinates.")

                nodeLocation : list = [latitude,longitude, altitude]
                nodeType : NodeType

                if nodeInformation["nodeType"] in stringToEnum:

                    nodeType = stringToEnum[nodeInformation["nodeType"]]



                node : Node


                if nodeType == NodeType.BUILDING:

                    buildingName = nodeInformation["buildingName"]
                    node = BuildingNode(name=nodeName, nodeID=nodeID, location=nodeLocation, type=nodeType, buildingName=buildingName)

                elif nodeType == NodeType.ROOM:

                    roomName = nodeInformation["roomName"]
                    buildingName = nodeInformation["buildingName"]
                    
                    node = RoomNode(name=nodeName, nodeID=nodeID, location=nodeLocation, type=nodeType, roomName=roomName, buildingName=buildingName)

                    if buildingName not in buildingNameToRooms:
                        buildingNameToRooms[buildingName] = [nodeID]
                    else:
                        buildingNameToRooms[buildingName].append(nodeID)
                
                else:
                    node = Node(name=nodeName, nodeID=nodeID, location=nodeLocation, type=nodeType)

                nodes.append(node)



        # Go through building nodes and add the rooms
                
        for eachNode in nodes:

            if eachNode.type == NodeType.BUILDING:

                eachNode : BuildingNode = eachNode

                buildingName = eachNode.buildingName

                if buildingName in buildingNameToRooms:

                    for eachRoomNodeID in buildingNameToRooms[buildingName]:

                        eachNode.addRoom(eachRoomNodeID)
                
        return nodes