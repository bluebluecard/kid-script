# this script is designed to find the overlaping region between input file,
# which format like gff

a=[[1,4],[7,13],[2,50],[9,30],[22,100],[34,78],[55,76],[3,90],[7,15]]
b=[[5,9],[-1,5],[6,13],[8,15],[3,9],[6,9],[2,8],[2,5],[9,77],[4,90]]

asort=sorted(a,key=lambda x:x[0])
bsort=sorted(b,key=lambda x:x[1])

LastStart=0
count=0
for i in range(len(asort)):
	status=0
	for j in range(LastStart,len(bsort)):
		count+=1
		length_i=asort[i][1]-asort[i][0]
		length_j=bsort[j][1]-bsort[j][0]

		if asort[i][0] <= bsort[j][0]:
			Bewteen=bsort[j][1]-asort[i][0]
		else:
			Bewteen=asort[i][1]-bsort[j][0]

		if length_i+length_j > Bewteen:
			print(asort[i],bsort[j])
			if status==0:
				LastStart=j
				status=1

		if asort[i][0] > bsort[j][1]:
			break
