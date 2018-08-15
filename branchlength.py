#!/usr/bin/env python

from ete3 import Tree
from argparse import ArgumentParser
import matplotlib.pyplot as plt
import seaborn

def branchlength(newickfile):

    def plot_bl_bysupport(allmindistances, allsupportvalues, allleaves):
        plt.figure()
        plt.scatter(allmindistances, allsupportvalues)
        for i, leaf in enumerate(allleaves):
            if leaf == "recombinant":
                plt.annotate(leaf, (allmindistances[i], allsupportvalues[i]))
                plt.scatter(allmindistances[i], allsupportvalues[i], c='r')
            else:
                pass
                #plt.annotate(leaf, (allmindistances[i], allsupportvalues[i]))
        plottitle = str(name)
        plt.title(plottitle)
        plt.xlabel('Minimal branchlength to another leaf', fontsize=14)
        #plt.xlim((0, 0.7))
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
    allbranchlengths = []
    allsupportvalues = []

    for leaf in t:
        stringleaf = str(leaf.name)
        allleaves.append(stringleaf)
        leafup = leaf.up
        branchlength = leafup.get_distance(stringleaf)
        print('The branchlength of %s is %f.' %(stringleaf, branchlength))
        allbranchlengths.append(branchlength)
        supportvalue = leafup.support
        print('The support value of %s is %f.' %(stringleaf, supportvalue))
        allsupportvalues.append(supportvalue)

    plot_bl_bysupport(allbranchlengths[1:], allsupportvalues[1:], allleaves[1:])    

parser = ArgumentParser()
parser.add_argument('fname', nargs='+', action='append', metavar='FILE', help='Newick file to analyse.')
args = parser.parse_args()

filenames = args.fname
for filename in filenames[0]:
    branchlength(filename)

