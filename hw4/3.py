def classify_numbers(numbers):
    result = {"positive": [], "negative": [], "zero": []}
    
    for num in numbers:
        if num > 0:
            result["positive"].append(num)
        elif num < 0:
            result["negative"].append(num)
        else:
            result["zero"].append
    return result 


print(classify_numbers([2, 0, -10]))