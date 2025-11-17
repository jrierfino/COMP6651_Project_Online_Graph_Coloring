# Online Graph Coloring Experiments

COMP6651 project for studying the competitive performance of online graph coloring heuristics on randomly generated *k*-colorable graphs.

## Repository Layout

- `graph.py` – data structures plus the `KColorable_Graph_Generator` and `load_graph_from_edges` helper.
- `algs/` – implementations of the First-Fit, CBIP, and FirstFit-LUF algorithms.
- `generate_graphs.py` – batch generator that saves `*.edges` files under `data/B_edges/graph_n{n}_k{k}`.
- `simulation1.py` – runs First-Fit for `k ∈ {2,3,4}` and CBIP for `k=2`, writing aggregates to `simulation1_results.csv`.
- `simulation2.py` – runs the FirstFit-LUF heuristic for the same input set and writes `simulation2_results.csv`.

## Requirements

- Python 3.10+.

## Usage

1. **Generate graphs (optional if `data/B_edges` already exists).**
   ```bash
   python generate_graphs.py
   ```
   Edit `n_values`, `k_values`, or the number of graphs per configuration in `generate_graphs_for_table()` to control how many instances are produced. Graphs are saved as edge lists (one undirected edge per line).

2. **Run Simulation I (First-Fit & CBIP).**
   ```bash
   python simulation1.py
   ```
   The script walks every folder named `graph_n{n}_k{k}` under `data/B_edges`, loads each `.edges` file, and records the average competitive ratio `ρ = χ_used / k`, its population standard deviation, and wall-clock time. Results land in `simulation1_results.csv` and can also be opened as `simulation1_results.xlsx` for sharing.

3. **Run Simulation II (FirstFit-LUF heuristic).**
   ```bash
   python simulation2.py
   ```
   Produces the same summary columns as Simulation I but only for the LUF ordering variant of First-Fit, saving them to `simulation2_results.csv` (and the companion Excel file if you export it).

## Tips

- The scripts assume the directory layout under `data/B_edges` exactly matches `graph_n{n}_k{k}`. If you change the generator output path, update `BASE_DIR` in both simulations.
- CSV files are convenient for plotting or statistical analysis. The repo also contains helper notebooks/scripts for visualizations (`generate_graphs.py` and `graph.py` contain all utilities you need).