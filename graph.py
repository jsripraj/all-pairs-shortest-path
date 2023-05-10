import math

class Node:
    def __init__(self, id) -> None:
        self.id = id
        self.incoming = []
        self.outgoing = []
        self.dist = math.inf
        self.heapInd = None

class Edge:
    def __init__(self, tail, head, length) -> None:
        self.tail = tail
        self.head = head
        self.length = length

def printGraph(G):
    V = G[0]
    for v in V:
        for e in v.outgoing:
            print(f'Node {e.tail.id} => Node {e.head.id} with length {e.length}')
    return