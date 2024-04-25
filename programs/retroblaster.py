from subprocess import run
import argparse
import gzip
import sys


# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<path>', help='some file')

# optional arguments with default parameters
parser.add_argument('query', type=str, metavar='<path>')
parser.add_argument('database', type=str, metavar='<path>')
parser.add_argument('--hsp', required=False, type=str, default='2000')
parser.add_argument('--n', required=False, type=str, defualt='20')
parser.add_argument('--cpu', required=False, type=str, default='15')
parser.add_argument('--evalue', reqired=False, type=str, default='1e-30')
parser.add_argument('--mformat', required=False, type=str, default='3')



output = sys.argv[1]
alignnments = run(f'ab-blast-20200317-linux-x64/tblastn* {arg.query} {arg.database}  -topcomboN={arg.n} -hspsepsmax={arg.hsp} -cpus={arg.cpu} -E {arg.evalue} -mformat {arg.mformat} & > {output}')

zipg = run(f'gzip {output}')

with gzip.open(f'output'.gz, 'rt') as fp:
	for line in fp:
		if line.startswith(">"):
			line = line.replace(" ", "_")
		print(line, end="")

	
