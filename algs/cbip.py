import random
from collections import deque

def bipartition(G, cc, start):
    color={start:0}
    q=deque([start])
    while q:
        v=q.popleft()
        for nb in G.neighbors(v):
            if nb in cc:
                if nb not in color:
                    color[nb]=1-color[v]
                    q.append(nb)
                elif color[nb]==color[v]:
                    return {x:0 for x in cc}
    return color

def cbip(G, order=None):
    vertices = G.vertices()
    if order is None:
        order = vertices[:]
        random.shuffle(order)
    c={}
    for i,v in enumerate(order):
        revealed=set(order[:i])
        cc = G.connected_component(v, revealed)
        part=bipartition(G, cc, v)
        A={x for x in cc if part.get(x,0)==part[v]}
        B={x for x in cc if x not in A}
        usedB={c[x] for x in B if x in c}
        col=1
        while col in usedB:
            col+=1
        c[v]=col
    return c
