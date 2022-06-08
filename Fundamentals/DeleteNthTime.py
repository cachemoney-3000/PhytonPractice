def delete_nth(order, max_e):
    result = []
    occurence = {}

    for element in order:
        count = occurence.setdefault(element, 0)
        if count >= max_e:
            continue

        result.append(element)
        occurence[element] += 1

    return result


print(delete_nth([1,1,3,3,7,2,2,2,2], 3))
