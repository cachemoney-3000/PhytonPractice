def unique_in_order(iterable):
    i = 0
    arr = []
    while i < len(iterable):
        element = iterable[i]
        arr.append(element)
        while i < len(iterable) and element == iterable[i]:
            element = iterable[i]
            print(element)
            i += 1

    return arr


print(unique_in_order('AAAABBBCCDAABBB'))
