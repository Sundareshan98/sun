a=int(input())
a1=list(input().split())
l=[]
l1=[]
for i in range(0,len(a1)):
  n=a1.count(a1[i])
  if n>1:
    l.append(a1[i])
  else:
      continue
l=sorted(l)
for j in range(0,len(l)):
    if l[j] not in l1:
        l1.append(l[j])
if len(l1)>=1:
  print(*l1)
else:
  print("Unique")
    
    
