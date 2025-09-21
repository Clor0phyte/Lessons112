def calculate_salary(hours_worked, rate, bonus=0):
        return hours_worked*rate + bonus

print(calculate_salary(160, 10, 200))
print(calculate_salary(200, 12))