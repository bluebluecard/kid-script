def get_overlap_region(a,b):

	d=sorted(a+b)		
	return d[1:3] \
			if d[-1]-d[0]  <= sum([i[1] - i[0] for i in [a,b]]) \
			else None
	
print(get_overlap_region([5,20],[3,20]))	
