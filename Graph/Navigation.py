import copy
from geopy import distance
from Graph.Graph import Graph
from Graph.Node import NodeType, Node
from Graph.Edge import Edge

MPH_WALKING_SPEED = 3
MILE_TO_FEET = 5280
MINUTES_IN_HOUR = 60
FEET_PER_MINUTE = (MPH_WALKING_SPEED * MILE_TO_FEET) / MINUTES_IN_HOUR

ucr_graph : Graph = Graph("Graph/UCR_PathFinder_Coordinates.kml")
ucr_graph.createNodes()
ucr_graph.createEdges()



class Navigation:
            # [latitude , longitude , altitude]
    def __init__(self, location : list[float], destinationBuildingName : str) -> None:
        
        self.location : list[int] = location
        self.destinationBuildingName : str = destinationBuildingName
        self.closestNodeIdToUser : str
        self.sourceNodeID : str
        self.destinationNodeIDs : list[str]
        self.totalCost = dict[str : float]
        self.vertexPaths = dict[str: list[str]]
        self.finished = list[str]
        self.current = list[str]
        self.pathToDestination = list[str]
        self.navigationDictionary =  {

        }

    def setClosestNodeToUser(self):
        closestNodeID : str = None
        closestNodeDistance : float = float('inf')

        for nodeID, nodeObject in ucr_graph.nodeIdToObject.items():
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

        for nodeID, nodeObject in ucr_graph.nodeIdToObject.items():

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
                adjacents.append(edge.n2.nodeID)
            elif edge.n2.nodeID == id:
                adjacents.append(edge.n1.nodeID)
            else:
                print("Error in getting adjacent nodes in navigation class")

        return adjacents
    
    def getDistance(self, cur : str, adj : str):
        edges = ucr_graph.nodeIdToObject[cur].edges
        for edge in  edges:
            if adj == edge.n1.nodeID or adj == edge.n2.nodeID:
                return edge.length
        print("getEdgeDistance could not find the edge")
        return 1

    def findMinID(self):
        min = self.totalCost[self.current[0]]               #initialize min as cost of first node in current[]
        id = self.current[0]
        for eachVertexID in self.current:                    #loop through all id's in cureent to find the one with min distance
            if self.totalCost[eachVertexID] < min:
                min = self.totalCost[eachVertexID]
                id = eachVertexID
        return id
    
    def calculate(self, id : str): # dijkstra visit
        adjacents = self.getAdjacent(id)
        for each in adjacents:
            if each in self.finished:
                continue
            elif each in self.current:
                newDist = self.getDistance(id, each) + self.totalCost[id]
                if newDist < self.totalCost[each]: # if current node total cost plus edge to neighbor node is less than that neighbor nodes total cost
                    self.totalCost[each] = newDist # update distance of neighbor
                    self.vertexPaths[each] = self.vertexPaths[id]
                    self.vertexPaths[each].append(id) # update path of neighbor
            else:
                cost = self.totalCost[id] + self.getDistance(id, each)
                path = copy.copy(self.vertexPaths[id])
                path.append(each)

                self.current.append(each)
                self.totalCost[each] = cost
                self.vertexPaths[each] = path

        self.finished.append(id)
        self.current.remove(id)

    def findEdges(self, nodes : list[str]):
        result = []
        for i in range(len(nodes) - 1):
            cur = nodes[i]
            next = nodes[i + 1]
            edges = ucr_graph.nodeIdToObject[cur].edges
            for edge in edges:
                if edge.n1.nodeID == next or edge.n2.nodeID == next:
                    result.append(edge)
        return result
    """
        Returns a dictionary that looks like this:
        {
            'nodes' : Node [ ] 
            'edges' : Edge [ ]
        }
        List of nodes and edges of the path to get from the source node to the destination node. If there are multiple
        destinations, figure out which one is the fastest
    """
    
    def shortestPathAlgorithm(self, sourceNodeID : str, destinationNodeID : str): # path to destination is at the bottom of the function 
        found = 0 #false
        self.totalCost = {sourceNodeID : 0} # distance to reach a vertex, starting vertex is sourceNodeID
        self.vertexPaths = {sourceNodeID : [sourceNodeID]} #arrays that contain path of nodeID strings
        self.finished = [] # array of nodeID strings represented by vertices that are completed
        self.current = [sourceNodeID] # array of nodeID strings represented by vertices that are being processed
        
        #what happens if node is not found?
        while found == 0:                                   #loop till destination node is completed
            selected = self.findMinID()                     #find unfinished node with shortest distance
            if selected == destinationNodeID:
                found = 1
                continue
            self.calculate(selected)
            if not self.current:
                found = 1
                print("could not find path")
                return

        self.pathToDestination = self.vertexPaths[destinationNodeID] # destination path
        return self.totalCost[destinationNodeID], self.vertexPaths[destinationNodeID]
    
    def getShortestPathNodesAndEdges(self) -> dict[str , list]:

        

        sourceNodeID = self.sourceNodeID
        destinationNodeIDs = self.destinationNodeIDs
        minLength = float('inf')
        minTime = float('inf')
        minNodes = []
        minEdges = []

        for eachDestinationNodeID in destinationNodeIDs:
            length, nodes = self.shortestPathAlgorithm(sourceNodeID, eachDestinationNodeID) # edges

            if length < minLength:
                minLength = length
                minTime = minLength / FEET_PER_MINUTE
                minNodes = nodes
                minEdges = self.findEdges(minNodes)
                
        self.navigationDictionary['nodes'] = minNodes
        self.navigationDictionary['edges'] = minEdges
        self.navigationDictionary['totalLength'] = minLength
        self.navigationDictionary['totalTime'] = minTime
        


        nodesArray  = []
        edgesArray = []


   

        for eachNodeID in self.navigationDictionary['nodes']:
            

            nodeObject : Node = ucr_graph.nodeIdToObject[eachNodeID]

            nodeDictionary = {
                "name" : nodeObject.name,
                "location" : nodeObject.location
            }

            nodesArray.append(nodeDictionary)


        for eachEdge in self.navigationDictionary['edges']:

            eachEdge : Edge = eachEdge

            edgeDictionary = {
                "arrayOfCoordinates" : eachEdge.arrayOfCoordinates
            }

            edgesArray.append(edgeDictionary)

        
        self.navigationDictionary['nodes'] = nodesArray
        self.navigationDictionary['edges'] = edgesArray


        return self.navigationDictionary




    
    