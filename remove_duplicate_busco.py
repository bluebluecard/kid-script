import sys

filePath = sys.argv[1]

data = {}

with open(filePath,'r') as f:
    for line in f:
        if "EOG" in line:
            info = line.strip().split()
            if info[0] in data:
                data[info[0]].append(line.strip())
            else:
                data[info[0]]=[]
                data[info[0]].append(line.strip())

lenPath = sys.argv[2]
lenDict = {}
with open(lenPath,'r') as f:
    for line in f:
        info = line.strip().split()
        lenDict[info[0]]=int(info[1])

for i in data:
    if len(data[i]) > 1:
        dupLen = [ abs(int(j.strip().split('\t')[-1]) - lenDict[i]) for j in data[i]]
        targetList = [ k for k,d in enumerate(dupLen) if d == min(dupLen)]
        if len(targetList) > 1:
            score = [float(data[i][t].split('\t')[-2]) for t in targetList]
            target = targetList[score.index(max(score))]
        else:
            target = targetList[0]
        print(data[i][target])
    else:
        print(data[i][0])
