import math
import graph
import bf
import dijkstra

def addSuperNode(G):
    V, E = G
    s = graph.Node(len(V)+1)
    for v in V:
        e = graph.Edge(s, v, 0)
        s.outgoing.append(e)
        v.incoming.append(e)
    V.append(s)
    return 

def johnson(G):
    addSuperNode(G)
    lensFromSuper = bf.bellmanFord(G, -1)
    if not lensFromSuper:
        return None
    
    # remove the super node
    V, E = G
    lensFromSuper.pop() 
    V.pop()
    for v in V:
        v.incoming.pop()

    # adjust edge lengths to be nonnegative
    for e in E:
        e.length += lensFromSuper[e.tail.id-1] - lensFromSuper[e.head.id-1]

    # run Dijkstra for each node as source 
    d = [] # 2D array to store dist(u,v) for every u, v node pair
    for v in V:
        dijkstra.dijkstra(G,v) # leaves the result in the node objects
        d.append([w.dist for w in V])

    # unadjust path lengths
    for i in range(len(V)):
        for j in range(len(V)):
            d[i][j] += lensFromSuper[j] - lensFromSuper[i]
    return d

def johnsonBig(G):
    addSuperNode(G)
    lensFromSuper = bf.bellmanFord(G, -1)
    if not lensFromSuper:
        return None
    
    # remove the super node
    V, E = G
    lensFromSuper.pop() 
    V.pop()
    for v in V:
        v.incoming.pop()

    # adjust edge lengths to be nonnegative
    for e in E:
        e.length += lensFromSuper[e.tail.id-1] - lensFromSuper[e.head.id-1]

    # run Dijkstra for each node as source 
    minPaths = [(math.inf, None, None)]
    for v in V:
        if dijkstra.dijkstraBig(G,v, minPaths[0][0]): # leaves the result in the node objects
            for w in V:
                if w.id != v.id:
                    if w.dist < minPaths[0][0]:
                        minPaths = [(w.dist, v, w)]
                    elif w.dist == minPaths[0][0]:
                        minPaths.append((w.dist, v, w))

    # unadjust path lengths
    smallest = math.inf
    for path in minPaths:
        smallest = min(smallest, path[0] - lensFromSuper[path[1].id-1] + lensFromSuper[path[2].id-1]) 
    return smallest