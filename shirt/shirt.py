import sys
import os
import PIL

exts = ['.jpg', '.jpeg', '.png']


if len(sys.argv) == 3:
    ext1 = os.path.splitext(sys.argv[1])[1].lower()
    ext2 = os.path.splitext(sys.argv[2])[1].lower()
    if ext1 in exts and ext2 in exts and ext1 == ext2:
        try:
            shirt = PIL.Image.open(sys.argv[1])
        except FileNotFoundError:
            sys.exit()
    else:
        sys.exit()
else:
    sys.exit()