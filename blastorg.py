import gzip
import sys
import json

def get_exons_from_defline(line):
	gid, tid, name, strand, chrom, begstr, endstr = line.split('|')
	begs = [int(coor) for coor in begstr.split(';')]
	ends = [int(coor) for coor in endstr.split(';')]
	begs.sort()
	ends.sort()
	gexons = [(beg, end) for beg, end in zip(begs, ends)]
	pexons = []
	gbeg = gexons[0][0]
	gend = gexons[-1][1]
	cumlen = 0
	for beg, end in gexons:
		pbeg = (beg - gbeg) // 3 + 1
		pend = (end - gbeg) // 3 + 1
		plen = pend - pbeg + 1
		pexons.append( (cumlen+1, cumlen + plen+1) )
		cumlen += plen
	if strand == '-1':
		mexons = []
		pmax = pexons[-1][1]
		for beg, end in pexons:
			mexons.append( (pmax-end+1, pmax-beg+1) )
		pexons = mexons
	return gexons, pexons

def overlap(b1, e1, b2, e2):
	beg = max(b1, b2)
	end = min(e1, e2)
	if end > beg: return end - beg + 1
	return 0


def gcompare(exons, aligns):
	total_exp = 0
	total_obs = 0
	for beg, end in exons:
		elen = end - beg + 1
		total_exp += elen

		#find the best matching alignment to this exon
		maxover = 0
		for qb, qe, sb, se, st, s, e, pct in aligns:
			if st == '-': sb, se = se, sb
			x = overlap(beg, end, sb, se)
			if x > maxover: maxover = x
		total_obs += maxover
	return total_exp, total_obs

def pcompare(exons, aligns):
	total_exp = 0
	total_obs = 0
	for beg, end in exons:
		elen = end - beg + 1
		total_exp += elen

		#find the best matching alignment to this exon
		maxover = 0
		for qb, qe, sb, se, st, s, e, pct in aligns:
			x = overlap(beg, end, qb, qe)
			if x > maxover: maxover = x
		total_obs += maxover
	return total_exp, total_obs

search = {}
with open(sys.argv[1]) as fp:
	for line in fp:
		if line.startswith('#'): continue
		if line.startswith('WARNING'): continue
		qid, sid, e, n, s1, s, alen, ni, np, ns, pct, ppos, qgn, qgl, sgn,\
			sgl, qf, qb, qe, sf, sb, se, grp = line.rstrip().split('\t')
		sid = f'Chr{sid}'
		if qid not in search: search[qid] = {}
		if sid not in search[qid]: search[qid][sid] = {}
		if grp not in search[qid][sid]: search[qid][sid][grp] = []
		align = (int(qb), int(qe), int(sb), int(se), sf[0], float(s),\
			float(e), float(pct))
		search[qid][sid][grp].append(align)

for qid in search:
	print(qid[:25])
	f = qid.split('|') # remove later
	if len(f) != 7: continue # remove later
	gexons, pexons = get_exons_from_defline(qid)

	for sid in search[qid]:
		print('\tsid', sid)
		for grp in search[qid][sid]:
			print('\t\tgroup', grp, len(search[qid][sid][grp]))
			x, y = gcompare(gexons, search[qid][sid][grp])
			print('\t\t\t',x, y, y/x, sb, se)
			x, y = pcompare(pexons, search[qid][sid][grp])
			print('\t\t\t', x, y, y/x, qb, qe)
			
# Chromosome: " "		
	# Group: " " 
		# Alignments: " " 
		# PercentId: " "
			# Beg 
			# End  

# original has high alignments 
# targets have notable decreases in alignments 
# look for genes with multiple groups 
# look for genes that have matches in multiple chromosomes
# find enough of the protein glue all the alignments together in a group(How long is that? NOT TO SHORT)
# make coordinates Chr3:2345..6789















