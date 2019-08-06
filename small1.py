n,m=list(map(int,input().split()))
l=list(map(int,input().split()))
for i in range(m):
    c,d=list(map(int,input().split()))
    print(min(l[c-1:d]))
