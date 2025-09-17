numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

unique_numbers = sorted(set(numbers))

if len(unique_numbers) < 2:
    print("Недостатньо унікальних чисел для пошуку другого мінімального і максимального.")
else:
    print("Другий мінімальний елемент:", unique_numbers[1])
    print("Другий максимальний елемент:", unique_numbers[-2])