def is_even(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"


a, b = map(int, input().split())
print(f"{is_even(a)}+{is_even(b)}={is_even(a + b)}")
