am,an=map(int,input().split())
list=input().split()
alg=[]
for i in list:
  if (int(i)%2!=0):
    alg.append(i)
print(alg[n-1])
