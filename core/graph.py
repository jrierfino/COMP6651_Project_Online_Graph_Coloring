class Graph:
    def __init__(self, edges=None):
        self.adj = {}
        if edges:
            for u,v in edges:
                self.add_edge(u,v)

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = set()

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)
        self.adj[v].add(u)

    @staticmethod
    def from_edges_file(path):
        edges=[]
        with open(path) as f:
            for line in f:
                a,b=line.split()
                edges.append((int(a),int(b)))
        return Graph(edges)

    def neighbors(self, v):
        return self.adj.get(v, set())

    def vertices(self):
        return list(self.adj.keys())

    def connected_component(self, start, revealed):
        visited=set()
        stack=[start]
        while stack:
            x=stack.pop()
            if x in visited: continue
            visited.add(x)
            for nb in self.neighbors(x):
                if nb in revealed:
                    stack.append(nb)
        return visited
