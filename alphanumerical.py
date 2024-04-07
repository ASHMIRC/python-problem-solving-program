vowel=['A','E','I','O','U']
str='AGK1LAU45ZTM126IKL'
a=[]
j=0
while j<len(str):
    if str[j].isdigit():
        c=j
        k=j+1
        while str[k].isdigit():

            j+=1
            k+=1
        if str[c-1] not in vowel or  str[k] in vowel:
            a.append(int(str[c:k]))

    j+=1

print(a)
c=0
for l in a:
    c+=l
print(c)
