import sys


def fib(x):
    arr = [0, 1]

    for i in range(2, x + 1):
        arr.append(arr[i - 2] + arr[i - 1])

    return arr[x]


def productFib(prod):
    arr = []
    for i in range(0, sys.maxsize):
        product = fib(i) * fib(i + 1)
        if product > prod:
            arr.append(fib(i))
            arr.append(fib(i + 1))
            arr.append(False)
            break

        elif product == prod:
            arr.append(fib(i))
            arr.append(fib(i + 1))
            arr.append(True)
            break

    return arr


print(fib(5))
print(productFib(1120149658760))
