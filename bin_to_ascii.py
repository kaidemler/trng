from sys import argv
bin_data = open(argv[1]).read()
ascii = ''.join(chr(int(bin_data[i:i+8],2)) for i in xrange(0, len(bin_data),8))
print ascii
