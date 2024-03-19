a,b=input("enter the ele: ").split()
l=[]
ll=[]
for i in range(int(a)):
    n=int(input("enter the values: "))
    l.append(n)
for j in range(int(b)):
    n1=int(input("enter the values: "))
    ll.append(n1)
print(*l)
print(*ll)
e=[]
ee=[]
for w in range(1,100):
    for j in l:
        if w%j==0:
            e.append(w)

print(e)
for k in range(1,100):
    for m in ll:
        if m%k==0:
            ee.append(k)
print(ee)
w=[]
ww=[]
for p in e:
    if p not in w:
        w.append(p)
print(w)

for o in ee:
    if o not in ww:
        ww.append(o)
print(ww)
q=[]
for t in ww:
    if t in w:
        q.append(t)
print(len(q))
