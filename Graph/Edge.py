from Node import Node

class Edge:
    def __init__(self, n1 : Node, n2 : Node, ):
        self.n1 = n1
        self.n2 = n2

#we want to use a geodetic/ellipsiod formula because the coordinates we get from google are based on WGS84, the world geodetic system
#i dont want to reinvent the wheel on geodetic caluculations so i will be using geopy

#if __name__ == '__main__':