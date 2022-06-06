def square_sum(numbers):
    sum = 0
    for i in range(0, len(numbers)):
        square = numbers[i] * numbers[i]
        sum = sum + square

    return sum


print(square_sum([-1, -2]))
