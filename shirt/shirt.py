import sys
import os
from PIL import Image, ImageOps

exts = ['.jpg', '.jpeg', '.png']

if len(sys.argv) == 3:
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    if ext1 in exts and ext2 in exts and ext1 == ext2:
        try:
            overlay = Image.open("shirt.png")
            size = overlay.size
            shirt = Image.open(sys.argv[1])
            shirt = ImageOps.fit(shirt, size)
            shirt.paste(overlay, overlay)

            shirt.save(sys.argv[2])
        except FileNotFoundError:
            sys.exit("Invalid CL Arguments")
    else:
        sys.exit("Invalid CL Arguments")
else:
    sys.exit("Invalid CL Arguments")