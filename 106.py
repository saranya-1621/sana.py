m1,m2=map(int,input().split())
alis=input().split()
l2=[]
for i in alis:
  if int(i)%2!=0:
    l2.append(i)
print(l2[m2-1])
