n=int(input())
arr=list(map(int,input().split()))
a=sorted(arr) 
b=max(a)
ll=[]
for i in range(len(a)):
    if a[i]==b:
        ll.append(a[i])
print(len(ll))
