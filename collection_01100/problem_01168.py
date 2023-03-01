birth, gender = input().split()

if gender == "1" or gender == "2":
    print(2012 - int("19" + birth[0:2]) + 1)
else:
    print(2012 - int("20" + birth[0:2]) + 1)
