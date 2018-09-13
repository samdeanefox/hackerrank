"""

Check out the resources on the page's right side to learn more about binary search trees. The video tutorial is by Gayle Laakmann McDowell, author of the best-selling interview book Cracking the Coding Interview.

For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

    The value of every node in a node's left subtree is less than the data value of that node.
    The value of every node in a node's right subtree is greater than the data value of that node.
    The value of every node is distinct.

For example, the image on the left below is a valid BST. The one on the right fails on several counts:
- All of the numbers on the right branch from the root are not larger than the root.
- All of the numbers on the right branch from node 5 are not larger than 5.
- All of the numbers on the left branch from node 5 are not smaller than 5.
- The data value 1 is repeated.

Given the root node of a binary tree, determine if it is a binary search tree.

Function Description

Complete the function checkBST in the editor below. It must return a boolean denoting whether or not the binary tree is a binary search tree.

checkBST has the following parameter(s):

    root: a reference to the root node of a tree to test

Input Format

You are not responsible for reading any input from stdin. Hidden code stubs will assemble a binary tree and pass its root node to your function as an argument.

Constraints

Output Format

Your function must return a boolean true if the tree is a binary search tree. Otherwise, it must return false.

Sample Input

image

Sample Output

Yes

Explanation

The tree in the diagram satisfies the ordering property for a Binary Search Tree, so we print Yes.

"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
    
def checkBST(root, min=0, max=10000):
    if not root:
        return True
    if root.data > min and root.data < max and checkBST(root.left,min,root.data) and checkBST(root.right,root.data,max):
         return True
    else:
         return False