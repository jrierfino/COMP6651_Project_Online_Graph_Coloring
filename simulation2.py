import os
import re
import time
import csv
import statistics as stats

from tqdm import tqdm

from graph import load_graph_from_edges
from algs.heuristics import firstfit_luf 


BASE_DIR = "data/B_edges" 
OUTPUT_CSV = "simulation2_results.csv"


def run_simulation2():
    """
    For each folder graph_n{n}_k{k} in BASE_DIR, load all graphs,
    run the heuristic FirstFit (firstfit_luf) on them, and save a CSV with:

    Algorithm, k, n, N, rho(Alg), SD(rho(Alg)), time_taken
    """

    results_rows = []

    folder_pattern = re.compile(r"graph_n(\d+)_k(\d+)$")

    for folder in sorted(os.listdir(BASE_DIR)):
        m = folder_pattern.match(folder)
        if not m:
            continue

        n = int(m.group(1))
        k = int(m.group(2))
        folder_path = os.path.join(BASE_DIR, folder)

        edge_files = sorted(
            f for f in os.listdir(folder_path)
            if f.endswith(".edges")
        )
        if not edge_files:
            continue

        file_paths = [os.path.join(folder_path, f) for f in edge_files]
        N = len(file_paths)

        alg_name = "FirstFit_LUF"
        start = time.perf_counter()
        ratios = []

        for path in tqdm(
            file_paths,
            desc=f"{alg_name} (k={k}, n={n})",
            unit="graph"
        ):
            G = load_graph_from_edges(path)
            coloring = firstfit_luf(G)
            num_colors = max(coloring.values()) if coloring else 0
            rho = num_colors / k
            ratios.append(rho)

        end = time.perf_counter()
        avg_rho = sum(ratios) / N
        sd_rho = stats.pstdev(ratios) if N > 1 else 0.0
        time_taken = end - start

        results_rows.append(
            (alg_name, k, n, N, avg_rho, sd_rho, time_taken)
        )

    header = [
        "Algorithm",
        "k",
        "n",
        "N",
        "rho(Alg)",        # average competitive ratio
        "SD(rho(Alg))",    # std-dev of competitive ratios
        "time_taken",      # seconds
    ]

    with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for row in results_rows:
            writer.writerow(row)

    print(f"Saved Simulation II results to {OUTPUT_CSV}")


if __name__ == "__main__":
    run_simulation2()
