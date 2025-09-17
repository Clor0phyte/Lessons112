numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

unique_numbers = sorted(set(numbers))

avg = sum(unique_numbers) / len(unique_numbers)
print("Середнє арифметичне унікальних чисел:", avg)

