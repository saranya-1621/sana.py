num1=int(input())
s1=list(map(int,input().split()))[:num1]
s1.sort(reverse=True)
print(*s1,sep="")
