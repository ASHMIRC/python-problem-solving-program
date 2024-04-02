def mat(a,i,j):
    if i==j:
        return 0
    minval=float('inf')
    for k in range(i,j):
        count=(mat(a,i,k)+mat(a,k+1,j)+a[i-1]*a[k]*a[j])
        if count<minval:
            minval=count
        return minval
a=list(map(int,input().split()))
n=len(a)
print(mat(a,1,n-1))
