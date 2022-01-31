# TODO
# improve the CIGAR string interpretation part for better meanings

import re
import sys, os
f = open(sys.argv[1],'r')
out = open(sys.argv[2],'w')
for line in f:
    ele = line.split()
    t = re.findall('(\d+|[A-Za-z]+)',ele[1])
    now = ele[2][int(t[0]):-int(t[-2])]
    print("> "+ele[0],file=out)
    print(now, file=out)

f.close()
out.close()