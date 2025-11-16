import argparse, os, csv, time
from core.graph import Graph
from algs.firstfit import firstfit
from algs.cbip import cbip
from algs.heuristics import firstfit_luf

ALG_MAP={'firstfit':firstfit,'cbip':cbip,'firstfit_luf':firstfit_luf}

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--dir', required=True)
    p.add_argument('--out', required=True)
    p.add_argument('--algs', required=True)
    args=p.parse_args()

    algs=args.algs.split(',')
    files=[os.path.join(args.dir,f) for f in os.listdir(args.dir) if f.endswith('.edges')]

    with open(args.out,'w',newline='') as f:
        w=csv.writer(f)
        w.writerow(['file','algorithm','colors_used','time_ms'])
        for file in files:
            G=Graph.from_edges_file(file)
            for alg in algs:
                start=time.time()
                result=ALG_MAP[alg](G)
                end=time.time()
                w.writerow([os.path.basename(file),alg,max(result.values()),(end-start)*1000])

if __name__=='__main__': main()
