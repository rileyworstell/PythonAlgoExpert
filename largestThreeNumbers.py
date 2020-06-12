## Find the largest 3 numbers.
def findThreeLargestNumbers(array):
    # Write your code here.
    arr = [-10000, -100000, -100000]
    count = 0
    for i in array:
        if count < 3:
            arr[count] = i
            count += 1
            if arr[0] < arr[1]:
                arr[0], arr[1] = arr[1], arr[0]
            if arr[1] < arr[2]:
                arr[1], arr[2] = arr[2], arr[1]
        else:   
            if i >= arr[0]:
                arr[0], arr[1], arr[2] = i, arr[0], arr[1]
            elif i >= arr[1]:
                arr[1], arr[2] = i, arr[1]
            elif i > arr[2]:
                arr[2] = i
	if arr[0] > arr[1]:
		arr[0], arr[1] = arr[1], arr[0]
    if arr[1] > arr[2]:
		arr[1], arr[2] = arr[2], arr[1]
	if arr[0] > arr[1]:
		arr[0], arr[1] = arr[1], arr[0]

    return arr