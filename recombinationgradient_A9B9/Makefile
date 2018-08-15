OUTGROUP := root
OUTDIR := out

.PRECIOUS: $(OUTDIR)/%.fasta $(OUTDIR)/%.newick

JSON := $(wildcard *.json)

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
	test -d $(OUTDIR) || mkdir $(OUTDIR)

$(OUTDIR)/%.fasta : %.json
	seq-gen.py --specification $< > $@

$(OUTDIR)/%.phy: $(OUTDIR)/%.fasta
	fasta-to-phylip.py < $< > $@

$(OUTDIR)/%-phyml.newick: $(OUTDIR)/%.phy
	phyml -m GTR -q -i $< -o tlr -f m -v e --run_id xxxxx >/dev/null
	mv $(OUTDIR)/*_tree_xxxxx.txt $@
	rm -f $(OUTDIR)/*.phy_phyml_*_xxxxx*

$(OUTDIR)/%-raxml.newick: $(OUTDIR)/%.phy
	raxml-ng --msa $< --model GTR+G --prefix xxxxx --seed $$RANDOM --threads 1 >/dev/null 
	mv xxxxx.raxml.bestTree $@
	rm -f xxxxx.*

$(OUTDIR)/%.ascii: $(OUTDIR)/%.newick
	newick-to-ascii.py --outgroup $(OUTGROUP) < $< > $@

uptree_branchlength:
	uptree_branchlength.sh

minimal_branchlength:
	minimal_branchlength.sh

clean:
	rm -f $(ASCII) $(NEWICK) $(PHY) $(OUTDIR)/*xxxxx* xxxxx.*

clobber: clean
	rm -fr $(OUTDIR)
