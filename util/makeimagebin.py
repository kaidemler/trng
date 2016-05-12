from PIL import Image
import png
import ImageDraw
import sys
infile = str(sys.argv[1])
outfile = str(sys.argv[2])
f = open(infile, "r")
im = Image.new("RGB", (128,128), "black")
draw = ImageDraw.Draw(im)
for x in range(0,16):
	for y in range(0,128):
		bro = f.read(1)
		if bro:
			b = bin(ord(bro))[2:]
			b = '0'*(8-len(b)) +b
		else:
			b = '0'*8
		print b
		if b[0] == "1":
			xy = (8*x,y)
			draw.point(xy)
		if b[1] == "1":
			xy = (8*x+1,y)
			draw.point(xy)
		if b[2] == "1":
			xy = (8*x+2,y)
			draw.point(xy)
		if b[3] == "1":
			xy = (8*x+3,y)
			draw.point(xy)
		if b[4] == "1":
			xy = (8*x+4,y)
			draw.point(xy)
		if b[5] == "1":
			xy = (8*x+5,y)
			draw.point(xy)
		if b[6] == "1":
			xy = (8*x+6,y)
			draw.point(xy)
		if b[7] == "1":
			xy = (8*x+7,y)
			draw.point(xy)
g = open(outfile, "w")
im.save(outfile)
f.close()
g.close()
		
