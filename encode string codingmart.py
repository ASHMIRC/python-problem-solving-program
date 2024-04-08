str='CODINGMART TECHNOLOGIES'
n=4
a=1
for i in range(n):
    for j in range(i,len(str),n):
        print(str[j],end='')
    if i!=n-1:
        print(a*'*',end='')
        a+=1
