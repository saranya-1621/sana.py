p2=input()
t2=input()
for i in range(len(p2)):
    n2=ord(p2[i])
    r2=ord(t2[i])
    l2=((n2-96)+(r2-96))
    if(l1 > 26)and(l1%26!=0):
        l2=(((n2-96)+(r2-96))%26)+96
        print(chr(l2),end='')
    elif(l2%26==0):
        l2=122
        print(chr(l2),end='')
    else:
        l2=(((n2-96)+(r2-96))+96)
        print(chr(l2),end='')
