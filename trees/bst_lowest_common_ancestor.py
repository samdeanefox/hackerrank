"""

You are given pointer to the root of the binary search tree and two values and . You need to return the lowest common ancestor (LCA) of and in the binary search tree.

image
In the diagram above, the lowest common ancestor of the nodes and is the node . Node is the lowest node which has nodes and as descendants.

Function Description

Complete the function lca in the editor below. It should return a pointer to the lowest common ancestor node of the two values given.

lca has the following parameters:
- root: a pointer to the root node of a binary search tree
- v1: a node.data value
- v2: a node.data value

Input Format

The first line contains an integer, , the number of nodes in the tree.
The second line contains space-separated integers representing values.
The third line contains two space-separated integers, and .

To use the test data, you will have to create the binary search tree yourself. Here on the platform, the tree will be created for you.

Constraints




The tree will contain nodes with data equal to and .

Output Format

Return the a pointer to the node that is the lowest common ancestor of and .

Sample Input

6
4 2 3 1 7 6
1 7

image

and .

Sample Output

[reference to node 4]

Explanation

LCA of and is , the root in this case.
Return a pointer to the node.

"""


class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

def lca(root, v1, v2):
    if not root:
        return None
    v1_path = [root]
    v2_path = [root]
    # First traverse to find the two values
    current = root
    while current and current.info != v1:
        if v1 < current.info:
            current = current.left
        elif v1 > current.info:
            current = current.right
        v1_path.append(current)
    if not current:
        return None
    current = root
    while current and current.info != v2:
        if v2 < current.info:
            current = current.left
        elif v2 > current.info:
            current = current.right
        v2_path.append(current)
    if not current:
        return None
    
    # Now find the ancestor
    for v1_item in reversed(v1_path):
        if v1_item in v2_path:
            return v1_item
        
    return None

tree = BinarySearchTree()
t = int(raw_input())

arr = list(map(int, raw_input().split()))

for i in xrange(t):
    tree.create(arr[i])
    
v = list(map(int, raw_input().split()))

ans = lca(tree.root, v[0], v[1])
print ans.info