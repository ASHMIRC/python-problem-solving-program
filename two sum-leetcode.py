list1=list(map(int,input().split()))
target=9
n=len(list1)
for i in range(n-1):
  for j in range(i+1,n):
    if list1[i]+list1[j+1]==target:
      print([i j])
