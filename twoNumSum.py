"""
Write a function that takes in a non-empty array of distinct integers and an integer
representing a target sum. If any two numbers in the input array sum up to the target sum, the 
function should return them in an array, in any order. If not two numbers sum up to the target sum,
the function should return an empty array.
Note that the target sum has to be obtained by summing two different integers in the array; you can't add a single integer
to itself in order to obtain the target sum.
You can assume there will be at most one pair of numbers summing up to the target sum.
"""

class Car:
    def __init__(self, year):
        self.color = "Red"
        self.year = year


Mustang = Car(1997)

print(Mustang.color)
print(Mustang.year)


dict1 = {
    "brand": "Nike",
    "color": "Red"
}

mydict = dict1
print(mydict["brand"])


arr = [[x for x in range(10)] for _ in range(10)]
print(arr)