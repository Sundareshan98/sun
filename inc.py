a1=int(input())
l=list(map(int,input().split())
       )
s=0
c=0
a=0
for i in range(0,a1):
    b=l[i]
    if a<(b):
        s+=1
        c+=s
        a=b
    else:
        s=1
        c+=s
        a=l[i]
print(c)
        
        
