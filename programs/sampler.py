import random
import sys

filename = sys.argv[1]   # genome/gene_names.txt
genes = int(sys.argv[2]) # 801 good

names = []
with open(sys.argv[1]) as fp:
	for line in fp:
		names.append(line.rstrip())

random.shuffle(names)
for name in names[0:genes]:
	print(name)
