n1 = int(input())
num1 = list(map(int,input().split()))
temp1 = []
for i in range(n1):
    if num1[i] == i:
        temp1.append(num1[i])
if len(temp1) == 0:
    print(-1)
else:
    for i in sorted(temp1):
        print(i,end=' ')
