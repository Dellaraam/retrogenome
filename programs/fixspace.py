import gzip
import sys


with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith(">"):
			line = line.replace(" ", "_")
		print(line, end="")

