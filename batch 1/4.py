import sys
from os.path import exists

f1 = sys.argv[1]
f2 = sys.argv[2]

if exists(f1) and exists(f2):
    f1 = open(f1, 'r')
    f2 = open(f2, 'a')
    lines = f1.readlines()
    print(lines)
    for line_no, line in enumerate(lines):
        line = line.rstrip('\n')
        f2.write(f"{line_no}\t{line}\t{len(line)}\n")
    f1.close()
    f2.close()
    
