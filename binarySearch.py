def binarySearch(array, target):
    newArr = {}
    for keys, values in enumerate(array):
        newArr[values] = keys
    try:
        return newArr[target]
    except:
        return -1
