nna = int(input())
nmki = list(map(int,input().split()))
fina = []
for i in range(nlen(nmki)):
    if nmki.count(nmki[i]) > 1:
        if nmki[i] not in fina:
            fina.append(nmki[i])
fina.sort()
if nlen(fina)==0:
    print("unique")
else:
    print(" ".join([str(nelem) for nelem in fina]))   
