import sys


#using genome locations to find the exon coordinates 
#

with open(sys.argv[1]) as fp:
	for line in fp:
		if line.startswith("#"): continue
		tokens = line.split("\t")
		t = tokens[0].split("|")
		if len(t) < 5: continue
		chromo = t[4]
		starts = [int(s) for s in t[5].split(";")]
		ends = [int(e) for e in t[6].split(";")]
		print(sorted(starts),sorted(ends))
			