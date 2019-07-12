intga=int(input())
numsa=list(map(int,input().split()))
o=0
for i in range(0,intga-2):
	for j in range(1,intga-1):
		for k in range(2,intga):
			if(numsa[i]<numsa[j] and numsa[j]<numsa[k]):
				o+=1
print(o)
