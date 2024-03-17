n = int(input().strip())
list = list(map(int, input().strip().split()))
count1=0
count2=0
count3=0
for j in range(len(list)):
    if list[j]>0:
        count1+=1
    elif list[j]<0:
        count2+=1
    elif list[j]==0:
        count3+=1
print(count1/n)
print(count2/n)
print(count3/n) 
