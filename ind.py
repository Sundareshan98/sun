a,b=list(map(int,input().split()))
a1=list(map(int,input().split()))
l=[]
for i in range(0,b):
    c1,c2=list(map(int,input().split()))
    s=0
    if c1==1:
        for i in range(0,c2):
            s+=a1[i]
        l.append(s)
    else:
        for i in range(c1-1,c2):
            s+=a1[i]
        l.append(s)
for i in l:
    print(i)

    
    
    
