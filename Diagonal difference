def diagonalDifference(arr):
    n=len(arr)
    l2r=0
    r2l=0
    for i in range(n):
        l2r+=arr[i][i]
        r2l+=arr[i][n-i-1]
    return abs(l2r-r2l)
