ka,ma=map(int,input().split())
mka=list(map(int,input().split()))
l11=[]
for i in range(0,ma):
     aa,ba=map(int,input().split())
     l11.append([aa,ba])
for i in range(ma):
     lower=l11[i][0]
     upper=l11[i][1]
     xa=sum(mka[lower-1:upper])
     print(xa)
