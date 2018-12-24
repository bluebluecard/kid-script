import sys
import os
import subprocess as sbp
from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

ape=importr('ape')
base=importr('base')
stats=importr('stats')

FilePath=sys.argv[1]
FileNiche='/ldfssz1/ST_DIVERSITY/UNKNOWN_PROJECT/USER/chenjiawei/0.drosophila/04.call_snp/14.GeneAlign/work/mean_temp.txt'
treedoctor='/hwfssz1/ST_DIVERSITY/PUB/USER/bixupeng/software/phast/bin/tree_doctor'
treefile="/hwfssz1/ST_DIVERSITY/F17ZQSB1SY3059_sand_rat/USER/lifang1/ifs5/lifang1/drosophila_denovo/08.analysis/25.Element/07.STUBB/03.stubb/divtree.newick"

NicheSpe=['bipectinata','immigrans','kikkawai','pseudoananassae','sulfurigaster','simulans','birchii','pseudotakahashii','serrata','jambulina','rubida','bunnanda','setifemur','ironensis']

DataPi={}
with open(FilePath,'r') as f:
    next(f)
    count=1
    for line in f:
        info=line.strip().split()
        for i in range(len(NicheSpe)):
            if not info[i+1] == 'NA' :
                if count in DataPi:
                    DataPi[count][NicheSpe[i]]=float(info[i+1])
                else:
                    DataPi[count]={}
                    DataPi[count][NicheSpe[i]]=float(info[i+1])
        count+=1

DataNiche={}
with open(FileNiche,'r') as f:
    for line in f:
        info=line.strip().split()
        DataNiche[info[0]]=float(info[1])


for count in DataPi:
    if len(DataPi[count]) >= 10:

        SpeInData=[]
        PiInData=[]
        NicheInData=[]
        for i in DataPi[count]:
            SpeInData.append(i)
            PiInData.append(DataPi[count][i])

        command=treedoctor+' --prune-all-but '+','.join(SpeInData)+' --newick '+treefile
        temptree_byte=sbp.check_output(command,shell='TRUE')
        temptree=str(temptree_byte,'utf-8').strip()
        k_tree=ape.read_tree(text=temptree)

        for i in SpeInData:
            NicheInData.append(DataNiche[i])

        Pi_m = robjects.r.matrix(robjects.FloatVector(PiInData), ncol=1)
        Niche_m=robjects.r.matrix(robjects.FloatVector(NicheInData), ncol=1)


        Pi_m.rownames = robjects.StrVector(SpeInData)
        Niche_m.rownames = robjects.StrVector(SpeInData)
        Pi_m.colnames = robjects.StrVector(['Pi'])
        Niche_m.colnames = robjects.StrVector(['Ni'])

        Pi_pic=base.apply(Pi_m,2,ape.pic,k_tree)
        Niche_pic=base.apply(Niche_m,2,ape.pic,k_tree)
        res=stats.cor_test(Pi_pic.rx(True,1),Niche_pic.rx(True,1))
        word=str(count)+'\t'+str(res.rx2('estimate')[0])+"\t"+str(res.rx2('p.value')[0])
        print(word)
