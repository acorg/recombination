What is the effect of recombination on ML trees?

## Install

You'll need `seqgen`:

```sh
$ pip install seqgen
```

Install [RAxML](https://github.com/amkozlov/raxml-ng). If on a mac with
[brew](https://brew.sh/) you can just run `brew install raxml-ng`.

Install [phyml](http://www.atgc-montpellier.fr/phyml/). If on a mac with
[brew](https://brew.sh/) you can just run `brew install phyml`.

## Plot recombinant tree data

One dataset (stored as out$i) contains trees generated from all json specification files, here different sequences are recombined.

`make` generates newick (with bootstrapvalues) and ascii files.

`make branchlength` plots bootstrap values against tip branchlengths for all trees in i datasets (i specified in `branchlength.sh`).

`make minimal_distance` plots bootstrap values against tip minimal distance to another tip for all trees in i datasets (i specified in `minimal_distance.sh`).

## Recombinantgradients

One dataset (stored as out$i) contains trees generated from the json specification files, here the recombinant is formed from to set sequences, but to varying percentages.

`make` generates newick (without bootstrapvalues for raxml-ng) and ascii files.

`../recombinant_gradient.py *raxml.newick > outtest` plots percentage of recombinant from one parent against the distance to it.
