def get_overlap_region(a,b):

	d=sorted(a+b)		
	return d[1:3] \
			if d[-1]-d[0]  <= sum([i[1] - i[0] for i in [a,b]]) \
			else None
	
print(get_overlap_region([5,20],[3,20]))	

#求极小值
import math
import numpy as np
import matplotlib.pyplot as plt

step=0.03
t0=0.01

X=[]
Y=[]
for o in range(1,1000000):
	x=t0
	a=1-math.exp(-1*x)
	b=math.pow(a,x)
	c=math.log(a)
	d=math.exp(-1*x)*x
	y=b*(c+d/a)
	t=t0-step*y
	X.append(o)
	Y.append(t0)
	if abs(t - t0) < 0.0000000001:
		break
	
	t0=t
plt.plot(X,Y)
plt.show()	


#merge_overlap_region,return length of merge region
def run_pick(last_cor,now_cor):
    if last_cor[1] >= now_cor[1]:
        merge_cor = last_cor
    else:
        merge_cor = [last_cor[0],now_cor[1]]
    return merge_cor

def merge(a):
    data = []
    a = sorted(a,key=lambda x:x[0])
    last_cor = a[0]
    total_length = 0
    for i in range(len(a)):
        if last_cor[0]<= a[i][0] <= last_cor[1]:
            merge_cor = run_pick(last_cor,a[i])
            last_cor = merge_cor
        else:
            data.append(last_cor)
            last_cor = a[i]
        if i == len(a) - 1:
            data.append(last_cor)
    for region in data:
        total_length += region[1]-region[0]
    return total_length



print(merge([[1,10],[5,9],[9,18],[20,30]]))
