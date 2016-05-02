from PIL import Image
import png
import ImageDraw
import sys
infile = str(sys.argv[1])
outfile = str(sys.argv[2])
f = open(infile, "r")
im = Image.new("RGB", (128,128), "black")
draw = ImageDraw.Draw(im)
for x in range(0,128):
	for y in range(0,128):
		if f.read(1) == "1":
			xy = (x,y)
			draw.point(xy)
g = open(outfile, "w")
im.save(outfile)
f.close()
g.close()
		
