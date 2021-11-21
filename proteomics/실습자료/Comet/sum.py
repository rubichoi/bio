
f1 = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.target.fasta",'r')
f2 = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.decoy.fasta",'r')
f3 = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.decoy.2.fasta",'r')
w1 = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.TD.fasta",'w')
w2 = open("C:/inetpub/wwwroot/ISB/data/Comet/swissprot.revCat.TD.2.fasta",'w')

print "start"

for line in f1:
    w1.write(line)
    w2.write(line)

for line in f2:
    w1.write(line)

for line in f3:
    w2.write(line)

print "end"

f1.close()
f2.close()
f3.close()
w1.close()
w2.close()


