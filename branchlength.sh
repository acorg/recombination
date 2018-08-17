for i in $(seq 5)
do
cd out$i
mkdir branchlengthplot
../branchlength.py *raxml.newick > branchlength_$i
cd ..
done