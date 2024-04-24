n=int(input())
for i in range(n):
    n1=int(input())
    for j in range(n1):
        list1=list(map(int,input().split()))
        a=sorted(list1,reverse=True)
        print(a)
        b=0
        for k in range(len(a)):
            b+=2**k * a[k]
        print(b)
