from algs.firstfit import firstfit
def firstfit_luf(G):
    vertices = sorted(G.vertices(), key=lambda v: len(G.neighbors(v)), reverse=True)
    return firstfit(G, order=vertices)
