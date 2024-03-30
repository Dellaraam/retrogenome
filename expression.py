
import argparse
import sys
import grimoire.genome

#from grimoire.sequence import DNA
#from grimoire.feature import Feature, mRNA, Gene, FeatureTable
#from grimoire.genome import Reader
#import grimoire.io as gio

## Command line stuff ##

parser = argparse.ArgumentParser(
	description='Get expression level for genes.')
parser.add_argument('fasta', type=str, metavar='<fasta>',
	help='path to input fasta file')
parser.add_argument('gff', type=str, metavar='<gff>',
	help='path to input GFF3 (or similar) file')
arg = parser.parse_args()

for chrom in grimoire.genome.Reader(fasta=arg.fasta, gff=arg.gff):

	# get the counts of every intron
	intron_count = {}
	for f in chrom.ftable.features:
		if f.source == 'RNASeq_splice':
			loc = (f.beg, f.end, f.strand)
			if loc not in intron_count: intron_count[loc] = 0
			intron_count[loc] += f.score

	# get expression for every gene
	for gene in chrom.ftable.build_genes():
		sizes = []
		for tx in gene.transcripts():
			for f in tx.introns:
				loc = (f.beg, f.end, f.strand)
				if loc in intron_count: sizes.append(intron_count[loc])
		if len(sizes) == 0: n = 0
		else:               n = max(sizes)
		if gene.is_coding(): cds = 'coding'
		else:                cds = 'non-coding'
		print(gene.id, int(n), cds, sep='\t')
