import math
import time
import csv
import os

# Binary Heap modify to sort by f value of nodes
class BinaryHeap:
    def __init__(self):
        self.__heap = []
        self.__last_index = -1

    def push(self, value):
        self.__last_index += 1
        if self.__last_index < len(self.__heap):
            self.__heap[self.__last_index] = value
        else:
            self.__heap.append(value)
        self.__siftup(self.__last_index)

    def pop(self):
        if self.__last_index == -1:
            raise IndexError('pop from empty heap')

        min_value = self.__heap[0]

        self.__heap[0] = self.__heap[self.__last_index]
        self.__last_index -= 1
        self.__siftdown(0)

        return min_value

    def __siftup(self, index):
        while index > 0:
            parent_index, parent_value = self.__get_parent(index)

            if parent_value.f <= self.__heap[index].f:
                break

            self.__heap[parent_index], self.__heap[index] =\
                self.__heap[index], self.__heap[parent_index]

            index = parent_index

    def __siftdown(self, index):
        while True:
            index_value = self.__heap[index]

            left_child_index, left_child_value = self.__get_left_child(index, index_value)
            right_child_index, right_child_value = self.__get_right_child(index, index_value)

            if index_value.f <= left_child_value.f and index_value.f <= right_child_value.f:
                break

            if left_child_value.f < right_child_value.f:
                new_index = left_child_index
            else:
                new_index = right_child_index

            self.__heap[new_index], self.__heap[index] =\
                self.__heap[index], self.__heap[new_index]

            index = new_index

    def __get_parent(self, index):
        if index == 0:
            return None, None

        parent_index = (index - 1) // 2

        return parent_index, self.__heap[parent_index]

    def __get_left_child(self, index, default_value):
        left_child_index = 2 * index + 1

        if left_child_index > self.__last_index:
            return None, default_value

        return left_child_index, self.__heap[left_child_index]

    def __get_right_child(self, index, default_value):
        right_child_index = 2 * index + 2

        if right_child_index > self.__last_index:
            return None, default_value

        return right_child_index, self.__heap[right_child_index]

    def __len__(self):
        return self.__last_index + 1

class Node:
    def __init__(self, id, cityId, g=None, parent=None, minimunEdgesList=None, w=None):
        LARGE = 1000000
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
        self.f = (g + self.InOut(minimunEdgesList, w)) * LARGE - g

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


# The script read all files .tsp in the directory
cwd = os.getcwd()
print(cwd)
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(cwd):
    for file in f:
        if '.tsp' in file:
            files.append(file)

for file in files:
    instanceName = file
    f = open(instanceName, "r")

    content = f.readlines()

    citiesCoordinates = []
    cities = []
    citiesCant = int(content[0])
    for i in range(1, len(content)):
        line = content[i].split()
        cities.append((int(line[0], )))
        citiesCoordinates.append((float(line[1]), float(line[2])))

    # print(citiesCant, "\n")

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

    # print(minimunEdges)

    # for i in range(0, citiesCant):
    #     for j in range(0, citiesCant):
    #         print(distanceMatrix[i][j], " ", end = "")
    #     print("")


    citiesTSP = []
    for city in cities:
        citiesTSP.append(city - 1)

    openList = BinaryHeap()
    notVisited = citiesTSP[1:]
    w = 1.0
    if citiesCant >= 10 and citiesCant < 25:
        w = 1.2
    elif citiesCant >= 25 and citiesCant < 35:
        w = 1.4
    elif citiesCant >= 35:
        w = 2.0
    nodesCount = 1
    startNode = Node(nodesCount, 0, distanceMatrix[0][0], None, minimunEdges, w)
    # print("Start subtour:", startNode.subtour, "g:", startNode.g, "h:", startNode.h, "f:", startNode.f, "\n")
    # openList(openList, [startNode.f, 0, startNode])
    openList.push(startNode)

    initialTime = time.time()
    while len(openList):
        # element = heappop(openList)
        # currentNode = element[2]
        currentNode = openList.pop()
        currentTour = currentNode.subtour
        # print("Current tour:", currentTour)
        # if len(currentTour) == citiesCant and currentTour[0] == currentTour[len(currentTour) - 1]:
        #     print("Finished!")
        #     break

        notVisited = [city for city in citiesTSP if city not in currentTour]

        # print("Not visited:", notVisited)
        
        # print("City id:", currentNode.cityId, "Subtour:", currentNode.subtour, end=" ")
        # print("g: %.3f" % currentNode.g, end=" ")
        # print("h: %.3f" % currentNode.h, end=" ")
        # print("f: %.3f" % currentNode.f)
        # print("id:", element[1])
        if len(notVisited) > 0:
            for cityId in notVisited:
                if cityId != currentNode.id:
                    nodesCount += 1
                    newNode = Node(nodesCount, cityId, distanceMatrix[currentNode.cityId][cityId] + currentNode.g, currentNode, minimunEdges, w)
                    # print("City id:", cityId, "Subtour:", newNode.subtour, "g:", newNode.g, "h:", newNode.h, "f:", newNode.f)
                    currentNode.AddSuccessor(newNode)
                    openList.push(newNode)
        else:
            nodesCount += 1
            newNode = Node(nodesCount, 0, distanceMatrix[currentNode.cityId][0] + currentNode.g, currentNode, minimunEdges, w)
            expansions = newNode.id
            solutionTime = time.time() - initialTime
            totalCost = newNode.g
            # print(newNode.subtour)
            # print("G:", totalCost)
            # print("Nodes cant:", expansions)
            # print("Time: ", solutionTime)

            with open('francisco_esquibel_resultados.csv', 'a') as writeFile:
                writer = csv.writer(writeFile)
                writer.writerow([instanceName, totalCost, w, expansions, solutionTime])
            
            break
        
        # print("")

print("Finished!")