numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Индекс пропущеного числа
index_none = numbers.index(None)
average = sum(y for y in numbers if y is not None) / (len(numbers))
numbers[index_none] = average
average = round(average, 2)

print("Измененный список:", numbers)
