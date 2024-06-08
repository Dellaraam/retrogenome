import sys

with open(sys.argv[1]) as fp:
	for line in fp:
		l = line.split()
		retrogene = l[0]
		parent = l[1] 
		retro_introns = l[2]
		parent_introns = l[3]
		different = l[4]
		#print(retrogene)
		if retro_introns == "pseudogene" or retro_introns == "0": continue
		if different == "NA": continue
		print(retrogene, parent)