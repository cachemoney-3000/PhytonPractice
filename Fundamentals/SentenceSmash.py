def smash(words):
    ans = ""
    for i in range(0, len(words)):
        if i == len(words) - 1:
            ans = ans + words[i]
        else:
            ans = ans + words[i] + " "

    return ans


smash(["hello", "amazing", "world"])
