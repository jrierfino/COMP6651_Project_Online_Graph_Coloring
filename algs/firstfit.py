import random
def firstfit(G, order=None):
    vertices = G.vertices()
    if order is None:
        order = vertices[:]
        random.shuffle(order)
    c = {}
    for i,v in enumerate(order):
        revealed = set(order[:i])
        neigh = set(G.neighbors(v)) & revealed
        used = {c[x] for x in neigh if x in c}
        col=1
        while col in used:
            col+=1
        c[v]=col
    return c
