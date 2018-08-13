# CHANGELOG

## 10.07.18

Adapted Makefile to call raxml-ng instead of raxml.

## 09.08.18

Adapted Makefile to call raxml-ng with `-all` to include bootstrap analysis.

## 10.08.18

Added script `minimal_branchlength.py` that calculates minimal branchlength and related bootstrap 
values for each leaf and plots these. `minimal_branchlength.sh` is a bash script that calls it the
python script a specified number of times to analyse newick files stored in out$number directories.
`Make minimal_branchlength` calls the bash script.

## 11.08.18

Added script `uptree_branchlength.py` that calculates the branchlength to the uptree neighbour and related bootstrap values for each leaf and plots these. `uptree_branchlength.sh` is a bash script that calls it the
python script a specified number of times to analyse newick files stored in out$number directories.
`Make uptree_branchlength` calls the bash script.