def robber_encode(sentence):
    myString = ''
    for c in sentence:
        if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u') or \
                (c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'):
            myString += c

        elif c.isalpha():
            if 'A' <= c <= 'Z':
                myString += c + 'O' + c
            else:
                myString += c + 'o' + c
        else:
            myString += c

    return myString


print(robber_encode("S.O.S"))
