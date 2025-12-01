import pandas as pd
import matplotlib.pyplot as plt
import os

FILE_SIM1 = "data/results/simulation1_results.csv"
FILE_SIM2 = "data/results/simulation2_results.csv"
PLOTS_SIM2 = "plots/simulation2"
os.makedirs(PLOTS_SIM2, exist_ok=True)

df1 = pd.read_csv(FILE_SIM1)
df1 = df1[df1["Algorithm"] == "FirstFit"] 
df2 = pd.read_csv(FILE_SIM2)

# Plot competitive ratio vs n
plt.figure(figsize=(8,6))
for k in sorted(df2["k"].unique()):
    sub = df2[df2["k"] == k].sort_values("n") 
    plt.plot(sub["n"], sub["rho(Alg)"], marker="o", label=f"k={k}")
plt.title("FirstFit-LUF Competitive Ratio vs n (Simulation II)")
plt.xlabel("n")
plt.ylabel("ρ (competitive ratio)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_SIM2, "plot_rho_vs_n_by_k.png"), dpi=300)
plt.close()

# Plot variance vs n
plt.figure(figsize=(8,6))
for k in sorted(df2["k"].unique()):
    sub = df2[df2["k"] == k].sort_values("n") 
    plt.errorbar(
        sub["n"], sub["rho(Alg)"], yerr=sub["SD(rho(Alg))"],
        fmt="o-", capsize=4, label=f"k={k}"
    )
plt.title("FirstFit-LUF Competitive Ratio ± SD (Simulation II)")
plt.xlabel("n")
plt.ylabel("ρ (competitive ratio)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_SIM2, "plot_variance_vs_n.png"), dpi=300)
plt.close()

# Plot Runtime vs n
plt.figure(figsize=(8,6))
for k in sorted(df2["k"].unique()):
    sub = df2[df2["k"] == k].sort_values("n") 
    plt.plot(sub["n"], sub["time_taken"], marker="o", label=f"k={k}")
plt.title("FirstFit-LUF Runtime vs n (Simulation II)")
plt.xlabel("n")
plt.ylabel("Time (seconds)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_SIM2, "plot_runtime_vs_n.png"), dpi=300)
plt.close()

# Plot comparison of FirstFit vs FirstFit-LUF
plt.figure(figsize=(8,6))
for k in sorted(df2["k"].unique()):
    sub1 = df1[df1["k"] == k].sort_values("n")
    sub2 = df2[df2["k"] == k].sort_values("n") 
    common_n = sorted(set(sub1["n"]) & set(sub2["n"]))
    sub1 = sub1[sub1["n"].isin(common_n)]
    sub2 = sub2[sub2["n"].isin(common_n)]

    plt.plot(sub1["n"], sub1["rho(Alg)"], marker="o", label=f"FirstFit k={k}")
    plt.plot(sub2["n"], sub2["rho(Alg)"], marker="s", label=f"FirstFit-LUF k={k}")

plt.title("FirstFit vs FirstFit-LUF (Simulation II)")
plt.xlabel("n")
plt.ylabel("ρ (competitive ratio)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(PLOTS_SIM2, "plot_comparison_firstfit_luf.png"), dpi=300)
plt.close()

print("Simulation II plots saved in 'plots/simulation2/'")
