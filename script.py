import math

print("Hello A*")
class Node:
    def __init__(self, id, x, y):
        self.id = id
        self.g = 0
        self.h = 0
        self.f = 0
        self.x = x
        self.y = y
        self.parent = 0
        self.visited = False


def EuclideanDistance(node1, node2):
    return math.sqrt((node2.x - node1.x)**2 + (node2.y - node1.y)**2)

f = open("test.txt", "r")

content = f.readlines()

nodes = []
nodesCant = 0
for i in range(1, len(content)):
    line = content[i].split()
    nodes.append(Node(int(line[0]), int(line[1]), int(line[2])))
    nodesCant += 1

print(nodesCant)


distanceMatrix = [[0 for x in range(nodesCant)] for y in range(nodesCant)]
largestDistance = 0

for i in range(0, nodesCant):
    for j in range(i + 1, nodesCant):
        if i != j:
            node1 = nodes[i]
            node2 = nodes[j]
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

for i in range(0, len(minimunEdges)):
    print(i, minimunEdges[i][0], minimunEdges[i][1])