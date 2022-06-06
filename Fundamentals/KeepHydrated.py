# Nathan drinks 0.5 liters per hour
# Round to the smallest number
import math


def litres(time):
    liters = 0
    while time >= 1:
        time = time - 1
        liters = liters + 0.5

    liters = math.floor(liters)
    return liters


#print(math.floor(0.5))
print(litres(1.4))
