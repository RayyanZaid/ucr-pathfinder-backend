from enum import Enum
import xml.etree.ElementTree as ET
import re



class NodeType(Enum):

    BUILDING = 1
    INTERSECTION = 2
    PARKING_LOT = 3
    LIVINGAREA = 4
    RECREATION = 5

stringToEnum = {
    "BUILDING" : NodeType.BUILDING,
    "INTERSECTION" : NodeType.INTERSECTION,
    "PARKING_LOT" : NodeType.PARKING_LOT,
    "LIVIINGAREA" : NodeType.LIVINGAREA,
    "RECREATION" : NodeType.RECREATION,
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



                node = Node(name=nodeName, nodeID=nodeID, location=nodeLocation, type=nodeType)

                nodes.append(node)


        return nodes


    

    

if __name__ == '__main__':
    nodeCreator = AutomateNodeCreation("./Experimenting/GoogleEarth/finishedSRC.kml")

    nodes : list[Node] = nodeCreator.createNodesFromKml()

    for eachNode in nodes:

        print(f"Name: {eachNode.name}")
        print(f"nodeID: {eachNode.nodeID}")
        print(f"Location: {eachNode.location}")
        print(f"Type: {eachNode.type}")
