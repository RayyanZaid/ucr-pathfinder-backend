

from Graph.Node import Node, AutomateNodeCreation
from Graph.Edge import Edge, AutomateEdgeCreation


class Graph:

    def __init__(self, googleEarthFile : str) -> None:
        
        self.googleEarthFile : str = googleEarthFile

        # Dictionary of Node IDs to Node Object (allows us to access a Node with it's ID)
        self.nodeIdToObject : dict[str, Node] = dict()

        # Each node has a property called "edges" which is an array of its Edges. That's why there's no Edge variable in this class


    # Purpose : Create nodes and add them to the nodeIdToObject dictionary
        
    def createNodes(self) -> None:

        autoNodeCreation : AutomateNodeCreation = AutomateNodeCreation(self.googleEarthFile)

        nodes : list[Node] = autoNodeCreation.createNodesFromKml()


        # Adding Nodes to the graph: 
        # Save each node to the dictionary for quick access

        for eachNode in nodes:

            nodeID : str = eachNode.nodeID

            self.nodeIdToObject[nodeID] = eachNode
        
    def createEdges(self):

        automateEdgeCreation : AutomateEdgeCreation = AutomateEdgeCreation(self.googleEarthFile, self.nodeIdToObject)

        edges : list[Edge] = automateEdgeCreation.createEdgesFromKml()



        # Adding Edges to the graph: 

        # For each edge, we want to populate the Node's "edges" property

        # Ex. If an edge is connecting 2 and 3, we want to add the edge to Nodes 2 and 3.

        for eachEdge in edges:

            nodeId1 = eachEdge.n1NodeID
            nodeId2 = eachEdge.n2NodeID

            self.nodeIdToObject[nodeId1].addEdge(eachEdge)
            self.nodeIdToObject[nodeId2].addEdge(eachEdge)

    

# Testing
            

if __name__ == '__main__':

    ucr_graph : Graph = Graph("./Experimenting/GoogleEarth/finishedSRC.kml")

    ucr_graph.createNodes()

    ucr_graph.createEdges()

    print()

    