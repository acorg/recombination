OUTGROUP := root
OUTDIR := out

CORES := $(shell test $$(uname) = Linux && echo $$(nproc --all) || echo $$(sysctl -n hw.ncpu))

.PRECIOUS: $(OUTDIR)/%.fasta $(OUTDIR)/%.newick

JSON := $(wildcard *.json)

# PHY := $(JSON:.json=.phy)
# FASTA := $(JSON:.json=.fasta)
# PHYML_ASCII := $(JSON:.json=-phyml.ascii)
# RAXML_ASCII := $(JSON:.json=-raxml.ascii)
# PHYML_NEWICK := $(JSON:.json=-phyml.newick)
# RAXML_NEWICK := $(JSON:.json=-raxml.newick)

PHY := $(patsubst %.json, $(OUTDIR)/%.phy, $(JSON))
FASTA := $(patsubst %.json, $(OUTDIR)/%.fasta, $(JSON))
PHYML_ASCII := $(patsubst %.json, $(OUTDIR)/%-phyml.ascii, $(JSON))
RAXML_ASCII := $(patsubst %.json, $(OUTDIR)/%-raxml.ascii, $(JSON))
PHYML_NEWICK := $(patsubst %.json, $(OUTDIR)/%-phyml.newick, $(JSON))
RAXML_NEWICK := $(patsubst %.json, $(OUTDIR)/%-raxml.newick, $(JSON))

ASCII := $(PHYML_ASCII) $(RAXML_ASCII)
NEWICK := $(PHYML_NEWICK) $(RAXML_NEWICK)

all: $(OUTDIR) $(ASCII) $(NEWICK)

out:
	test -d out || mkdir out

$(OUTDIR)/%.fasta : %.json
	seq-gen.py --specification $< > $@

$(OUTDIR)/%.phy: $(OUTDIR)/%.fasta
	fasta-to-phylip.py < $< > $@

$(OUTDIR)/%-phyml.newick: $(OUTDIR)/%.phy
	phyml -m GTR -q -i $< -o tlr -f m -v e --run_id xxxxx >/dev/null
	mv $(OUTDIR)/*_tree_xxxxx.txt $@
	rm -f $(OUTDIR)/*.phy_phyml_*_xxxxx*

$(OUTDIR)/%-raxml.newick: $(OUTDIR)/%.phy
	raxmlHPC-PTHREADS -T $(CORES) -n xxxxx -m GTRCAT -s $< -p $$RANDOM >/dev/null
	mv RAxML_bestTree.xxxxx $@
	rm -f *.xxxxx

$(OUTDIR)/%.ascii: $(OUTDIR)/%.newick
	draw-tree-ascii.py --outgroup $(OUTGROUP) < $< > $@

clean:
	rm -f $(ASCII) $(NEWICK) $(PHY) $(OUTDIR)/*xxxxx* *.xxxxx

clobber: clean
	rm -fr $(OUTDIR)
