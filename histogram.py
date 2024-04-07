list1=list(map(int,input("enter the list: ").split()))
ans=max(list1)
ans1=[]

for i in range(len(list1)):
    if list1[i]==ans :
        if i>0:
            ans1.append(list1[i-1])
        if i<len(list1)-1:
            ans1.append(list1[i+1])
print((ans1))
x=2
if len(ans1)>1:
    a=(max(ans1))
    print(a*2)
elif len(ans1)==1:
    b=ans1
    print(b)
    for i in b:
        c=i*2
        print(c)
else:
    print('no values found')
