import PIL, sys
from PIL import Image

img_name = sys.argv[1]
pdf_name = sys.argv[2]

img = PIL.Image.open(img_name)

img.save(pdf_name, "PDF", quality = 100)
