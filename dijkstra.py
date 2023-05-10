import math

def dijkstra(G, s): 
    V, E = G
    for v in V: # reset 
        v.dist = math.inf
        v.heapInd = None
    X = set([s])
    s.dist = 0
    h = []
    for e in s.outgoing:
        e.head.dist = e.length
        heapPush(h, e.head)
    while h and len(X) < len(V):
        v = heapPop(h)
        X.add(v)
        for e in v.outgoing:
            if e.head not in X:
                if e.head.heapInd == None:
                    e.head.dist = e.tail.dist + e.length
                    heapPush(h, e.head)
                elif e.tail.dist + e.length < e.head.dist:
                    e.head.dist = e.tail.dist + e.length
                    heapUpdate(h, e.head)
    return 

def dijkstraBig(G, s, ceiling): 
    V, E = G
    for v in V: # reset 
        v.dist = math.inf
        v.heapInd = None
    X = set([s])
    s.dist = 0
    h = []
    potential = False
    for e in s.outgoing:
        e.head.dist = e.length
        if e.head.dist < ceiling:
            potential = True
        heapPush(h, e.head)
    if not potential:
        return False
    while h and len(X) < len(V):
        v = heapPop(h)
        X.add(v)
        for e in v.outgoing:
            newDist = e.tail.dist + e.length
            if e.head not in X and newDist < ceiling:
                if e.head.heapInd == None:
                    e.head.dist = e.tail.dist + e.length
                    heapPush(h, e.head)
                elif e.tail.dist + e.length < e.head.dist:
                    e.head.dist = e.tail.dist + e.length
                    heapUpdate(h, e.head)
    return True 

def heapPush(h, v):
    h.append(v)
    v.heapInd = len(h)-1
    swim(h, v.heapInd)
    return

def swim(h, c):
    if len(h) < 2:
        return
    p = max(0, (c+1)//2 - 1)
    while h[c].dist < h[p].dist:
        swap(h, c, p)
        c = p
        p = max(0, (c+1)//2 - 1)
    return

def swap(h, i, j):
    h[i].heapInd = j
    h[j].heapInd = i
    temp = h[i]
    h[i] = h[j]
    h[j] = temp
    return
    
def heapUpdate(h, v):
    i = v.heapInd
    swim(h,i)
    sink(h,i)
    return

def sink(h, p):
    if len(h) < 2:
        return
    c1, c2 = 2*p + 1, 2*p + 2
    if c1 >= len(h):
        return
    elif c2 >= len(h):
        if h[p].dist > h[c1].dist:
            swap(h,p,c1)
        return
    elif h[p].dist > min(h[c1].dist, h[c2].dist):
        if h[c1].dist < h[c2].dist:
            swap(h,p,c1)
            p = c1
        else:
            swap(h,p,c2)
            p = c2
            c1, c2 = 2*p + 1, 2*p + 2
    else:
        return
    
def heapPop(h):
    swap(h,0,len(h)-1)
    x = h.pop()
    x.heapInd = None
    sink(h,0)
    return x

def printDists(G):
    V, E = G
    for v in V:
        print(f'Node {v.id} is {v.dist} from source')
    return