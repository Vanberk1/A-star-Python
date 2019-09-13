import math
from fibheap import *
from heapq import *

print("Hello A*")
class Node:
    def __init__(self, id=None, g=None, h=None, parent=None):
        self.id = id
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
        self.visited = False
    


def EuclideanDistance(node1, node2):
    return math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)

def InOut(minimunEdgesList, notVisitedList, currentNode):
    heuristic = 0
    for node in notVisitedList:
        heuristic += minimunEdgesList[node - 1][0] + minimunEdgesList[node - 1][1]
    heuristic += minimunEdgesList[0][0] + minimunEdgesList[currentNode - 1][0]

    return heuristic

f = open("test1.txt", "r")

content = f.readlines()

nodesCoordinates = []
notVisitedList = []
nodesCant = 0
for i in range(1, len(content)):
    line = content[i].split()
    notVisitedList.append(int(line[0]))
    nodesCoordinates.append((int(line[1]), int(line[2])))
    nodesCant += 1

print(nodesCant)

distanceMatrix = [[0 for x in range(nodesCant)] for y in range(nodesCant)]
largestDistance = 0

for i in range(0, nodesCant):
    for j in range(i + 1, nodesCant):
        if i != j:
            node1 = nodesCoordinates[i]
            node2 = nodesCoordinates[j]
            eucDis = EuclideanDistance(node1, node2)
            if largestDistance <= eucDis:
                largestDistance = eucDis
            distanceMatrix[i][j] = eucDis
            distanceMatrix[j][i] = eucDis

minimunEdges = []

for i in range(0, nodesCant):
    minimunEdges.append([largestDistance, largestDistance])
    for j in range(0, nodesCant):
        if i != j:
            if minimunEdges[i][0] >= distanceMatrix[i][j]:
                minimunEdges[i][1] = minimunEdges[i][0]
                minimunEdges[i][0] = distanceMatrix[i][j]

for i in range(0, nodesCant):
    for j in range(0, nodesCant):
        print(distanceMatrix[i][j], " ", end = "")
    print("")

print(notVisitedList)

nodeId = 0
openList = makefheap()
fheappush(openList, (distanceMatrix[0][0], Node(nodeId, distanceMatrix[0][0], InOut(minimunEdges, notVisitedList, 0), None)))

while openList.num_nodes:
    currentNode = fheappop(openList)[1]
    print(currentNode.f)
    

print(openList.num_nodes)