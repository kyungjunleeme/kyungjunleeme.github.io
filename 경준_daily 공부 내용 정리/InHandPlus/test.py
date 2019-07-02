from PIL import Image, ImageDraw
import sys

im = Image.open("D:\\0619_data_완료\\tl_0001_0001_20190619_051738.jpg")

draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
# draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw

# write to stdout
im.save(sys.stdout, "PNG")