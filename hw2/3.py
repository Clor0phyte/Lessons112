n = int(input("Sum of price:"))

d1 = n - (n*0.2)
d2 = n - (n*0.1)

if n >= 5000:
    print(f"with 20% discount all your products cost - {d1}")
elif n >= 1000:
    print(f"with 10% discount all your products cost - {d2}")
else:
    print(f"you dont have discount, price still {n}")