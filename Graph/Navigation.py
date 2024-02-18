
from geopy import distance
from Graph import Graph

from Node import NodeType


ucr_graph : Graph = Graph("./Experimenting/GoogleEarth/finishedSRC.kml")
ucr_graph.createNodes()
ucr_graph.createEdges()


class Navigation:



            # [latitude , longitude , altitude]
    def __init__(self, location : list[float], destinationBuildingName : str) -> None:
        
        self.location : list[int] = location
        self.destinationBuildingName : str = destinationBuildingName

        self.nodeIdToObject = ucr_graph.nodeIdToObject
        self.closestNodeIdToUser : str


        self.sourceNodeID : str

        self.destinationNodeIDs : list[str]


    def setClosestNodeToUser(self):

        closestNodeID : str = None
        closestNodeDistance : float = float('inf')

        for nodeID, nodeObject in self.nodeIdToObject.items():


            coord1 = (self.location[0], self.location[1]) #needs to be in the format (lat,long)
            coord2 = (nodeObject.location[0], nodeObject.location[1])
            euclidDistance = distance.distance(coord1, coord2, ellipsoid='WGS-84').feet

            if euclidDistance < closestNodeDistance:

                closestNodeID = nodeID
                closestNodeDistance = euclidDistance
        

        self.sourceNodeID = closestNodeID
            

            




    # Returns a list of node ids representing entrances of building
                
    def setBuildingNodes(self) -> list[str]:
        
        buildingNodeIDs : list[str] = []


        for nodeID, nodeObject in self.nodeIdToObject.items():

            if nodeObject.type == NodeType.BUILDING:

                nodeBuildingName = nodeObject.name

                if nodeBuildingName == self.destinationBuildingName:

                    buildingNodeIDs.append(nodeID)


        self.destinationNodeIDs = buildingNodeIDs

    
    def similarityScoring(self):

        # might implement later

        return self.destinationBuildingName
    
    def getAdjacent(self, id : str): #return id of adjacent nodes
        adjacents = []

        for edge in ucr_graph.nodeIdToObject[id].edges:
            if edge.n1.nodeID == id:
                adjacents.append(edge.n1.nodeID)
            elif edge.n2.nodeID == id:
                adjacents.append(edge.n2.nodeID)
            else:
                print("Error in getting adjacent nodes in navigation class")

        return adjacents
    
    """
        Returns a dictionary that looks like this:
        {
            'nodes' : Node [ ] 
            'edges' : Edge [ ]
        }
        List of nodes and edges of the path to get from the source node to the destination node. If there are multiple
        destinations, figure out which one is the fastest
    """
    def shortestPathAlgorithm(self, sourceNodeID : str, destinationNodeID : str):
        # found = 0 #false
        # self.vertexCost = {sourceNodeID : 0} # distance or time to reach a vertex, starting vertex is sourceNodeID
        # self.vertexPath = {sourceNodeID : [sourceNodeID]} #arrays that contain path mappped to each vertex
        # finished = [] # array of vertices that are completed
        # current = [sourceNodeID] # array of vertices that are being processed
        
        # while found == 0:                                   #loop till destination node is completed
        #     min = self.vertexCost[current[0]]               #initialize min as cost of first node in current[]
        #     for eachVertexID in current:                    #loop through all id's in cureent to find the one with min distance
        #         if self.vertexCost[eachVertexID]:
        #             min = self.vertexCost[eachVertexID]

        return int(sourceNodeID) - int(destinationNodeID)
    



    def getShortestPathNodesAndEdges(self) -> dict[str , list]:

        pathDictionary = {

            "node" : [],
            "edge" : [],

        }

        sourceNodeID = self.sourceNodeID

        destinationNodeIDs = self.destinationNodeIDs


        minLength = float('inf')
        for eachDestinationNodeID in destinationNodeIDs:

            length = self.shortestPathAlgorithm(sourceNodeID, eachDestinationNodeID)

            if length < minLength:
                minLength = length


        return pathDictionary


if __name__ == "__main__":

    # Testing
    
    userLocation = [33.975931, -117.329059, 0.0] 
    destinationBuildingName = "Materials Sci and Engineering"
    navigationObject : Navigation = Navigation(userLocation, destinationBuildingName)

    navigationObject.setClosestNodeToUser() # should be 10

    print(navigationObject.sourceNodeID == '10')

    

    userLocation = [33.975948, -117.327881, 0.0]
    navigationObject : Navigation = Navigation(userLocation , destinationBuildingName)
    navigationObject.setClosestNodeToUser() # Should be 11
    print(navigationObject.sourceNodeID == '11')


    navigationObject.setBuildingNodes()
    print(navigationObject.destinationNodeIDs == ['9', '12'])
    
    