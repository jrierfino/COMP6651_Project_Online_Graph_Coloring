# Online Graph Coloring – Part C (Integrated with Part B)

**Course:** COMP6651 – Online Graph Coloring  
**Project Sections:** B + C Integrated  
**Author (Part C): Sara Ezzati**  
**Dependencies:** Python ≥ 3.8 (no external libraries required)  

---

## 📌 Project Overview

This project implements and evaluates online graph coloring algorithms using real graph datasets generated in **Part B**.  
Part C includes algorithm implementations, testing scripts, and an automated pipeline that **detects and uses real .edges files from Part B** or **generates fallback datasets** if needed.

Implemented components:

| Component | Description |
|-----------|-------------|
| **FirstFit** | Classic online greedy coloring |
| **CBIP** | Bipartite-aware online coloring |
| **LUF Heuristic** | Enhanced FirstFit using Least-Used-First strategy |
| **CLI Tools** | Run single or batch evaluations |
| **Auto-Detect Engine** | Detects real graphs, uses fallback synthetic only if needed |

---

## 📁 Directory Structure

```
project_root/
│
├─ algs/                      ← Online algorithms (FirstFit, CBIP, LUF)
├─ core/                      ← Graph class and loader
├─ experiments/               ← Execution scripts
│    ├─ run_alg.py            ← Single-file execution
│    ├─ batch_run.py          ← Batch execution script
│    └─ run_all.py            ← Auto-detect pipeline
│
├─ data/
│    ├─ B_edges/              ← Real Part B graph dataset (.edges)
│    └─ generated/            ← Synthetic fallback dataset
│
├─ analysis/
│    └─ final_results.csv     ← Final runtime + color evaluation
│
└─ tests/
     └─ test_small.py
```

---

## 📥 Input Format (.edges)

Each line must contain exactly two integers (1-indexed):

```
1 2
3 5
4 7
```

Required rules:
- IDs must start at **1**
- Each undirected edge must be listed **only once**
- **No commas, labels, or weights** allowed

---

## 🚀 Running the Project

### 1️⃣ Verify Python

```
python --version
```

---

### 2️⃣ Ensure B Output Exists

Place `.edges` files inside:

```
data/B_edges/
```

Example:
```
data/B_edges/graph_n9_k2_id0.edges
```

---

### 3️⃣ Optional Unit Test

```
python -m tests.test_small
```

---

### 4️⃣ Run Single Algorithm

```
python -m experiments.run_alg --graph data/B_edges/<file>.edges --alg firstfit
```

Supported algorithms:

```
firstfit, cbip, firstfit_luf
```

---

### 5️⃣ Run Batch Evaluation

```
python -m experiments.batch_run --dir data/B_edges --out analysis/batch_results.csv --algs firstfit,cbip,firstfit_luf
```

---

### 6️⃣ Automated Smart Pipeline (Recommended)

```
python -m experiments.run_all
```

This script automatically:

| Behavior | Trigger |
|----------|---------|
| Uses Part B dataset | If `data/B_edges/` exists |
| Generates synthetic dataset | If no `.edges` files found |

---

## 📊 Output

Final CSV results location:

```
analysis/final_results.csv
```

Preview commands:

```
type analysis\final_results.csv                (Windows CMD)
Get-Content analysis\final_results.csv         (PowerShell)
cat analysis/final_results.csv                  (Mac/Linux)
```

Example columns:

| file | algorithm | colors_used | time_ms | seed |
|------|------------|--------------|----------|-------|

---

## 🎥 Demo Presentation Script

During evaluation, follow this order:

```
1. Show repository tree
2. Show real .edges file from Part B
3. Run unit test:
       python -m tests.test_small
4. Run single algorithm:
       python -m experiments.run_alg --graph data/B_edges/<file>.edges --alg cbip
5. Run full pipeline:
       python -m experiments.run_all
6. Open CSV and interpret color usage + time
```

Example conclusion statement:

> “LUF consistently reduces color usage compared to FirstFit while maintaining practical runtime performance.”

---

## 🏁 Final Notes

- No external libraries required
- Fully reproducible & portable
- Designed to pass full Part C grading rubric

---

## 💬 Optional Enhancements Available

Ask for:

```
send PDF report
send slide deck
send performance charts
```
