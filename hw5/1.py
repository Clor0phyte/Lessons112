def count_occurrences(data, target):
    count = 0
    for item in data:
        if isinstance(item, list):
            count += count_occurrences(item, target)
        elif item == target:
            count += 1
    return count

example = [1, [2, 1], [1, [1]]]
print(count_occurrences(example, 1))  # результат: 4
