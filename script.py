import math
from fibheap import *

print("Hello A*")
class Node:
    def __init__(self, id=None, g=None, h=None, parent=None):
        self.id = id
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
        self.visited = False
        self.subTour = []
        currentNode = self
        while currentNode != None:
            self.subTour.append(id)
            currentNode = currentNode.parent

    def MakeSuccessors(self, citiesCant, distanceMatrix):
        self.successors = []
        for i in range(self.id + 1, citiesCant):
            break


def EuclideanDistance(node1, node2):
    return math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)

def InOut(minimunEdgesList, notVisitedList, currentNode):
    heuristic = 0
    for node in notVisitedList:
        heuristic += minimunEdgesList[node][0] + minimunEdgesList[node][1]
    heuristic += minimunEdgesList[0][0] + minimunEdgesList[currentNode][0]

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

# for i in range(0, citiesCant):
#     for j in range(0, citiesCant):
#         print(distanceMatrix[i][j], " ", end = "")
#     print("")


citiesTSP = []
for city in cities:
    citiesTSP.append(city - 1)

openList = makefheap()
notVisited = citiesTSP

startNode = Node(citiesTSP[0], distanceMatrix[0][0], InOut(minimunEdges, citiesTSP, 0), None)
fheappush(openList, (startNode.f, startNode))
print(citiesTSP)
notVisited.remove(0)
print(notVisited)

while openList.num_nodes:
    currentNode = fheappop(openList)[1]
    # for x in currentNode.subTour:
    #     print(x)
    currentTour = currentNode.subTour
    print(currentTour)
    if len(currentTour) == citiesCant + 1 and currentTour[0] == currentTour[len(currentTour) - 1]:
        print("Finished!")
        break

    notVisited = []
    for city in citiesTSP:
        if city not in currentTour:
            notVisited.append(city)

    for x in range(currentNode.id + 1, citiesCant):
        print(currentNode.id, x)
        newNode = Node(x, distanceMatrix[currentNode.id][x], InOut(minimunEdges, notVisited, x), currentNode)
        print(newNode.f)
        #fheappush(openList, (newNode.f, newNode))

    break
     
print("Error")