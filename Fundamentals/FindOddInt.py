def find_it(seq):
    counter = 0
    seq = sorted(seq)
    print(seq)
    i = 0
    while i < len(seq):
        num = seq[i]
        while i < len(seq) and num == seq[i]:
            num = seq[i]
            i += 1
            counter += 1

        if counter % 2 != 0:
            return num
        else:
            counter = 0

    return -1


print(find_it([10]))
