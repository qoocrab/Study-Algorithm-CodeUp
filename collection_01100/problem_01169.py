n = int(input())

if 2013 - n >= 2000:
    print(int(str(2013 - n)[-2:]), 3)
else:
    print(int(str(2013 - n)[-2:]), 1)
