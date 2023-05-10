import graph
import johnson

def readInputToAdjList(filename):
    with open(filename, 'r') as f:
        n, m = [int(x) for x in f.readline().strip().split()]
        V = [graph.Node(i+1) for i in range(n)]
        E = []
        for line in f:
            i, j, c = [int(x) for x in line.strip().split()]
            e = graph.Edge(V[i-1], V[j-1], c)
            E.append(e)
            V[i-1].outgoing.append(e)
            V[j-1].incoming.append(e)
    return (V, E)

def printShortestPaths(d):
    for i in range(len(d)):
        for j in range(len(d)):
            print(f'Path: Node {i+1} => Node {j+1}, Length: {d[i][j]}')
    return

def shortestShortestPath(d):
    smallest = d[0][0]
    for col in d:
        smallest = min(smallest, min(col))
    return smallest

def runJohnson(filename):
    print(f'Running Johnson\'s algorithm with file {filename}...')
    G = readInputToAdjList(filename)
    d = johnson.johnson(G)
    if not d:
        print('Graph has a negative cycle!')
    else:
        smallest = shortestShortestPath(d)
        print(f'The shortest shortest path has length {smallest}')
    print('\n')
    return

def runJohnsonBig(filename):
    print(f'Running Johnson\'s algorithm (for big inputs) with file {filename}...')
    G = readInputToAdjList(filename)
    d = johnson.johnsonBig(G)
    if d is None:
        print('Graph has a negative cycle!')
    else:
        print(f'The shortest shortest path has length {d}')
    print('\n')
    return

files = ['g_small.txt', 'g1.txt', 'g2.txt', 'g3.txt', 'large.txt']
runJohnson(files[3])
runJohnsonBig(files[3])