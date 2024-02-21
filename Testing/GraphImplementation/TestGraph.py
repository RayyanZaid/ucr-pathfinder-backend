import sys


sys.path.append("")

from Graph.Graph import Graph

# Testing
            

if __name__ == '__main__':

    ucr_graph : Graph = Graph("./Experimenting/GoogleEarth/finishedSRC.kml")

    ucr_graph.createNodes()

    ucr_graph.createEdges()

    print()