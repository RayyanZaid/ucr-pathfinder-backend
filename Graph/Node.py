from enum import Enum

class NodeType:

    BUILDING = 1
    INTERSECTION = 2
    PARKING_LOT = 3


class Node:

    def __init__(self) -> None:
        
        self.name = ""
                            # latitude, longitude
        self.location : list = []

        self.type : NodeType

        self.neighbors : list = []






