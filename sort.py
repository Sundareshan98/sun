a=int(input())
s1=[]
for i in range(0,a):
    a=list(map(int,input().split()))
    for j in range(0,len(a)):
        s1.append(a[j])
s=sorted(s1)
print(*s)
