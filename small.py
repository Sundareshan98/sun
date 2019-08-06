a=list(map(int,input().split()))
a1=a[0]
a2=a[1]
b=list(input().split())
l2=[]
for i in range(0,a2):
    c=list(map(int,input().split()))
    c1=c[0]
    c2=c[1]
    l=[]
    for j in range(c1-1,c2):
        l.append(b[j])
    n=min(l)
    l2.append(n)
for i in range(0,len(l2)):
    print("".join(l2[i]))
