import os
import subprocess
from experiments.generator import generate_batch

# ------------------------------------------
# PARAMETERS for fallback synthetic generation
# ------------------------------------------
N_VALUES = [50, 100, 200]
K_VALUES = [2, 3, 4]
NUM_GRAPHS = 10
EDGE_PROB = 0.35  # probability for synthetic generator

# ------------------------------------------
# Candidate input paths for PART B output (.edges)
# ------------------------------------------
CANDIDATE_DIRS = [
    "data/B_edges",
    "data/B",
    "data/b_edges",
    "data/b_output",
    "data/k2",
    "data/k3",
    "data/k4",
]

# fallback path when B not available
FALLBACK_DIR = "data/generated"

# final CSV output file
OUTPUT_CSV = "analysis/final_results.csv"

# algorithms to run
ALGORITHM_LIST = "firstfit,cbip,firstfit_luf"


def detect_input_directory():
    """
    Smart auto-detection:
    Checks valid directories for B output that contain at least one .edges file.
    Returns path if found, else None
    """
    for path in CANDIDATE_DIRS:
        if os.path.exists(path) and os.path.isdir(path):
            edges = [f for f in os.listdir(path) if f.endswith(".edges")]
            if edges:
                print(f"✔ Detected Part B graph dataset at: {path}")
                return path
    return None


def ensure_directory_exists(path):
    folder = os.path.dirname(path)
    if folder and not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)


def main():
    # STEP 1 — Detect real B dataset
    input_dir = detect_input_directory()

    # STEP 2 — If no B dataset found → generate fallback synthetic dataset
    if input_dir is None:
        print("\n⚠ No Part B dataset detected.")
        print(f"→ Fallback mode: generating synthetic graphs in {FALLBACK_DIR}")
        input_dir = FALLBACK_DIR
        if not os.path.exists(input_dir) or not os.listdir(input_dir):
            generate_batch(input_dir, N_VALUES, K_VALUES, NUM_GRAPHS, EDGE_PROB)

    # STEP 3 — Ensure output directory for analysis exists
    ensure_directory_exists(OUTPUT_CSV)

    # STEP 4 — Run batch execution
    print("\n🚀 Running Evaluation Batch...")
    subprocess.run([
        "python", "-m", "experiments.batch_run",
        "--dir", input_dir,
        "--out", OUTPUT_CSV,
        "--algs", ALGORITHM_LIST
    ], check=True)

    print("\n🎉 DONE — Final integrated results saved at:")
    print(f"➡ {OUTPUT_CSV}")

    print("\n🧪 You can preview results using:")
    print("   type analysis\\final_results.csv   (Windows CMD)")
    print("   Get-Content analysis\\final_results.csv -TotalCount 20   (PowerShell)")
    print("   cat analysis/final_results.csv     (Linux/Mac)")


if __name__ == "__main__":
    main()
