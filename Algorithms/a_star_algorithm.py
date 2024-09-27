''' Created by @Fatema110
A* Algorithm 
It is a path finding algorithm which find the shortest path between start node and the end node.

Problem Statement
You will be given 2 Dimensional array containing 0s and 1s where each 0 represents free space and each 1 represents an obstacle. Consider this array as a grid-shaped graph. you're given 4 integers StartRow, StartCol, endRow, and endCol, representing the position of a start node and an end node in the graph.

Write a function that finds the shortest path between the start node and the end node using the A* search algorithm and returns it.

The shortest path should be returned as an array of node positions, where each node is an array of two elements the [row, col] of the respective node in the graph. The output should contain the start node's position, the end node's position should be ordered from the start node to the end node.
if there is no path from the start node to the end node, your function should return an empty array.

Note 
From each node the graph, you can travel in four diretions: up, down , left, right.
The distance between all the neighbouring nodes in the graph is the same; you can treat it as a distance of 1.
The start node and the end node are guaranteed to be located in the empty spaces.
The start node and the end node will never be out of bound.
There will be atmost one shortest path from the start node and the end node.
  Time Complexity: O(w*h* log(w*h))
  Space Complexity:O(w*h) where h is height and w is width of graph
'''
class Node: # information about each of the position in graph
	def __init__(self, row, col, value):
		self.id = str(row) + '-' + str(col)
		self.row = row
		self.col = col
		self.value = value
		self.distanceFromStart = float('inf') 
		self.estimatedDistanceToEnd = float('inf') 
		self.cameFrom = None
		
		
def aStarAlgorithm( startRow, startCol, endRow, endCol, graph):
    nodes =initializeNodes(graph)
    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.distanceFromStart = 0
    startNode.estimatedDistanceToEnd = calculateManhattanDistance(startNode, endNode)
    nodesToVisit = MinHeap([startNode])
    while not nodesToVisit.isEmpty():
        currentMinDistanceNode = nodesToVisit.remove() 

        if currentMinDistanceNode == endNode:
            break
        # all the neighbor of current node and update their node accordingly
        neighbors = getNeighboringNodes(currentMinDistanceNode, nodes)
        for neighbor in neighbors:
            #  check obstacles
            if neighbor.value == 1: 
                continue
            #distance that we get when we travel from current node(tentativeDistanceToNeighbor)
            tentativeDistanceToNeighbor = currentMinDistanceNode.distanceFromStart +1
            #  if neighbor has shorter or same distance then continue
            if tentativeDistanceToNeighbor >= neighbor.distanceFromStart:
                continue
            # the tentativeDistanceToNeighbor is less than the distanceFromStart update all values 
            neighbor.cameFrom = currentMinDistanceNode
            neighbor.distanceFromStart = tentativeDistanceToNeighbor
            neighbor.estimatedDistanceToEnd = tentativeDistanceToNeighbor + calculateManhattanDistance( neighbor, endNode)
            # if nodes not visited the  insert and  update if present    
            if not nodesToVisit.containsNode(neighbor):
                nodesToVisit.insert(neighbor)
            else:
                nodesToVisit.update(neighbor)
    return reconstructPath(endNode)


def initializeNodes(graph):  # stores node object all of the 1s and 0s in graph
    nodes =[]
    for i, row in enumerate(graph):
        nodes.append([])
        for j, value in enumerate(row):
            nodes[i].append(Node(i,j,value))
    return nodes
def calculateManhattanDistance(currentNode, endNode):
    currentRow = currentNode.row
    currentCol = currentNode.col
    endRow = endNode.row
    endCol = endNode.col
    return abs(currentRow - endRow) + abs(currentCol - endCol) 
def getNeighboringNodes(node, nodes):
    neighbors=[]
    numRows = len(nodes)
    numCols = len(nodes[0])
    row = node.row
    col = node.col
    if row < numRows - 1 : # DOWN
        neighbors.append(nodes[row + 1] [col])
    if row > 0: #UP
        neighbors.append(nodes[row -1][col])
    if col< numCols - 1 : #RIGHT
        neighbors.append(nodes[row] [col + 1])
    if col > 0: #LEFT
        neighbors.append(nodes[row][col - 1]) 
    return neighbors
# reconstruct the path if one exists to get to it
def reconstructPath(endNode):
    if  not endNode.cameFrom:
        return []
    currentNode = endNode
    path = []
    while currentNode is not None :
        path.append([currentNode.row, currentNode.col])
        currentNode = currentNode.cameFrom
    return path[::-1] # reverse path so it goes from start to end
class MinHeap:
    def __init__(self, array):
        # Hold the position in the heap that each node is at
        self.nodePositionInHeap ={ node.id : idx for idx, node in enumerate(array)}
        self.heap = self.buildHeap(array)
    def isEmpty(self):
        return len(self.heap)==0
    #O(n) time complexity | O(1) space complexity
    def buildHeap(self, array):
        firstParentIdx = (len(array)-2)//2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx,len(array)-1, array)
        return array 
    # sorting according to the estimatedDistanceToEnd
    # O(log(n)) time complexity | O(1) space complexity
    def siftDown(self, currentIdx, endIdx, heap):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx *2 + 2 if currentIdx *2 + 2 <= endIdx else -1
            if(childTwoIdx!= -1 and heap[childTwoIdx].estimatedDistanceToEnd < heap[childOneIdx].estimatedDistanceToEnd):
               idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            if heap[idxToSwap].estimatedDistanceToEnd < heap[currentIdx].estimatedDistanceToEnd:
                self.swap(currentIdx,idxToSwap, heap)
                currentIdx = idxToSwap
                childOneIdx = currentIdx *2 + 1
            else:
                return 
    # sorting according to the estimatedDistanceToEnd
    # O(log(n)) time complexity | O(1) space complexity
    def siftUp(self, currentIdx, heap): 
        parentIdx = (currentIdx - 1)//2
        while currentIdx > 0 and heap[currentIdx].estimatedDistanceToEnd < heap[parentIdx].estimatedDistanceToEnd:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1)//2
    # removes from the nodePositionInHeap and heap
    def remove(self): 
        self.swap(0,len(self.heap)-1, self.heap)
        node = self.heap.pop()
        del self.nodePositionInHeap[node.id]
        self.siftDown(0, len(self.heap)-1, self.heap)
        return node
    # insert in  nodePositionInHeap and heap
    # O(log(n)) time complexity | O(1) space complexity
    def insert(self, node):
        self.heap.append(node)
        self.nodePositionInHeap[node.id] = len(self.heap)-1
        self.siftUp(len(self.heap)-1,self.heap)
    #swaps the position in nodePositionInHeap
    def swap(self, i, j, heap): 
        self.nodePositionInHeap[heap[i].id] = j
        self.nodePositionInHeap[heap[j].id] = i
        heap[i], heap[j] = heap[j], heap[i]
    # node is present in heap
    def containsNode(self, node): 
        return node.id in self.nodePositionInHeap
        # update nodes
    def update(self, node): 
        self.siftUp(self.nodePositionInHeap[node.id], self.heap)


def main():
    print(aStarAlgorithm(0,1,4,3,[[0,0,0,0,0],[0,1,1,0,0],[0,0,0,0,0],[1,0,1,1,1],[0,0,0,0,0]]))
main()
'''
Output
[[0, 1], [0, 0], [1, 0], [2, 0], [2, 1], [3, 1], [4, 1], [4, 2], [4, 3]]
'''