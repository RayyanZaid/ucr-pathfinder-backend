from Node import Node
from geopy import distance
from Node import AutomateNodeCreation


MPH_WALKING_SPEED = 2.5
MILE_TO_FEET = 5280
MINUTES_IN_HOUR = 60
FEET_PER_MINUTE = (MPH_WALKING_SPEED * MILE_TO_FEET) / MINUTES_IN_HOUR

class Edge:
    def __init__(self, n1 : Node, n2 : Node):
        self.n1 = n1
        self.n2 = n2
        self.length : int
        self.time : float

    def setDistance(self):
        coord1 = (self.n1.location[0], self.n1.location[1]) #needs to be in the format (lat,long)
        coord2 = (self.n2.location[0], self.n2.location[1])
        self.length = distance.distance(coord1, coord2, ellipsoid='WGS-84').feet

    def setTime(self):
        
        self.time = self.length / FEET_PER_MINUTE

    def printValues(self):
        print(f"Between {self.n1.name} and {self.n2.name}")
        print(f"Distance: {self.length} feet")
        print(f"Time: {self.time} minutes")
        print()


if __name__ == "__main__":

    nodeCreator = AutomateNodeCreation("./Experimenting/GoogleEarth/test.kml")

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