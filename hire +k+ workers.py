wages/quality:

wages=list(map(int,input('enter the wages: ').split()))
quality=list(map(int,input('enter the quality: ').split()))
expected_wages=[wages[0]]
cost=int(input('enter the cost: '))
for i in range(1,len(wages)-1):
    expected_wages.append(quality[i]*wages[i+1]/quality[i+1])
count=0
for j in expected_wages:
    if j<cost:
        count+=1
print(count)
