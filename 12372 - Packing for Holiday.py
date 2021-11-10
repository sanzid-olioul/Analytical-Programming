n = int(input())
for i in range(1,n+1):
    x,y,z = (int(j) for j in input().split())
    if x <=20 and y <=20 and z <= 20:
        print('Case {cou}: good'.format(cou = i))
    else:
        print('Case {cou}: bad'.format(cou = i))

    