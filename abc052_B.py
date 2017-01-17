#abc052_B.py
n = input()
s = input()
ans = 0
x = 0
for i in s:
    if i =='I':
        x+= 1
        ans = max(ans,x)
    else:
        x -= 1
    print(ans)
