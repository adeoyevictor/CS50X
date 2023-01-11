import sys
import os

if len(sys.argv) == 3:
    ext1 = os.path.splitext(sys.argv[1])[1]
    ext2 = os.path.splitext(sys.argv[2])[1]
    
    print(ext1, ext2)
else:
    sys.exit()