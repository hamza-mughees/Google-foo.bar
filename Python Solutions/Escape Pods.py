INF = float('inf')

def addSuperSrcSnk(entrances, exits, path):
    n = len(path)
    
    if len(entrances) > 1 or len(exits) > 1:
        for r in path:
            r.append(0)
            r.insert(0, 0)
    
    if len(entrances) > 1:
        entrances = [i+1 for i in entrances]
        
        srcRow = (n+2) * [0]
        for i in entrances:
            srcRow[i] = INF     # supersource to source capacities = infinity
        path.insert(0, srcRow)
    
    if len(exits) > 1:
        exits = [i+1 for i in exits]
        snkRow = (n+2) * [0]
        for i in exits:
            path[i][-1] = INF     # sink to supersink capacities = infinity
        path.append(snkRow)
    
    return entrances, exits, path

def bfs(src, snk, path, flowMtx):
    n = len(path)
    prev = n * [-1]
    q = []
    
    prev[src] = -2      # to separate the src from the other nodes
    q.append(src)
    
    while prev[snk] == -1 and q:
        u = q.pop(0)
        for v in range(n):
            cap = path[u][v] - flowMtx[u][v]
            
            if prev[v] == -1 and cap > 0:
                q.append(v)
                prev[v] = u
    
    if prev[snk] == -1:
        return 0, prev       # no path to sink
    
    v = snk
    pathFlow = INF       # so this value is always changed
    
    while v != src:
        u = prev[v]
        cap = path[u][v] - flowMtx[u][v]
        pathFlow = min(cap, pathFlow)
        v = u
    
    return pathFlow, prev

def solution(entrances, exits, path):
    addSuperSrcSnk(entrances, exits, path)
    
    n = len(path)
    maxFlow = 0
    flowMtx = [[0 for i in range(n)] for j in range(n)]
    src = 0
    snk = n - 1
    
    while True:
        pathFlow, prev = bfs(src, snk, path, flowMtx)
        
        if pathFlow == 0:
            break
        
        maxFlow += pathFlow
        v = snk
        
        while v != src:
            u = prev[v]
            flowMtx[u][v] += pathFlow
            flowMtx[v][u] -= pathFlow
            v = u
    
    return maxFlow