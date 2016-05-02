import random
import sys
outfile = str(sys.argv[1])
f = open(outfile, 'w')
for x in range(0,16384):
	f.write(str(random.randint(0,1)))
f.close

