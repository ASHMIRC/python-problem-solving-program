string=input()
g=0
for i in range(len(string)):
    for j in range(i,len(string)):
        ans=string[i:j+1]
        if ans==ans[::-1]:
            c=len(ans)
            if c>g:
                a=ans
                g=c
print(a)
print(g)
