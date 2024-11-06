numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

total = 0
count = len(numbers)
mis_index = numbers.index(None)
for number in numbers:
  if number is not None:
    total += number
average = total / count
numbers[mis_index] = average
print("Измененный список:", numbers)



