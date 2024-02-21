import xml.etree.ElementTree as ET
import re


from Graph.Node import Node, AutomateNodeCreation
from geopy import distance



MPH_WALKING_SPEED = 3
MILE_TO_FEET = 5280
MINUTES_IN_HOUR = 60
FEET_PER_MINUTE = (MPH_WALKING_SPEED * MILE_TO_FEET) / MINUTES_IN_HOUR

class Edge:
    def __init__(self, n1 : Node, n2 : Node, arrayOfCoordinates = []):
        self.n1 = n1
        self.n2 = n2

        self.n1NodeID = n1.nodeID
        self.n2NodeID = n2.nodeID

        self.length : int
        self.time : float
        
        self.arrayOfCoordinates = arrayOfCoordinates

    def setDistance(self):
        coord1 = (self.n1.location[0], self.n1.location[1]) #needs to be in the format (lat,long)
        coord2 = (self.n2.location[0], self.n2.location[1])
        self.length = distance.distance(coord1, coord2, ellipsoid='WGS-84').feet

    def setTime(self):
        
        self.time = self.length / FEET_PER_MINUTE

    def printValues(self):
        print(f"Between {self.n1.name} {self.n1.nodeID} and {self.n2.name} {self.n2.nodeID}")
        print(f"Distance: {self.length} feet")
        print(f"Time: {self.time} minutes")
        print()


class AutomateEdgeCreation:

    def __init__(self, googleEarthFilePath, nodeIDToNodeObject) -> None:
        
        self.filePath = googleEarthFilePath
        self.nodeIDToNodeObject = nodeIDToNodeObject


    def parse_info_from_name(self, nameFromGoogleEarth) -> str:

        # Check for EDGE case
        if nameFromGoogleEarth.startswith("EDGE"):


            edgePattern = re.compile(r"EDGE_(\d+)_(\d+)")

            match = edgePattern.match(nameFromGoogleEarth)


            if match:

                firstNumber = match.group(1)
                secondNumber = match.group(2)

                return {
                    "firstNumber" : firstNumber,
                    "secondNumber" : secondNumber
                }
            
            return  'No match found.'
        
        return  'No match found.'
            
    
    def createEdgesFromKml(self) -> list[Edge]:

        ns = {'kml': 'http://www.opengis.net/kml/2.2'}

        tree = ET.parse(self.filePath)
        root = tree.getroot()



        edges : list[Edge] = []

        # Find all placemarks in the KML file
        for placemark in root.findall('.//kml:Placemark', ns):
            nameFromGoogleEarth = placemark.find('kml:name', ns)
            if nameFromGoogleEarth is not None:
                nameFromGoogleEarth = nameFromGoogleEarth.text
            else:
                nameFromGoogleEarth = "No Name"


            edgeInformation = self.parse_info_from_name(nameFromGoogleEarth)
        
            



            # Create Node object

            if edgeInformation != 'No match found.':
                
                firstNumber = edgeInformation['firstNumber']

                secondNumber = edgeInformation['secondNumber']

                # Extracting the coordinates
                
                coordinates = placemark.find('.//kml:coordinates', ns)
                if coordinates is not None:
            
                    # print(coordinates)


                    coord_text = coordinates.text.strip()

                    arrayOfCoordinateStrings = coord_text.split(' ')


                    

                    arrayOfCoordinates : list[list[float]] = []


                    for eachString in arrayOfCoordinateStrings:

                        longitude, latitude, _ = eachString.split(',')

                        latitude = float(latitude)
                        longitude = float(longitude)

                        arrayOfCoordinates.append([latitude,longitude])






                    n1 : Node = self.nodeIDToNodeObject[firstNumber]
                    n2 : Node = self.nodeIDToNodeObject[secondNumber]

                    edge = Edge(n1,n2, arrayOfCoordinates)
                    edge.setDistance()
                    edge.setTime()
                    edges.append(edge)


        return edges
    

                


        



if __name__ == "__main__":

    nodeCreator = AutomateNodeCreation("./Experimenting/GoogleEarth/finishedSRC.kml")

    nodes : list[Node] = nodeCreator.createNodesFromKml()


    for i in range(len(nodes)):

        for j in range(i+1,len(nodes)):
            testEdge : Edge = Edge(nodes[i] , nodes[j])
            testEdge.setDistance()
            testEdge.setTime()
            testEdge.printValues()
    # for eachNode in nodes:

    #     print(f"Name: {eachNode.name}")
    #     print(f"Number: {eachNode.number}")
    #     print(f"Location: {eachNode.location}")
    #     print(f"Type: {eachNode.type}")
    #     print(f"Neighbors: {eachNode.neighbors}")