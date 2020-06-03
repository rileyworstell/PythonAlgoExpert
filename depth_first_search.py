"""
You're given a node class that has a name and an array of optional children nodes. 
When put together, nodes form an acyclic tree like structure.
Implement depthFirstsearch on the NOde class.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		array.append(self.name)
		for i in self.children:
			i.depthFirstSearch(array)
		return array
        