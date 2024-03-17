def miniMaxSum(arr):
    mini=sum(sorted(arr)[:4])
    maxi=sum(sorted(arr)[-4:])
    return ('{} {}'.format(mini,maxi))

arr = list(map(int, input().rstrip().split()))

print(miniMaxSum(arr))
