import math
from fibheap import *

class Node:
    def __init__(self, id, cityId, g=None, parent=None, minimunEdgesList=None, w=None):
        self.id = id
        self.cityId = cityId
        self.g = g
        self.parent = parent
        self.successors = []
        if parent != None:
            self.subtour = parent.subtour.copy()
            self.subtour.append(cityId)
        else:
            self.subtour = [cityId]
        self.f = g + self.InOut(minimunEdgesList, w)

    def AddSuccessor(self, succ):
        # print("New succ:", succ)
        self.successors.append(succ)
        # print("Succs:", self.successors)

    def InOut(self, minimunEdgesList, w):
        self.h = 0
        for city in range(0, len(minimunEdges)):
            if city not in self.subtour:
                self.h += minimunEdges[city][0] + minimunEdges[city][1]
        self.h += minimunEdges[0][0] + minimunEdges[self.cityId][0]
        self.h = self.h / 2
        
        wh = self.h * w
        return wh


def EuclideanDistance(node1, node2):
    return math.sqrt((node2[0] - node1[0])**2 + (node2[1] - node1[1])**2)


f = open("inst3.tsp", "r")

content = f.readlines()

citiesCoordinates = []
cities = []
citiesCant = 0
for i in range(1, len(content)):
    line = content[i].split()
    cities.append((int(line[0], )))
    citiesCoordinates.append((int(line[1]), int(line[2])))
    citiesCant += 1

print(citiesCant, "\n")

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


# REMOVE NEXT LINES TO USE THE ORIGINAL MATRIX
# ///////////////////////////////////////////////
# distanceMatrixAux = [[0, 2, 4, 5],
#                      [2, 0, 4, 2],
#                      [4, 4, 0, 3],
#                      [5, 2, 3, 0]]
# distanceMatrix = distanceMatrixAux
# citiesCant = 4
# cities = [1, 2, 3, 4]
# largestDistance = 4
# w = 1.0
# ///////////////////////////////////////////////

minimunEdges = []

for i in range(0, citiesCant):
    auxDistance = distanceMatrix[i].copy()
    auxDistance.sort()
    minimunEdges.append(auxDistance[1:3])

print(minimunEdges)

for i in range(0, citiesCant):
    for j in range(0, citiesCant):
        print(distanceMatrix[i][j], " ", end = "")
    print("")


citiesTSP = []
for city in cities:
    citiesTSP.append(city - 1)

openList = makefheap()
notVisited = citiesTSP[1:]
nodesCount = 0
w = 1.0
if citiesCant >= 10 and citiesCant < 25:
    w = 1.4
elif citiesCant >= 25 and citiesCant < 35:
    w = 1.7
elif citiesCant >= 35:
    w = 2


startNode = Node(nodesCount, 0, distanceMatrix[0][0], None, minimunEdges, w)
print("Start subtour:", startNode.subtour, "g:", startNode.g, "h:", startNode.h, "f:", startNode.f, "\n")
fheappush(openList, (startNode.f, 0, startNode))

while openList.num_nodes:
    currentNode = fheappop(openList)[2]
    currentTour = currentNode.subtour
    print("Current tour:", currentTour)
    if len(currentTour) == citiesCant + 1 and currentTour[0] == currentTour[len(currentTour) - 1]:
        print("Finished!")
        break

    notVisited = []
    for city in citiesTSP:
        if city not in currentTour:
            notVisited.append(city)

    print("Not visited:", notVisited)
    
    if len(notVisited) > 0:
        for cityId in notVisited:
            if cityId != currentNode.id:
                lastCity = currentNode.cityId
                nodesCount += 1
                newNode = Node(nodesCount, cityId, distanceMatrix[lastCity][cityId] + currentNode.g, currentNode, minimunEdges, w)
                print("City id:", cityId, "Subtour:", newNode.subtour, "g:", newNode.g, "h:", newNode.h, "f:", newNode.f)
                currentNode.AddSuccessor(newNode)
                fheappush(openList, (newNode.f, nodesCount, newNode))
    else:
        lastCity = currentNode.cityId
        newNode = Node(nodesCount, 0, distanceMatrix[lastCity][0] + currentNode.g, currentNode, minimunEdges, w)
        print("Finished!")
        print(newNode.subtour)
        print("G:", newNode.g)
        break
    
    print("")
     
print("\nError")