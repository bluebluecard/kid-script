import sys

CdsFile=sys.argv[1]
GffFile=sys.argv[2]

code='/hwfssz5/ST_DIVERSITY/P18Z10200N0197_Drosophila/USER/chenjiawei/01.drosophila/15.CdsPrank/work/ScriptPy/mcdonald_kreitman_test/new.code.txt'

with open(code,'r') as f:
    GeneticCode={}
    for line in f:
        info=line.strip().split()
        GeneticCode[info[1]]=info[0]

def ReadGff():
    gff={}
    with open(GffFile,'r') as f:
        for line in f:
            info=line.strip().split()
            if info[2] == 'CDS' :
                gene=info[-1].strip('Parent=').strip(';')
                if gene in gff :
                    gff[gene].append([int(info[3]),int(info[4])])
                else:
                    gff[gene]=[]
                    gff[gene].append([int(info[3]),int(info[4])]) 
    return gff

def ReadScaf():
    
    Scaf={}
    with open(GffFile,'r') as f:
        for line in f:
            info=line.strip().split()
            if info[2] == 'CDS' :
                gene=info[-1].strip('Parent=').strip(';')
                #if gene in gff :
                #    gff[gene].append([int(info[3]),int(info[4])])
                #else:
                #    gff[gene]=[]
                #    gff[gene].append([int(info[3]),int(info[4])])
                Scaf[gene]=info[0]
    return Scaf


def ReadStrand():

    Strand={}
    with open(GffFile,'r') as f:
        for line in f:
            info=line.strip().split()
            if info[2] == 'CDS' :
                gene=info[-1].strip('Parent=').strip(';')
                Strand[gene]=info[6]

    return Strand
                    

def ReadCDS():

    Seq={}
    with open(CdsFile,'r') as f:
        for line in f:
            if '>' in line:
                info=line.strip().split()
                gene=info[0].strip('>') 
                Seq[gene]=''
            else:
                Seq[gene]+=line.strip().upper()
    return Seq

def Point2Point(seq,interval,strand):
    
    a=list(range(len(seq)))
    b=[]
    c={}
    for i in interval:
        if strand == '+':
            for j in list(range(i[0],i[1]+1,1)):
                b.append(j)
        else:
            for j in list(range(i[0],i[1]+1,1))[::-1]:
                b.append(j)

    for i in range(len(a)):
        #c.append([a[i],b[i]])        
        c[a[i]]=b[i]
    return c


def SiteType(codon,position):

    alternative=['A','G','C','T']
    temp=[]
    for i in alternative:
        NewSym=i+codon[1]+codon[2]
        temp.append(GeneticCode[NewSym])
    if len(set(temp)) == 1 :
        onetype='4d'
    elif len(set(temp)) == 2 or len(set(temp)) == 3:
        onetype='2d'
    elif len(set(temp)) == 4 :
        onetype='0d'
    temp=[]
    for i in alternative:
        NewSym=codon[0]+i+codon[2]
        temp.append(GeneticCode[NewSym])
    if len(set(temp)) == 1 :
        twotype='4d'
    elif len(set(temp)) == 2 or len(set(temp)) == 3:
        twotype='2d'
    elif len(set(temp)) == 4 :
        twotype='0d'
    temp=[]
    for i in alternative:
        NewSym=codon[0]+codon[1]+codon[2]
        temp.append(GeneticCode[NewSym])
    if len(set(temp)) == 1 :
        threetype='4d'
    elif len(set(temp)) == 2 or len(set(temp)) == 3:
        threetype='2d'
    elif len(set(temp)) == 4 :
        threetype='0d'

    return [[onetype,position],[twotype,position+1],[threetype,position+2]]

def GetCodon(seq):
    a=[]
    degenerate={}
    for i in range(0,len(seq),3):
        codon=seq[i:i+3]
        if not 'N' in codon:
            for m in SiteType(codon,i):
                degenerate[m[1]]=m[0]
                #a.append(m)
    #print(a)
    return degenerate

def main():

    Seq=ReadCDS()
    gff=ReadGff()
    Strand=ReadStrand()
    Scaf=ReadScaf()
    for i in Seq:
        if len(Seq[i])%3 == 0:
            MatchPoint=Point2Point(Seq[i],gff[i],Strand[i])    
            a=GetCodon(Seq[i]) 
            for j in a.keys():
                if j in MatchPoint :
                    print(i+'\t'+str(j)+'\t'+Scaf[i]+'\t'+str(MatchPoint[j])+'\t'+a[j])                    
main()
