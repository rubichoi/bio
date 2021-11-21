# -*- coding: cp949 -*-
import random

f = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.target.fasta",'r')
w = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.decoy.fasta",'w')

print "make a reverse decoy."

for line in f:
    if line[0] == ">":
        line = line[0] + "XXX_" + line[1:]
        w.write(line)
    else:
        line = line.rstrip("\n")
        w.write(line[::-1] + "\n")

print "END"        

f.close()
w.close()

