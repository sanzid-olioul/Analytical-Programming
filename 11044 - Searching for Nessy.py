n = int(input())
while n> 0:
    n-=1
    x,y = (int(i) for i in input().split())
    print((x//3)*(y//3))