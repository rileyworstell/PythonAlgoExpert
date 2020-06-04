"""
The Fibonacci sequence. Write a function that takes
in an integer n and returns the nth Fibonnaci number
"""

def getNthFib(n):
    # Write your code here.
    arr = [0, 1]
	counter = 1
	if n == 1:
		return 0
	elif n == 2:
		return 1
	else:
		while counter <= n:
			if counter == n:
				return arr[0]
			else:
				arr[0], arr[1] = arr[1], (arr[0] + arr[1])
				counter += 1


