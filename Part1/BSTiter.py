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




# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNodeIter(root, key):
    while root is not None:
        # If the key to be deleted is smaller than the root's
        # key then it lies in  left subtree
        if key < root.val:
            root = root.left

        # If the kye to be delete is greater than the root's key
        # then it lies in right subtree
        elif (key > root.val):
            root = root.right

        # If key is same as root's key, then this is the node
        # to be deleted
        else:

            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = findMinIter(root.right)

            # Copy the inorder successor's content to this node
            root.val = temp.val

            # Delete the inorder successor
            #root.right = deleteNode(root.right, temp.val)
    return root


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



# Driver program to test the above functions
# Let us create the following BST
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80
r = Node(50)
insertIter(r, Node(30))
insertIter(r, Node(20))
insertIter(r, Node(40))
insertIter(r, Node(70))
insertIter(r, Node(60))
insertIter(r, Node(80))
inorder(r)
# Print inoder traversal of the BST
print(findMinIter(r))
print(findMaxIter(r))
print("spacer")
print(findNextIter(r, 55))
print(findPrevIter(r, 45))
#deleteNode(r, 25)
print ("traversal")
inorder(r)

