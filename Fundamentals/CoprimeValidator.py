def are_coprime(n, m):
    gcf = 0
    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcf = i

    return gcf == 1


print(are_coprime(20, 27))
print(are_coprime(12, 39))
