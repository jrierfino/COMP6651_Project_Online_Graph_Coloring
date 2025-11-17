import argparse, json, time
from core.graph import Graph
from algs.firstfit import firstfit
from algs.cbip import cbip
from algs.heuristics import firstfit_luf

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--graph', required=True)
    p.add_argument('--alg', choices=['firstfit','cbip','firstfit_luf'], required=True)
    args=p.parse_args()

    G=Graph.from_edges_file(args.graph)
    start=time.time()
    if args.alg=='firstfit': res=firstfit(G)
    elif args.alg=='cbip': res=cbip(G)
    else: res=firstfit_luf(G)
    end=time.time()

    print(json.dumps({
        "colors_used": max(res.values()),
        "time_ms": (end-start)*1000,
        "assignments": res
    }, indent=2))

if __name__=="__main__": main()
