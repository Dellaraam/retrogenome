import sys

def proc_chunk(chunk):
	# the longest protein is the "match"
	pmax = 0
	hspn = None
	for gid, gpct, ppct, plen, hsps, loc in chunk:
		if gpct > 0.9 and plen > pmax:
			pmax = plen
			hspn = hsps
	if pmax == 0: return

	# need to collapse redundant locations...
	keep = []
	for gid, gpct, ppct, plen, hsps, loc in chunk:
		prel = plen/pmax
		if gpct == 0 and ppct > 0.8 and prel > 0.8 and hspn > 2 and hsps == 1:
			print(f'{gid} {ppct} {prel:.3f} {hspn} {hsps} {loc}')


with open(sys.argv[1]) as fp:
	chunk = []
	for line in fp:
		if len(line) < 5:
			proc_chunk(chunk)
			chunk = []
		else:
			gid, tid, gpct, ppct, plen, hsps, loc = line.split()
			gpct = float(gpct)
			ppct = float(ppct)
			plen = float(plen)
			hsps = int(hsps)
			chunk.append( (gid, gpct, ppct, plen, hsps, loc) )
	proc_chunk(chunk)




# gid, tid, gpct, ppct, plen, hsps, loc
