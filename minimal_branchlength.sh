for i in $(seq 5)
do
cd out$i
rm branchlengthplot/*
rmdir branchlengthplot
rm minimal_branchlength_$i
mkdir branchlengthplot
../minimal_branchlength.py *raxml.newick > minimal_branchlengths_$i
cd ..
done