t = int(input())

for i in range(t):
    d, s = input().split()
    d = int(d)
    res = ""
    for i in s:
        res += i*d
    print(res)