inp = int(input())
for i in range(inp):
    st = input()
    if st == "1" or st == "4" or  st == "78":
        print("+")
    elif st[-1] == '5' and st[-2] == '3':
        print("-")
    elif st[0] == '1' and st[1] == '9' and st[2]=='0':
        print("?")
    else:
        print("*")