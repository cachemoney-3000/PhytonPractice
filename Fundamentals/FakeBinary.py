def fake_bin(x):
    result = ""
    for i in x:
        num = int(i)
        if num < 5:
            result = result + '0'

        else:
            result = result + '1'

    return result

fake_bin("45385593107843568")
