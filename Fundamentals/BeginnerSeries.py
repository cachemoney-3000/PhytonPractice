def past(h, m, s):
    ms = (h * 60 * 60 * 1000) + (m * 60000) + (s * 1000)
    return ms


def sum_array(arr):
    if not arr:
        return 0

    arr.sort()
    total = 0
    for i in range(1, len(arr) - 1):
        total += arr[i]
    return total


sum_array([6, 0, 1, 10, 10])
