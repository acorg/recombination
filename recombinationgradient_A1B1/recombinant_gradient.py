#!/usr/bin/env python

from ete3 import Tree
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import seaborn

def rec_parentdistance(newickfile):

    with open(newickfile) as f:
        name = f.name
        print('Analysing sample:', name)
        treedata = f.read()
        treedata = treedata.strip()
    t = Tree(treedata)

    # Reroot the tree.
    t.set_outgroup("root")
    print(t)

    # Find distance from recombinant to A1
    A1distance = t.get_distance("recombinant", "A-mutant-1")
    B1distance = t.get_distance("recombinant", "B-mutant-1")

    return(A1distance, B1distance)

    print('\n')

parser = ArgumentParser()
parser.add_argument('fname', nargs='+', action='append', metavar='FILE', help='Newick file to analyse.')
args = parser.parse_args()

A1_distances = []
B1_distances = []
filenames = args.fname
for filename in filenames[0]:
    recdistances = rec_parentdistance(filename)
    A1_distances.append(recdistances[0])
    B1_distances.append(recdistances[1])

listemitxwerten = [10, 20, 30, 40, 50, 60, 70, 80, 90]
plt.figure()
plt.plot(listemitxwerten, A1_distances, label="A1")
plt.plot(listemitxwerten, B1_distances, label="B1")
plt.title("Recombinant from A1 and B1 (a gradient of percentages)")
plt.xlabel("Percentage of recombinant from A1 (from B1=100-A1)", fontsize=14)
plt.ylabel('Distance to recombinant', fontsize=14)
plt.legend(fontsize=12)
plt.tight_layout()
plotpath = '../recombinants_A1B1.png'
plt.savefig(plotpath, dpi=300)