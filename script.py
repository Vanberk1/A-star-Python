import math
from fibheap import *

print("Hello A*")
class Node:
    def __init__(self, id, cityId, g=None, h=None, parent=None):
        self.id = id
        self.cityId = cityId
        self.g = g
        self.h = h
        self.f = g + h
        self.parent = parent
        self.successors = []
        if parent != None:
            self.subtour = parent.subtour.copy()
            self.subtour.append(cityId)
        else:
            self.subtour = [cityId]

    def AddSuccessor(self, succ):
        self.successors.append(succ)

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


# REMOVE NEXT LINES TO USE THE ORIGINAL MATRIX
distanceMatrixAux = [[0, 2, 4, 5],
                     [2, 0, 5, 2],
                     [4, 5, 0, 3],
                     [5, 2, 3, 0]]
distanceMatrix = distanceMatrixAux
citiesCant = 4
cities = [1, 2, 3, 4]
# ///////////////////////////////////////////////

minimunEdges = []

for i in range(0, citiesCant):
    minimunEdges.append([largestDistance, largestDistance])
    for j in range(0, citiesCant):
        if i != j:
            if minimunEdges[i][0] >= distanceMatrix[i][j]:
                minimunEdges[i][1] = minimunEdges[i][0]
                minimunEdges[i][0] = distanceMatrix[i][j]
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

startNode = Node(nodesCount, 0, distanceMatrix[0][0], InOut(minimunEdges, citiesTSP, 0), None)
print("Start subtour:", startNode.subtour)
fheappush(openList, (startNode.f, 0, startNode))
times = 0

while openList.num_nodes:
    currentNode = fheappop(openList)[2]
    print(currentNode.successors)
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

    for cityId in notVisited:
        print("Current tour in for:", currentTour)
        if cityId != currentNode.id:
            print("City id:", cityId)
            nodesCount += 1
            newNode = Node(nodesCount, cityId, distanceMatrix[currentNode.cityId][cityId] + currentNode.g, InOut(minimunEdges, notVisited, cityId), currentNode)
            print("parent tour:", newNode.parent.subtour)
            print("actual id:", currentNode.id, "new id:", newNode.id, "f:", newNode.f)
            print("Subtour:", newNode.subtour)
            currentNode.AddSuccessor(newNode)
            fheappush(openList, (newNode.f, nodesCount, newNode))



    # if times >= 10:
    #     break

    # times += 1

     
print("Error")