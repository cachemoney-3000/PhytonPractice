def vowel_indices(word):
    vowelIndex = []
    if len(word) == 0:
        return vowelIndex

    else:
        word = word.lower()

        for i in range(0, len(word)):
            if word[i] == 'a' or word[i] == 'e' or word[i] == 'i' \
                    or word[i] == 'o' or word[i] == 'u':
                vowelIndex.append(i + 1)

    return vowelIndex


print(vowel_indices("UNDISARMED"))
