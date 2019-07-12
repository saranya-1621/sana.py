import math
cho,cha=map(int,input().split())
ohoa=[]
gaao=list(map(int,input().split()))
for p in range(0,cha):
    loe,hut=map(int,input().split())
    ohoa.append([loe,hut])
for p in ohoa:
    kaaa=p[0]-1
    laaa=p[1]-1
    print(math.gcd(gaao[kaaa],gaao[laaa]))
