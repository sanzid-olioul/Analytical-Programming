count = 1
while(True):
    bal = 0
    n = int(input())
    if n ==0:
        break
    el = [int(e) for e in input().split()]
    for i in range(0,n):
        if el[i] > 0:
            bal+=1
        else:
            bal-=1
    print('Case {cou}: {bal}'.format(cou = count,bal = bal))
    count+=1
