import subprocess
from experiments.generator import generate_batch

n_vals=[50,100,200,400,800]
k_vals=[2,3,4]
N=50
p=0.3

edges_dir='data/generated'
csv_out='analysis/final_results.csv'

def run():
    print("Generating graphs...")
    generate_batch(edges_dir, n_vals, k_vals, N, p)
    print("Running batch tests...")
    subprocess.run(["python","experiments/batch_run.py","--dir",edges_dir,"--out",csv_out,"--algs","firstfit,cbip,firstfit_luf"])

if __name__=='__main__': run()
