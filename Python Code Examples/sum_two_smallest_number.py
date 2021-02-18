def sum_two_smallest_numbers(numbers):
    numbers_1 = min(numbers)
    numbers.remove(numbers_1)
    numbers_2 = min(numbers)
    total = numbers_1 + numbers_2
    return total
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))