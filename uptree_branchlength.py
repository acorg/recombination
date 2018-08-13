#!/usr/bin/env python

from ete3 import Tree
from argparse import ArgumentParser

def maxbranchlength(newickfile):

    # Define helper functions.
    def locate_nodes(t):
        root = t&"root"
        A = t&"A"
        A1 = t&"A-mutant-1"
        A2 = t&"A-mutant-2"
        A3 = t&"A-mutant-3"
        A4 = t&"A-mutant-4"
        A5 = t&"A-mutant-5"
        A6 = t&"A-mutant-6"
        A7 = t&"A-mutant-7"
        A8 = t&"A-mutant-8"
        A9 = t&"A-mutant-9"
        B = t&"B"
        B1 = t&"B-mutant-1"
        B2 = t&"B-mutant-2"
        B3 = t&"B-mutant-3"
        B4 = t&"B-mutant-4"
        B5 = t&"B-mutant-5"
        B6 = t&"B-mutant-6"
        B7 = t&"B-mutant-7"
        B8 = t&"B-mutant-8"
        B9 = t&"B-mutant-9"

    def add_uptree_node(ancestor, position):
        uptreenode = ancestor.children[position]
        alluptreenodes.append(uptreenode)

    def which_uptree(position):
        z = ancestors.children[position]
        print(z)
        closestleaf = z.get_closest_leaf()[0]
        print('closestleaf')
        print(closestleaf)
        print('distance to A3')
        print(z.get_distance("A-mutant-3"))
        print(t.get_distance("A-mutant-3", "A-mutant-5"))
        print('distance to A4')
        print(z.get_distance("A-mutant-4"))
        print(t.get_distance("A-mutant-4", "A-mutant-5"))
        top_dist = closestleaf.get_distance(stringnode, topology_only = True)
        print(top_dist)
        # If the closest leaf is the node we want to get the uptree node of:
        if top_dist == 0:
            newancestors = ancestors.get_ancestors()[0]
            if len(newancestors.children[0]) == 1:
                add_uptree_node(newancestors, 0)
            elif len(newancestors.children[1]) == 1:
                add_uptree_node(newancestors, 1)
            elif len(newancestors.children[0]) == 2:
                newz = newancestors.children[0]
                uptreenode = newz.get_closest_leaf()[0]
                print(uptreenode)
                alluptreenodes.append(uptreenode)
            elif len(newancestors.children[1]) == 2:
                newz = newancestors.children[1]
                uptreenode = newz.get_closest_leaf()[0]
                print(uptreenode)
                alluptreenodes.append(uptreenode)
                
        # If the closest leaf is one node away from the node we want to get the uptree node of:
        elif top_dist == 1:
            uptreenode = closestleaf
            alluptreenodes.append(uptreenode)
        # If the closest leaf is three nodes away from the node we want to get the uptree node of:
        elif top_dist == 3:
            print('top is three!')
            uptreenode = closestleaf.get_sisters()[0]
            print(closestleaf.get_sisters())
            alluptreenodes.append(uptreenode)

    # Input the tree data. This is written for newick, as the code assumes only 
    # one input line.
    with open(newickfile) as f:
        name = f.name
        print('Sample:', name)
        treedata = f.read()
        treedata = treedata.strip()
    t = Tree(treedata)
    locate_nodes(t)

    # Check if there is a recombinant, if so locate node.
    recombinants = t.get_leaves_by_name("recombinant")    
    if len(recombinants) == 0:
        print('There is no recombinant in this sample.')
    elif len(recombinants) > 1:
        print('There is more than one recombinant in this sample.')
    else:
        recombinant = recombinants[0]
    
    # Reroot the tree.
    t.set_outgroup("root")
    print(t)

    # Define lists to be filled.
    allnodes = []
    alluptreenodes = []
    alldistances = []

    # Fill allnodes and alluptreenodes list.
    for node in t.traverse("preorder"):
        stringnode = str(node.name)
        # Leave out all internal (unnamed) nodes.
        if stringnode.startswith(('A', 'B', 'r')):
            print(stringnode)
            # Leave out root (has no uptree node).
            if stringnode == "root":
                root = t.get_leaves_by_name("root")
            # Leave out the last mutant.
            elif 'mutant-9' in stringnode:
                pass
            else:
                allnodes.append(stringnode)
                # Find uptree node to add to alluptreenodes list.
                ancestors = node.get_ancestors()[1]
                print(ancestors)
                print(len(ancestors.children[0]))
                print(len(ancestors.children[1]))
                if len(ancestors.children[0]) == 1:
                    add_uptree_node(ancestors, 0)
                elif len(ancestors.children[1]) == 1:
                    add_uptree_node(ancestors, 1)
                elif len(ancestors.children[0]) == 2:
                    which_uptree(0)
                elif len(ancestors.children[1]) == 2:
                    which_uptree(1)
                # If none of the above, the uptree node must be root.
                else:
                    alluptreenodes.append(root[0])
    for i in range(18):  
        print(allnodes[i])
        print('and')
        #print(len(allnodes))
        print(alluptreenodes[i])
        print('\n')
        #print(len(alluptreenodes))

    print(allnodes)
    print(alluptreenodes)
    # Calculate the distance from node to the children of the most recent ancestor.
    #for i in range(len(allnodes)):
    #    node1 = alluptreenodes[i]
    #    node2 = allnodes[i]
    #    distance = node1.get_distance(node2)
    #    alldistances.append(distance)
    #print(alldistances)

    # Find the maximal distance to closest uptree node.
    #maximal = max(alldistances)
    #nameofmaximal = allnodes[alldistances.index(maximal)]
    #nameofuptreenode = str(alluptreenodes[alldistances.index(maximal)])[3:]
    #print('The maximal distance of a node to its uptree node is %f, for %s to %s.' %(maximal, nameofmaximal, nameofuptreenode))

# Call function maxbranchlength 
parser = ArgumentParser()
parser.add_argument('fname', nargs='+', action='append', metavar='FILE', help='Newick file to analyse.')
args = parser.parse_args()

filenames = args.fname
for filename in filenames[0]:
    maxbranchlength(filename)
    print('\n')
    