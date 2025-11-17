import random, os
from core.graph import Graph

def generate_k_colorable(n, k, p):
    sets=[[] for _ in range(k)]
    for i in range(n):
        sets[i%k].append(i+1)
    for s in sets: random.shuffle(s)

    G=Graph()
    for i in range(1,n+1): G.add_vertex(i)

    for i in range(k):
        for j in range(i+1,k):
            for u in sets[i]:
                for v in sets[j]:
                    if random.random() < p:
                        G.add_edge(u,v)
    return G

def save_edges(G, path):
    with open(path,'w') as f:
        for u in G.vertices():
            for v in G.neighbors(u):
                if u < v:
                    f.write(f"{u} {v}\n")

def generate_batch(output_dir, n_values, k_values, N, p):
    os.makedirs(output_dir, exist_ok=True)
    for k in k_values:
        for n in n_values:
            for i in range(N):
                G=generate_k_colorable(n,k,p)
                save_edges(G, os.path.join(output_dir, f"g_n{n}_k{k}_{i}.edges"))
