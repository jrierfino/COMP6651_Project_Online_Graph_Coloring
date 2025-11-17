from graph import KColorable_Graph_Generator
import time

def generate_graphs_for_table():
    gen = KColorable_Graph_Generator(seed=42, folder_path="data/B_edges")

    n_values = [50, 100, 200, 400, 800, 1600, 3200]
    k_values = [2, 3, 4, 5]  
    num_graphs = 100 

    for k in k_values:
        for n in n_values:
            for i in range(1, num_graphs + 1):
                p = i / num_graphs   # 0.01, 0.02, ..., 1.00
                gen.generate_online_kcolourable_graph(n=n, k=k, p=p, save=True)


if __name__ == "__main__":
    t0 = time.perf_counter()
    generate_graphs_for_table()
    t1 = time.perf_counter()
    total_t = t1 - t0
    print(f"Time taken: {total_t}")