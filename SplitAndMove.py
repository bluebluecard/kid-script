import threading
import time
import sys
import shutil
import os

DepthFile=sys.argv[1]

Library=os.path.basename(DepthFile).split('.')[0]

def SplitScaf(Path,Lib):
    count=1
    with open(Path,'r') as f:
        LastScaf=0
        for line in f:
            info=line.strip().split()
            if LastScaf ==0:
                LastScaf=info[0]
            NowScaf=info[0]
            if not LastScaf == NowScaf:
                count+=1
            with open(str(count)+'_'+Lib+'_'+info[0]+'.txt','a+') as fo:
                fo.write(line)

            LastScaf=NowScaf

def MoveScaf(Lib):
    a=[]
    for i in os.listdir('./'):
        if i.endswith('txt') and Lib in i:
            a.append(i)
    b=sorted(a,key=lambda x:int(x.split('_')[0]))
    print(b)
    for i in range(0,len(b)-1):
        fd=int(int(b[i].split('_')[0])/1000)
        sd=int(int(b[i].split('_')[0])/100)
        tp=str(fd)+'/'+str(sd)
        if os.path.exists(tp):
            name=b[i]
            shutil.move(name,tp)
        else:
            os.makedirs(tp)
            name=b[i]
            shutil.move(name,tp)


def t2(Lib):
    while 1:
        MoveScaf(Lib)
        time.sleep(0.5)


if __name__ == '__main__':
    T1 = threading.Thread(target=t2,args=(Library,))
    T2 = threading.Thread(target=SplitScaf,args=(DepthFile,Library,))
    T1.start()
    T2.start()
    T2.join()
