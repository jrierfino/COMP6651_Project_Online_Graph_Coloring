from core.graph import Graph
from algs.cbip import cbip
G=Graph.from_edges_file('data/examples/k2_toy.edges')
res=cbip(G)
assert max(res.values())<=2
print('Tests passed!')
