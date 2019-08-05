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
