retrogenome
===========

## Install

Install blast from bioconda first
Install ab-blast for Advanced Bioinformatics 


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
  + num_threads X
  + outfmt 7
  
  
+ makeblastdb 
	+ -in
	+ -dbtype nucl/prot 
  
## ab-blast
+ xbformat 
	+ -n for nucle then "database"

+ tblastn*
	+ -topcomboN=20
	+ -hspsepsmax=# (A.thaliana 2000)
	+ -cpus=8
	+ -E 
	+ -mformat 2 maybe 3

```
ab-blast-20200317-linux-x64/tblastn* Code/retrogenome/Arabidopsis_thaliana.TAIR10.dna_sm.toplevel.fa Code/retrogenome/Arabidopsis_thaliana.proteins.fa  -topcomboN=20 -hspsepsmax=2000 -cpus=15 -E 1e-30 -mformat 3 & > tabbularab
```

What to look for 

High percentage identity
Noticeable gaps where introns should be 









