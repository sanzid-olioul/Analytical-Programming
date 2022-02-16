import math
n = int(input())
for i in range(n):
    inp = int(input())
    lst = [int(x) for x in input().split()]
    me = 0
    je = 0
    for j in range(inp):
        me+= math.ceil((lst[j]+1)/30) * 10
        je+= math.ceil((lst[j]+1)/60) * 15
    
    if me < je :
        print("Case {inc}: Mile {dta}".format(inc = i+1,dta = me))
    elif me > je :
        print("Case {inc}: Juice {dta}".format(inc = i+1,dta = je))
    else:
        print("Case {inc}: Mile Juice {dta}".format(inc = i+1,dta = je))