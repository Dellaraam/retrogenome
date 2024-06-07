import sys



with open(sys.argv[1]) as fp1:
	#candadites = []
	for line in fp1:
		l1 = line.split()
		candadite = l1[0]
		#candadites.append(candadite)
		with open(sys.argv[2]) as fp2:
			for line2 in fp2:
				l = line2.split()
				retrogene = l[0]
				parent = l[1] 
				retro_introns = l[2]
				parent_introns = l[3]
				different = l[4]
				#print(retrogene)
				if retro_introns == "pseudogene" or different == "NA": continue
				if candadite == retrogene:
					print(candadite, retrogene)
	
			
		