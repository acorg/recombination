for i in $(seq 5)
do
cd out$i
../uptree_branchlength.py *raxml.newick > calculated_branchlengths_$i
cd ..
done