import random
import os
from collections import deque


class Vertex:
    def __init__(self, vid):
        self.id = vid
        self.distance = 0
        self.predecessor = None
        self.color = None

    def __repr__(self):
        return f"Vertex({self.id})"


class Edge:
    def __init__(self, left_edge, right_edge, weight=0):
        self.left_edge = left_edge
        self.right_edge = right_edge
        self.weight = weight


class Graph:
    """
    Undirected simple graph using Vertex objects.
    Provides the API expected by firstfit and cbip:
      - vertices()
      - neighbors(v)
      - connected_component(start, allowed)
    """
    def __init__(self, vertices=None):
        self._vertices = set()
        self._adj = {}      # dict[Vertex, set[Vertex]]
        self.edges = set()  # set[Edge]
        if vertices is not None:
            for v in vertices:
                self.add_vertex(v)

    # --- basic graph construction ---

    def add_vertex(self, v):
        if v not in self._vertices:
            self._vertices.add(v)
            self._adj[v] = set()

    def add_edge(self, u, v, weight=0):
        """Add an undirected edge {u, v}."""
        if u is v:
            return  # no self-loops
        self.add_vertex(u)
        self.add_vertex(v)

        if v not in self._adj[u]:
            self._adj[u].add(v)
            self._adj[v].add(u)
            self.edges.add(Edge(u, v, weight))

    # --- API used by algorithms ---

    def vertices(self):
        """Return a list of all vertices."""
        return list(self._vertices)

    def neighbors(self, v):
        """Return an iterable of neighbors of v."""
        return self._adj.get(v, set())

    def connected_component(self, start, allowed=None):
        """
        Return the connected component of 'start' within the
        subgraph induced by 'allowed' ∪ {start}.
        """
        if allowed is None:
            allowed = self._vertices
        allowed = set(allowed)
        allowed.add(start)

        visited = set()
        queue = deque()

        if start not in allowed:
            return visited

        visited.add(start)
        queue.append(start)

        while queue:
            v = queue.popleft()
            for nb in self.neighbors(v):
                if nb in allowed and nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return visited


class KColorable_Graph_Generator:
    def __init__(self, seed=42, folder_path="data/B_edges/"):
        self.seed = seed
        self.folder_path = folder_path


    def save_edges(self, G, n, k, p):
        folder = os.path.join(self.folder_path, f"graph_n{n}_k{k}")
        os.makedirs(folder, exist_ok=True)

        graph_id = int(round(p * 100))  # e.g., p=0.01 -> 1, p=1.00 -> 100
        file_name = f"graph_n{n}_k{k}_id{graph_id}.edges"
        full_file_path = os.path.join(folder, file_name)

        with open(full_file_path, "w", encoding="ascii") as f:
            for edge in G.edges:
                u_id = edge.left_edge.id
                v_id = edge.right_edge.id
                f.write(f"{u_id} {v_id}\n")

        print(f"Saved graph (n={n}, k={k}, p={p:.2f}) to {full_file_path}")


    def generate_online_kcolourable_graph(self, n, k, p=0.5, save=True):
        """
        Generate a random online k-colourable graph on n vertices.

        - Vertices are partitioned into k non-empty independent sets S_1,...,S_k.
        - Edges are only between different sets (no edges inside a set).
        - For every pair of sets (S_i, S_j), every vertex in S_i has at least
          one neighbor in S_j.
        - Additional edges between sets are added with probability p.
        """
        assert k > 0, "k must be positive"
        assert n >= k, "n must be at least k so each colour class is non-empty"

        random.seed(self.seed)

        vertices = [Vertex(i + 1) for i in range(n)]

        sets = [[] for _ in range(k)]
        for i in range(k):
            sets[i].append(vertices[i])
        for i in range(k, n):
            idx = random.randrange(k)
            sets[idx].append(vertices[i])

        G = Graph(vertices)

        for i in range(k):
            S_i = sets[i]
            for v in S_i:
                for j in range(k):
                    if j == i:
                        continue
                    S_j = sets[j]

                    u_mandatory = random.choice(S_j)
                    G.add_edge(v, u_mandatory)

                    for u in S_j:
                        if u is u_mandatory:
                            continue
                        if random.random() < p:
                            G.add_edge(v, u)

        if save:
            self.save_edges(G, n, k, p)

        return G
    
def load_graph_from_edges(file_path):
    id_to_vertex = {}

    def get_vertex(vid):
        if vid not in id_to_vertex:
            id_to_vertex[vid] = Vertex(vid)
        return id_to_vertex[vid]

    G = Graph()

    with open(file_path, "r", encoding="ascii") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            u_id = int(parts[0])
            v_id = int(parts[1])
            u = get_vertex(u_id)
            v = get_vertex(v_id)
            G.add_edge(u, v)

    return G
