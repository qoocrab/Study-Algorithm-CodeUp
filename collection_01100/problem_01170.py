g, c, n = map(int, input().split())

if n < 10:
    print(str(g) + str(c) + "0" + str(n))
else:
    print(str(g) + str(c) + str(n))
