a,b=map(int,input().split())
m,n=map(int,input().split())
apples=list(map(int,input().split()))
oranges=list(map(int,input().split()))
aa=[]
ora=[]
la=[]
lo=[]

for i in apples:
    o=a+i
    aa.append(o)
for j in oranges:
    oo=b+j
    ora.append(oo)
for k in aa:
    if k>=s and k<=t:
        la.append(k)
for m in ora:
    if m<=t and m>=s:
        lo.append(m)
print(len(la))
print(len(lo))

