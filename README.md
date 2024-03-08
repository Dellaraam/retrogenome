retrogenome
===========

## Install

Install blast from bioconda first


## Manifest

+ Arabidopsis_thaliana.TAIR10.dna_sm.toplevel.fa.gz
	+ downloaded from Ensembl not TAIR 2024-02-24
	+ Chromosome names: 1 2 3 4 5 Mt Pt
+ Arabidopsis_thaliana.proteins.fa.gz
	+ downloaded from BioMart 2024-02-24
	+ FASTA header is | delimited with the following fields
	+ Gene stable ID
	+ Transcript (works for Protein also) stable ID
	+ Gene symbol
	+ Strand (1, -1)
	+ CDS starts (semicolon delimited)
	+ CDS ends (semicolon delimited)
	

## blast

+ tblastn
 + input: -query 
 + library: -dp

+ other arguments 
  + evalue 1e-30
  + max_intron_length 9999
  + sorthits 3
  + sorthsps 2
  + num_threads X
  + outfmt 7
  
  
+ makeblastdb 
	+ -in
	+ -dbtype nucl/prot 
  
## ab-blast
+ ad-formatdb 
	+ -i
	+ -p T-protein F-nucl