import sys
import random
import numpy as np

File1=sys.argv[1]

Species=[]
Seq=[]
with open(File1,'r') as f:
	header=f.readline()
	for line in f:
		info=line.strip().split()
		Species.append(info[0])
		Seq.append(list(info[1]))
		
SeqLen=int(header.strip().split()[1])
SampleColumn=sorted(random.sample(range(0,SeqLen),int(SeqLen*2/3)))
SeqArray=np.array(Seq)
SeqSample=SeqArray[:,SampleColumn]
NewSeq=[]
for i in SeqSample.tolist():
	NewSeq.append(''.join(i))
NewSeqLen=len(NewSeq[0])
print(len(Species),end='\t')
print(NewSeqLen)
for i in range(len(Species)):
	print(Species[i],end='\t')
	print(NewSeq[i])
