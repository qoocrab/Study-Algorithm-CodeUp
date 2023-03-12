h, m = map(int, input().split())

time = h * 60 + m - 30

if time < 0:
    time = time + 24 * 60

print(time // 60, time % 60)
