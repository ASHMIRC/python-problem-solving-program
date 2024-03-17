n = int(input().strip())
data = [input().strip() for i in range(n)]
data.sort(key = lambda x: (len(x), x))
for v in data:
     print(v)
