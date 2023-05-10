import math

# Returns a list, indexed by node ID, of shortest paths from source
# Returns None if graph contains a negative cycle
# Takes as input the graph and index of the source vertex in V
def bellmanFord(G, s):
    V, E = G
    A = [[math.inf for j in range(len(V))] for i in range(len(V)+1)]
    A[0][s] = 0 
    for i in range(1, len(V)+1):
        stable = True
        for v in range(len(V)):
            incl = math.inf
            for e in V[v].incoming:
                p = A[i-1][e.tail.id-1] + e.length
                incl = min(p, incl) 
            A[i][v] = min(A[i-1][v], incl)
            if A[i][v] != A[i-1][v]:
                stable = False
        if stable:
            return A[i-1]
    return None