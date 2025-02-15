numbers = [1, 2, 3, 4, 5]
if len(numbers) == 0:
    result =[[],[]]
elif len(numbers) % 2 == 0:
    mid = len(numbers) // 2
    result = [numbers[0:mid], numbers[mid:]]
else:
    mid = len(numbers) // 2 + 1
    result = [numbers[0:mid], numbers[mid:]]
print(result)