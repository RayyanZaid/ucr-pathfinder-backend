import sys


sys.path.append("")

from Graph.Node import Node, AutomateNodeCreation

if __name__ == '__main__':
    nodeCreator = AutomateNodeCreation("./Experimenting/GoogleEarth/finishedSRC.kml")

    nodes : list[Node] = nodeCreator.createNodesFromKml()

    for eachNode in nodes:

        print(f"Name: {eachNode.name}")
        print(f"nodeID: {eachNode.nodeID}")
        print(f"Location: {eachNode.location}")
        print(f"Type: {eachNode.type}")
