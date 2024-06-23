import sys 
import  gzip

retrolist = {}
parentlist = {}

with open(sys.argv[1]) as fp:
	for line1 in fp:
		l = line1.split()
		retrogene = l[0]
		parent = l[1]
		#print(retrogene)
		retrolist[retrogene] = True
		parentlist[parent] = True	

f1 = open("retro_introns.fa", "w")
f2 = open("parent_introns.fa", "w")

with gzip.open(sys.argv[2], "rt") as fp2:
	for line2 in fp2:
		l2 = line2.split()
		g = l2[0].split(".")
		gene = g[0]
		read = g[1]
		start = l2[1]
		end = l2[2]
		intron = l2[5]
		#print(gene)
		if read != "1": continue 
		for retro in retrolist.keys():
			if gene == retro:
				f1.write(f'>{gene}.{read} {start}-{end}\n')
				f1.write(f'{intron}\n')
		for parent in parentlist.keys():
			if gene == parent:
				f2.write(f'>{gene}.{read} {start}-{end}\n')
				f2.write(f'{intron}\n')
	
		
#print(retrolist, parentlist)
	
		
#-W 7 -Q 3 -R 1 -M 1 -N -1
