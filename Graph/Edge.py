import geopy
from Node import Node
from geopy import distance

class Edge:
    def __init__(self, n1 : Node, n2 : Node):
        self.n1 = n1
        self.n2 = n2

    def setDistance(self):
        coord1 = (self.n1.location[0], self.n1.location[1]) #needs to be in the format (lat,long)
        coord2 = (self.n2.location[0], self.n2.location[1])
        self.length = distance.distance(coord1, coord2, ellipsoid='WGS-84').feet

    def setTime(self, time : float):
        self.time = geopy.units.miles(feet=self.length) * 2.5

    def printValues(self):
        print(self.length + ' ' + self.time)