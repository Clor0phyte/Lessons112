def apply_function(lst, func):
    result = []
    for x in lst:
        result.append(func(x))
    return result
numbers = [1, 2, 3]
squared = apply_function(numbers, lambda x: x**2)
print(squared)  # [1, 4, 9]
