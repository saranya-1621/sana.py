cho2,sawa2=map(int,input().split())
lost2=list(map(int,input().split()))
law2=[]
for p in range(0,sawa2):
     sha2,she2=map(int,input().split())
     law2.append([sha2,she2])
for p in range(sawa2):
     las2=law2[p][0]
     upo2=law2[p][1]
     yaw2=sum(lost2[last2-1:upo2])
     print(yaw2)
