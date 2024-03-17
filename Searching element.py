v=int(input())
size=int(input())
arr=list(map(int,input().split()))
arr.sort()
for i in range(len(arr)):
    if v==arr[i]:
        print(i)
