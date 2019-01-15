import sys

# this script define pn and ps as below:
# pn include variants_effect_missense_variant variants_effect_start_lost variants_effect_stop_gained and  variants_effect_stop_lost
# ps include variants_effect_synonymous_variant and  variants_effect_stop_retained_variant
# when calculate the ratio of pn/ps, if ps equal to zero, the ratio is define to  NA

VariantType={'Pn':['missense_variant','start_lost','stop_gained','stop_lost'],'Ps':['synonymous_variant','stop_retained_variant']}

def GeneRegion():
    GeneAnnFile=sys.argv[2]
    Gene={}
    
    with open(GeneAnnFile,'r') as f:
        for line in f:
            if 'ID=' in line:
                #GeneID=info[-1].split(';')[0].split('=')[1]
                info=line.strip().split()
                GeneID=info[-1].split(';')[0].split('=')[1]
                if info[0] in Gene:
                    Gene[info[0]][(int(info[3]),int(info[4]))]=GeneID
                    #Gene[info[1]][GeneID]=[int(info[3]),int(info[4])]
                else:
                    Gene[info[0]]={}
                    Gene[info[0]][(int(info[3]),int(info[4]))]=GeneID
                    #Gene[info[1]][GeneID]=[int(info[3]),int(info[4]))]

    return Gene

def ConfirmType(SnpEffInfo):
    Num={'Pn':0,'Ps':0}
    detail=SnpEffInfo.strip().split('|')
    for k in VariantType:
        for variant in VariantType[k]:
            if variant in detail[1]:
                Num[k]+=1
                break

    return [Num['Pn'],Num['Ps']]
              
def CheckOverLap(Line,GeneDict):

    GeneName=''
    info=Line.strip().split()
    if info[0] in GeneDict:
        for m in GeneDict[info[0]]:
            if int(info[1]) <= m[1] and int(info[1]) >= m[0]:
                GeneName=GeneDict[info[0]][m]

    return GeneName

def ReadSnpEff():
    SnpEffFile=sys.argv[1]

    GeneAnn=GeneRegion()
    GenePnPs={}
    with open(SnpEffFile,'r') as f:
        for line in f:
            GeneName=CheckOverLap(line,GeneAnn)
            if not '#' in line and GeneName and 'ANN' in line:
                NumPnPs=ConfirmType(line)
                if GeneName in GenePnPs:
                    GenePnPs[GeneName]['Pn']+=NumPnPs[0]
                    GenePnPs[GeneName]['Ps']+=NumPnPs[1]
                else:
                    GenePnPs[GeneName]={}
                    GenePnPs[GeneName]['Pn']=NumPnPs[0]
                    GenePnPs[GeneName]['Ps']=NumPnPs[1]
                
    for k in GenePnPs:
        print(k+'\t'+str(GenePnPs[k]['Pn'])+'\t'+str(GenePnPs[k]['Ps']))

ReadSnpEff()
