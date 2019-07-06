n1 = int(input())
num1 = input().split()
for i in num1:
    if num1.count(i) == 1:
        print(i)
        break
