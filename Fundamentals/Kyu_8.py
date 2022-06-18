def high_and_low(numbers):
    numbers = sorted([int(n) for n in numbers.split()])
    return str(numbers[len(numbers) - 1]) + " " + str(numbers[0])


def DNA_strand(dna):
    temp = list(dna)
    for i in range(0, len(dna)):
        if temp[i] == 'A':
            temp[i] = 'T'
        elif temp[i] == 'T':
            temp[i] = 'A'
        elif temp[i] == 'G':
            temp[i] = 'C'
        else:
            temp[i] = 'G'

    return ''.join(map(str, temp))


print(DNA_strand("ATTGC"))
