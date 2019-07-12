km122=int(input())
km212=[]
guvi=0
for h in range (0,km122+1):
    guvi=abs((2**h)-km122)
    km212.append(guvi)
stn=min(km212)
print(stn)
