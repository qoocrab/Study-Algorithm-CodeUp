total = 0

for _ in range(3):
    a, b = map(float, input().split())
    total += a * b

print(f"{total:.1f}")
