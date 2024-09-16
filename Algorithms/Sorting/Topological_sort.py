#Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u,v vertex u comes before v in the ordering.
#Topological sorting for a graph is not possible id the graph is not a DAG.

#Time complexity: O(V+E)
#Space complexity: O(V)


def topsort(g, vtx):
    degree = [0]*vtx
    for node in g:
        for adjnode in g[node]:
            degree[adjnode]+=1
    
    bfs = [i for i in range(vtx) if degree[i] == 0]
    for node in bfs:
        for adjnode in g[node]:
            degree[adjnode]-=1 
            if degree[adjnode] == 0:
                bfs.append(adjnode)
    return bfs

from collections import defaultdict
g = defaultdict(list)
vtx, e = map(int, input().split())
for i in range(e):
    u,v = map(int, input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    g[u].append(v)
topsort = topsort(g, vtx)
topsort = [chr(i+65) for i in topsort]
print(topsort(g, vtx))