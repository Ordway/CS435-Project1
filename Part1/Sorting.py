# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Insert a new node with the given key
def insertIter(root, node):
    while root is not None:
        if root.val < node.val:
            if root.right is None:
                root.right = node
                break
            else:
                root =root.right

        else:
            if root.left is None:
                root.left = node
                break
            else:
                root = root.left







def findNextIter(node, value):
    while node is not None:
        if (value >= node.val):
            if node.right is None:
                return node.val
                break
            else:
                node = node.right
        elif (value < node.val):
            if node.left is None:
                return node.val
                break
            else:
                node = node.left

def findPrevIter(node, value):
    while node is not None:
        if (value <= node.val):
            if node.left is None:
                return node.val
                break
            else:
                node = node.left
        elif (value > node.val):
            if node.right is None:
                return node.val
                break
            else:
                node = node.right

# findmin
def findMinIter(root):
    while root is not None:
        if root.left is None:
            return (root.val)
        else:
            root = root.left


# findmax
def findMaxIter(root):
    while root is not None:
        if root.right is None:
            return (root.val)
        else:
            root = root.right

# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.val)
        inorder(root.right)

def sort(r, list):
    length = len(list)
    r = Node(list[0])
    i = 1
    while i < length:
        insertIter(r, Node(list[i]))
        i += 1
    inorder(r)


# Driver program to test the above functions
# Let us create the following BST
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80
list = [111,2,30,4,50,60,7]
r = Node(None)
sort(r, list)



