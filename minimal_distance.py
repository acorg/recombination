#!/usr/bin/env python

from ete3 import Tree
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import seaborn

def maxbranchlength(newickfile):

    def plot_bl_bysupport(allmindistances, allaveragedistances, allleaves):
        plt.figure()
        plt.scatter(allmindistances, allaveragedistances)
        for i, leaf in enumerate(allleaves):
            if leaf == "recombinant":
                plt.annotate(leaf, (allmindistances[i], allaveragedistances[i]))
                plt.scatter(allmindistances[i], allaveragedistances[i], c='r')
            else:
                pass
                #plt.annotate(leaf, (allmindistances[i], allaveragedistances[i]))
        plottitle = str(name)
        plt.title(plottitle)
        plt.xlabel('Minimal branchlength to another leaf', fontsize=14)
        plt.xlim((0, 0.7))
        plt.ylabel('Support value', fontsize=14)
        plt.ylim((15, 102))
        plt.tight_layout()
        plotpath = 'branchlengthplot/' + str(name) + '.png'
        plt.savefig(plotpath, dpi=300)

    # Input the tree data. This is written for newick, as the code assumes only 
    # one input line.
    with open(newickfile) as f:
        name = f.name
        print('Analysing sample:', name)
        treedata = f.read()
        treedata = treedata.strip()
    t = Tree(treedata)

    # Reroot the tree.
    t.set_outgroup("root")

    allleaves = []
    allmindistanceleaves = []
    allmindistances = []
    allsupportvalues = []

    for leaf in t:
        stringleaf = str(leaf.name)
        allleaves.append(stringleaf)

        # Find the leaf2 with the smallest distance to leaf.
        alldistances = []
        allleaves2 = []
        for leaf2 in t:
            stringleaf2 = str(leaf2.name)
            if stringleaf2 == stringleaf:
                pass
            else:
                distance = leaf2.get_distance(stringleaf)
                alldistances.append(distance)
                allleaves2.append(stringleaf2)
        mindist = min(alldistances)
        allmindistances.append(mindist)
        leaf2mindist = allleaves2[alldistances.index(mindist)]
        allmindistanceleaves.append(leaf2mindist)

        # Find support value for parent internal node of leaf.
        leafup = leaf.up
        supportvalue = leafup.support
        allsupportvalues.append(supportvalue)

    # Textoutput.
    if "recombinant" not in allleaves:
        print('There is no recombinant in this sample.')
    maxmindist = max(allmindistances)
    maxminleaf = str(allleaves[allmindistances.index(maxmindist)])
    maxminleaf2 = str(allmindistanceleaves[allmindistances.index(maxmindist)])
    minsupport = min(allsupportvalues[1:])
    minsupportleaf = str(allleaves[allsupportvalues.index(minsupport)])
    print('The leaf with the biggest minimal distance to another leaf is %s, to %s.' %(maxminleaf, maxminleaf2))
    print('The leaf with the parental node with a minimal branch bootstrap value is %s.' %(minsupportleaf))
    #print(allleaves)
    #print(allmindistanceleaves)
    #print(allmindistances)
    #print(allsupportvalues)
    if all(element==1.0 for element in allsupportvalues):
        print('There are no bootstrapvalues in the newick file.')

    # Plot branchlength against bootstrap value, leave out root (at index 0).
    plot_bl_bysupport(allmindistances[1:], allsupportvalues[1:], allleaves[1:])

parser = ArgumentParser()
parser.add_argument('fname', nargs='+', action='append', metavar='FILE', help='Newick file to analyse.')
args = parser.parse_args()

filenames = args.fname
for filename in filenames[0]:
    maxbranchlength(filename)
    print('\n')