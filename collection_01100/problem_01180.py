n = int(input())
s = int(str(n)[::-1]) * 2

if s >= 100:
    s = int(str(s)[-2:])

print(s)

if s <= 50:
    print("GOOD")
else:
    print("OH MY GOD")
