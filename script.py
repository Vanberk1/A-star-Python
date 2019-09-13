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

    def MakeSuccessors(self, citiesCant, distanceMatrix):
        self.successors = []
        for i in range(self.id + 1, citiesCant):
            break


def EuclideanDistance(node1, node2):
    return math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)

def InOut(minimunEdgesList, notVisitedList, currentNode):
    heuristic = 0
    for node in notVisitedList:
        heuristic += minimunEdgesList[node - 1][0] + minimunEdgesList[node - 1][1]
    heuristic += minimunEdgesList[0][0] + minimunEdgesList[currentNode - 1][0]

    return heuristic  

f = open("inst1.tsp", "r")

content = f.readlines()

citiesCoordinates = []
cities = []
citiesCant = 0
for i in range(1, len(content)):
    line = content[i].split()
    cities.append((int(line[0], )))
    citiesCoordinates.append((int(line[1]), int(line[2])))
    citiesCant += 1

print(citiesCant)

distanceMatrix = [[0 for x in range(citiesCant)] for y in range(citiesCant)]
largestDistance = 0

for i in range(0, citiesCant):
    for j in range(i + 1, citiesCant):
        if i != j:
            node1 = citiesCoordinates[i]
            node2 = citiesCoordinates[j]
            eucDis = EuclideanDistance(node1, node2)
            if largestDistance <= eucDis:
                largestDistance = eucDis
            distanceMatrix[i][j] = eucDis
            distanceMatrix[j][i] = eucDis

minimunEdges = []

for i in range(0, citiesCant):
    minimunEdges.append([largestDistance, largestDistance])
    for j in range(0, citiesCant):
        if i != j:
            if minimunEdges[i][0] >= distanceMatrix[i][j]:
                minimunEdges[i][1] = minimunEdges[i][0]
                minimunEdges[i][0] = distanceMatrix[i][j]

for i in range(0, citiesCant):
    for j in range(0, citiesCant):
        print(distanceMatrix[i][j], " ", end = "")
    print("")

print(cities)

citiesTSP = cities
openList = makefheap()
startNode = Node(cities[0] - 1, distanceMatrix[0][0], InOut(minimunEdges, cities, 0), None)
fheappush(openList, (startNode.f, startNode))
currentTour = [citiesTSP[0] - 1]
print(currentTour[0])
print(currentTour[len(currentTour) - 1])

while openList.num_nodes:
    currentNode = fheappop(openList)[1]
    print(currentNode.f)
    if len(citiesTSP) != 0 and citiesTSP[0] == citiesTSP[len(citiesTSP) - 1]:
        break
     
