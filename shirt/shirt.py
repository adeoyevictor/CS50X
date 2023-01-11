import sys
import os

if len(sys.argv) == 3:
    ext1 = os.path.splitext(sys.argv[1])
    print(ext1)
else:
    sys.exit()