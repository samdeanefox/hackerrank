class Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right

def search(head):
	ptr = head
	array = [ptr]

	while array:
		ptr = array[-1]
		array = array[:-1]
		if ptr.right:
			array.append(ptr.right)
		if ptr.left:
			array.append(ptr.left)
		print ptr.value

node = Node(0)
node.left = Node(1, Node(2), Node(3))
node.right = Node(4, Node(5), Node(6))
node.left.left.left = Node(7, Node(8), Node(9))
node.right.right.right = Node(10, Node(11), Node(12))

search(node)


'''


							0
					  /           \
				    1               4
				/	  \  		 /     \
			   2       3		5       6
			/						     \	
		   7  						      10 
         /  \ 							 /  \
        8    9                          11   12


'''