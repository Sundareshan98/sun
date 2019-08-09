l=list(input())
a=""
for i in range(0,len(l)):
    a+=l[i]
a1=int(a)
if l[0]=='-':
  print("invalid")
elif a1%2==0:
    print("Even")
else:
    print("Odd")
