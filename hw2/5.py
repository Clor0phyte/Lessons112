a = int(input("First num:"))
b = int(input("Second num:"))

start = min(a, b)
end = max(a, b)

total = sum(range(start, end + 1))

print("Сума чисел від", a, "до", b, "дорівнює:", total)