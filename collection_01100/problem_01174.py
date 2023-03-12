h, m = map(int, input().split())

hour = list(range(0, 24))
time = h * 60 + m - 30

print(hour[time // 60], time % 60)
