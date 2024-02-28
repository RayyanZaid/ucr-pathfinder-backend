import sys


sys.path.append("")


from Graph.Navigation import Navigation


# Testing



# Test 1

# userLocation = [33.975931, -117.329059, 0.0] 
# destinationBuildingName = "Materials Sci and Engineering"
# navigationObject : Navigation = Navigation(userLocation, destinationBuildingName)

# navigationObject.setClosestNodeToUser() # should be 10

# print(navigationObject.sourceNodeID == '10')

# navigationObject.setBuildingNodes()
# print(navigationObject.destinationNodeIDs == ['9', '12'])

# navigationDictionary = navigationObject.getShortestPathNodesAndEdges()




# Test 2

# userLocation = [33.975948, -117.327881, 0.0]
# navigationObject : Navigation = Navigation(userLocation , destinationBuildingName)
# destinationBuildingName = "Materials Sci and Engineering"
# navigationObject.setClosestNodeToUser() # Should be 11
# print(navigationObject.sourceNodeID == '11')


# navigationObject.setBuildingNodes()
# print(navigationObject.destinationNodeIDs == ['9', '12'])

# navigationDictionary = navigationObject.getShortestPathNodesAndEdges()



# # Test 3
# # Testing Shortest Path (some bugs)

# userLocation22 = [33.97551741560539, -117.3280488150658, 318.0153092198389]
# destinationBuildingName = "Materials Sci and Engineering"
# navigationObject : Navigation = Navigation(userLocation22 , destinationBuildingName)
# navigationObject.setClosestNodeToUser() # Should be 22
# print(navigationObject.sourceNodeID == '22')


# navigationObject.setBuildingNodes()
# print(navigationObject.destinationNodeIDs == ['9', '12'])


# navigationDictionary = navigationObject.getShortestPathNodesAndEdges()
# print()


# # Test 4

# # Shortest Path (some bugs)

# userLocationNode30 = [33.97571667778362, -117.3286881329295,317.4348304680136] 
# destinationBuildingName = "Materials Sci and Engineering"
# navigationObject : Navigation = Navigation(userLocationNode30 , destinationBuildingName)
# navigationObject.setClosestNodeToUser() # Should be 30, but it's going to 29 because they're the exact same coordinates
# print(navigationObject.sourceNodeID == '30')


# navigationObject.setBuildingNodes()
# print(navigationObject.destinationNodeIDs == ['9', '12'])


# navigationDictionary = navigationObject.getShortestPathNodesAndEdges()


# Test 5

# For some reason, this is going from 19 --> 23 --> 16,

userLocation37 = [33.97488141666391, -117.3286340179911,318.9579109074609]
destinationBuildingName = "Materials Sci and Engineering"
navigationObject : Navigation = Navigation(userLocation37 , destinationBuildingName)
navigationObject.setClosestNodeToUser() 
navigationObject.setBuildingNodes()
navigationDictionary = navigationObject.getShortestPathNodesAndEdges()



print()