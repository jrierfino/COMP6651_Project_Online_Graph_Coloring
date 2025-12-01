import pandas as pd
import matplotlib.pyplot as plt
import os

INPUT_CSV = "data/results/simulation1_results.csv"
OUTPUT_DIR = "plots/simulation1"
os.makedirs(OUTPUT_DIR, exist_ok=True)

df = pd.read_csv(INPUT_CSV)

# Plot average competitive ratio vs n for each k
plt.figure(figsize=(8,6))
for k in sorted(df['k'].unique()):
    sub_df = df[(df['k'] == k) & (df['Algorithm'].str.contains('FirstFit'))]
    sub_df = sub_df.sort_values("n")   
    plt.plot(sub_df['n'], sub_df['rho(Alg)'], marker='o', label=f'k={k}')
plt.xlabel("Number of nodes (n)")
plt.ylabel("Average Competitive Ratio ρ(Alg)")
plt.title("FirstFit: Average Competitive Ratio vs n")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot_avg_rho_vs_n.png"))
plt.close()

# Plot standard deviation vs n for each k
plt.figure(figsize=(8,6))
for k in sorted(df['k'].unique()):
    sub_df = df[(df['k'] == k) & (df['Algorithm'].str.contains('FirstFit'))]
    sub_df = sub_df.sort_values("n")     # <-- SORTING ADDED
    plt.plot(sub_df['n'], sub_df['SD(rho(Alg))'], marker='o', label=f'k={k}')
plt.xlabel("Number of nodes (n)")
plt.ylabel("Standard Deviation of ρ(Alg)")
plt.title("FirstFit: Standard Deviation of Competitive Ratio vs n")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot_sd_rho_vs_n.png"))
plt.close()

# Plot runtime vs n for each k
plt.figure(figsize=(8,6))
for k in sorted(df['k'].unique()):
    sub_df = df[(df['k'] == k) & (df['Algorithm'].str.contains('FirstFit'))]
    sub_df = sub_df.sort_values("n")     # <-- SORTING ADDED
    plt.plot(sub_df['n'], sub_df['time_taken'], marker='o', label=f'k={k}')
plt.xlabel("Number of nodes (n)")
plt.ylabel("Time taken (seconds)")
plt.title("FirstFit: Runtime vs n")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot_runtime_vs_n.png"))
plt.close()

# Plot comparison of FirstFit vs CBIP for k=2
plt.figure(figsize=(8,6))
for alg in ['FirstFit', 'CBIP']:
    sub_df = df[(df['k'] == 2) & (df['Algorithm'] == alg)]
    sub_df = sub_df.sort_values("n")     # <-- SORTING ADDED
    plt.plot(sub_df['n'], sub_df['rho(Alg)'], marker='o', label=alg)
plt.xlabel("Number of nodes (n)")
plt.ylabel("Average Competitive Ratio ρ(Alg)")
plt.title("Comparison: FirstFit vs CBIP (k=2)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "plot_comparison_k2.png"))
plt.close()

print(f"All plots saved in '{OUTPUT_DIR}'")
