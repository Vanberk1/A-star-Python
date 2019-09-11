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

f = open("test.txt", "r")

content = f.readlines()

print(content[0])
print(content[1])

nodes = []
for i in range(1, len(content)):
    line = content[i].split()
    nodes.append(Node(line[0], line[1], line[2]))

for node in nodes:
    print(node.id)
