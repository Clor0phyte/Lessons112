a = int(input("Number:"))

if a % 3 == 0 and a % 5 == 0:
    print(f"fizz buzz")
elif a % 3 == 0:
    print(f"fizz")
elif a % 5 == 0:
    print(f"buzz")
elif a <= 0:
    print(f"try again")