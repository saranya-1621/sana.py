chata=int(input())
chota=[int(o) for o in input().split(" ")]
cheta=0
for p in range(chata):
      for g in range(p):
           if(chota[g]<chota[p]):
                cheta+=chota[g]
print(cheta)
