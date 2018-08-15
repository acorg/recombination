for i in $(seq 5)
do
cd out$i
mkdir minimal_distanceplot
../minimal_distance.py *raxml.newick > minimal_distance_$i
cd ..
done