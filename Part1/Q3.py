def getRandomArray(n):
    import random
    list = []
    while len(list) < n:
        r = random.random()
        if r not in list: list.append(r)
    return list

def getSortedArray(n):
    r = n
    list = []
    while len(list) < n:
        list.append(r)
        r -= 1
    return list

print(getRandomArray(10))
print(getSortedArray(10))