import sys


sys.path.append("")

from Graph.Node import Node, AutomateNodeCreation
from Graph.Edge import Edge

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