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
        self.subtour = []

    def MakeSuccessors(self, cities):
        self.successors = cities
        print(self.subTour)
        for city in self.subTour:
            print(city)
            self.successors.remove(city)

    def UpdateSubtour(self, newCity):
        self.subtour.append(newCity)
        

            


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
notVisited = citiesTSP[1:]
nodesCount = 0

startNode = Node(nodesCount, distanceMatrix[0][0], InOut(minimunEdges, citiesTSP, 0), None)
startNode.UpdateSubtour(citiesTSP[0])
fheappush(openList, (startNode.f, 0, startNode))
print(citiesTSP) 

while openList.num_nodes:
    currentNode = fheappop(openList)[2]
    # for x in currentNode.subTour:
    #     print(x)
    print(currentNode)
    currentTour = currentNode.subtour
    print(currentTour)
    if len(currentTour) == citiesCant + 1 and currentTour[0] == currentTour[len(currentTour) - 1]:
        print("Finished!")
        break

    notVisited = []
    for city in citiesTSP:
        if city not in currentTour:
            notVisited.append(city)

    print("Not visited:", notVisited)

    for cityId in citiesTSP:
        if cityId != currentNode.id:
            nodesCount += 1
            newNode = Node(nodesCount, distanceMatrix[currentNode.id][cityId] + currentNode.g, InOut(minimunEdges, notVisited, cityId), currentNode)
            print(currentNode.id, newNode.id, newNode.f)
            # print(newNode.successors)
            fheappush(openList, (newNode.f, nodesCount, newNode))


     
print("Error")