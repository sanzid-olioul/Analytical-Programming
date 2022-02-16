inp = int(input())
while inp:
    inp-=1
    nmb = int(input())
    lst = []
    for i in range(nmb):
        lst.append(input())
    out = 0
    for i in range(nmb):
        if lst[i] == 'LEFT':
            out-=1
        elif lst[i] == 'RIGHT':
            out+=1
        else:
            ls = int(lst[i].split()[-1])-1
            lst[i] = lst[ls]
            if lst[i] == 'LEFT':
                out-=1
            elif lst[i] == 'RIGHT':
                out+=1
    print(out)