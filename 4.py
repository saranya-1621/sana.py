N2=int(input())
n1=list(map(int,input().split()))
for k1 in range(len(n1)):
    if n1.count(n1[k1])==1:
        print(n1[k1])
