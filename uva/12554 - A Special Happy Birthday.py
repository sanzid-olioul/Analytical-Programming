inp = int(input())
str = "Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you".split()
lst = []
for i in range(inp):
    ins = input()
    lst.append(ins)

if inp <= 16:
    cou =0
    for wrd in str:
        print("{nm}: {wer}".format(nm = lst[cou%inp], wer = wrd))
        cou+=1
else:
    flg = inp // 16
    if flg != inp/16:
        flg+=1
    cou =0
    for i in range(flg):
        for wrd in str:
            print("{nm}: {wer}".format(nm = lst[cou%inp], wer = wrd))
            cou+=1
