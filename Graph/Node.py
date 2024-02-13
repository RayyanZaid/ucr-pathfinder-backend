from enum import Enum
import xml.etree.ElementTree as ET
import re
class NodeType(Enum):

    BUILDING = 1
    INTERSECTION = 2
    PARKING_LOT = 3

stringToEnum = {
    "BUILDING" : NodeType.BUILDING,
    "INTERSECTION" : NodeType.INTERSECTION,
    "PARKING_LOT" : NodeType.PARKING_LOT
}


class Node:

    def __init__(self, name : str, number: str, location : list, type : NodeType, neighbors : list) -> None:
        
        self.name = name

        self.number = number
                            # latitude, longitude, altitude
        self.location : list = location

        self.type : NodeType = type

        self.neighbors : list = neighbors


class AutomateNodeCreation:

    def __init__(self, googleEarthFilePath) -> None:
        
        self.filePath = googleEarthFilePath

    

    def createNodesFromKml(self) -> list[Node]:

        ns = {'kml': 'http://www.opengis.net/kml/2.2'}

        tree = ET.parse(self.filePath)
        root = tree.getroot()



        nodes : list[Node] = []

        # Find all placemarks in the KML file
        for placemark in root.findall('.//kml:Placemark', ns):
            name = placemark.find('kml:name', ns)
            if name is not None:
                name = name.text
            else:
                name = "No Name"




            nodeInformation = self.parseInfoFromName(name)
            

            # For the marker name : SRCTopLeft_INTERSECTION_1_2_3,

            # info is a dictionary that looks like this:
            
            # {
            #   nodeName : 'SRCTopLeft',
            #   nodeType : 'INTERSECTION',
            #   nodeNumber : '1',
            #   neighborNumbers : ['2','3']
            # }




            # Extracting the coordinates
            coordinates = placemark.find('.//kml:coordinates', ns)
            if coordinates is not None:
        
                coord_text = coordinates.text.strip()

                # Coordinates are provided as longitude,latitude,altitude
                longitude, latitude, altitude = coord_text.split(',')

                # print(f"Name: {name}, Coordinates: Latitude {latitude}, Longitude {longitude}")
            else:
                print(f"Name: {name} has no coordinates.")


            # Create Node object

            nodeName = nodeInformation["nodeName"]

            nodeNumber = nodeInformation["nodeNumber"]
            nodeLocation : list = [latitude,longitude, altitude]
            nodeType : NodeType

            if nodeInformation["nodeType"] in stringToEnum:

                nodeType = stringToEnum[nodeInformation["nodeType"]]

            nodeNeighbors = nodeInformation["neighborNumbers"]


            node = Node(name=nodeName, number=nodeNumber, location=nodeLocation, type=nodeType, neighbors=nodeNeighbors)

            nodes.append(node)


        return nodes


    def parseInfoFromName(self,fullName) -> dict:
        # Compile regex to match the pattern, including capturing the neighbors as a separate group

        # RegEx = {NODE NAME}_{NODE TYPE}_{NUMBER}(_{NEIGHBOR NUMBER})*

        pattern = re.compile(r"^(.*?)_(.*?)_(\d+)((?:_\d+)*)$")
        match = pattern.match(fullName)
        
        if match:
            nodeName, nodeType, nodeNumber, neighbors_str = match.groups()
            # Extract neighbor numbers from the neighbors_str, if any
            neighborNumbers = neighbors_str[1:].split('_') if neighbors_str else []
            return {
                "nodeName": nodeName,
                "nodeType": nodeType,
                "nodeNumber": nodeNumber,
                "neighborNumbers": neighborNumbers
            }
        else:
            return "No match found."

    

if __name__ == '__main__':
    nodeCreator = AutomateNodeCreation("Experimenting\\GoogleEarth\\test.kml")

    nodes : list[Node] = nodeCreator.createNodesFromKml()

    for eachNode in nodes:

        print(f"Name: {eachNode.name}")
        print(f"Number: {eachNode.number}")
        print(f"Location: {eachNode.location}")
        print(f"Type: {eachNode.type}")
        print(f"Neighbors: {eachNode.neighbors}")
