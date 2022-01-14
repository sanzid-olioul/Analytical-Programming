import sys
import queue
que = queue.Queue()
for i in range(97,97+26):
    que.put(chr(i))

dic = dict()
count = 1
for i in range(0,26):
    dic[chr(i+97)] = count
    count+=1

for i in range(0,26):
    for j in range(i+1,26):
        dic[chr(i+97)+chr(j+97)]= count
        count+=1

for i in range(0,26):
    for j in range(i+1,26):
        for k in range(j+1,26):
            dic[chr(i+97)+chr(j+97)+chr(k+97)] = count
            count+=1

for i in range(0,26):
    for j in range(i+1,26):
        for k in range(j+1,26):
            for l in range(k+1,26):
                dic[chr(i+97)+chr(j+97)+chr(k+97)+chr(l+97)] = count
                count+=1
            
for i in range(0,26):
    for j in range(i+1,26):
        for k in range(j+1,26):
            for l in range(k+1,26):
                for m in range(l+1,26):
                        dic[chr(i+97)+chr(j+97)+chr(k+97)+chr(l+97)+chr(m+97)] = count
                        count+=1


# for inp in sys.stdin:
#     if inp:
#         bas = ''
#         for i in inp:
#             bas+=chr(ord(i))
#         print(dic.get(bas,0))
        
while True:
    try:
        inp = input()
        if inp:
            print(dic.get(inp,0))
    except EOFError:
        break
