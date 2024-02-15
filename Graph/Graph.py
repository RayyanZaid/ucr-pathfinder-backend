from Node import Node, AutomateNodeCreation
from Edge import Edge


class Graph:

    def __init__(self, googleEarthFile : str) -> None:
        
        self.googleEarthFile : str = googleEarthFile



        # Dictionary of Node IDs to Node Object (allows us to access a Node with it's ID)
        self.nodeIdToObject : dict[str, Node] = dict()


        # Node to Edge Mapping. Ex. (2,1) : Edge() -- The edge that connects nodes 2 and 1
        self.nodesToEdge : dict[list , Edge] = dict()
    

    # Purpose : Create nodes and add them to the nodeIdToObject dictionary
        
    def createNodes(self) -> None:

        autoNodeCreation : AutomateNodeCreation = AutomateNodeCreation(self.googleEarthFile)

        nodes : list[Node] = autoNodeCreation.createNodesFromKml()

        for eachNode in nodes:

            nodeID : str = eachNode.number

            self.nodeIdToObject[nodeID] = eachNode
        
    def createEdges(self):

        # Go through each node and get each neighbor's number and Node object
        # For each (nodeNumber, neighborNodeNumber) create an Edge using the Node objects

        for nodeNumber , nodeObject in self.nodeIdToObject.items():

            neighborNumberList = nodeObject.neighbors

            for neighborNumber in neighborNumberList:
                
                nodeKey = self.getEdgeFromNodeNumbers(nodeNumber, neighborNumber)
                
                nodeObject = self.nodeIdToObject[nodeNumber]
                neighborNodeObject = self.nodeIdToObject[neighborNumber]

                self.nodesToEdge[nodeKey] = Edge(nodeObject,neighborNodeObject)


    # This function takes in 2 node numbers (strings), turns them into integers, sorts them, turns back to string
    def getEdgeFromNodeNumbers(node1Number : str, node2Number : str):

        node1NumberInt = int(node1Number)
        node2NumberInt = int(node2Number)

        nodeKey = []

        if node1NumberInt < node2NumberInt:

            nodeKey = [node1Number, node2Number]

        else:
            nodeKey = [node2Number, node1Number]

        return nodeKey

# Testing
            

if __name__ == '__main__':

    ucr_graph : Graph = Graph("./Experimenting/GoogleEarth/test.kml")

    ucr_graph.createNodes()

    ucr_graph.createEdges()

    print()

    