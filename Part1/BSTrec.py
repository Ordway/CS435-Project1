# A utility class that represents an individual node in a BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Insert a new node with the given key
def insertRec(root, node):
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insertRec(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insertRec(root.left, node)


# Given a binary search tree and a key, this function
# delete the key and returns the new root
def deleteNode(root, key):

	# If the key to be deleted is smaller than the root's
	# key then it lies in  left subtree
	if key < root.val:
		root.left = deleteNode(root.left, key)

	# If the kye to be delete is greater than the root's key
	# then it lies in right subtree
	elif (key > root.val):
		root.right = deleteNode(root.right, key)

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
		temp = findMinRec(root.right)

		# Copy the inorder successor's content to this node
		root.val = temp.val

		# Delete the inorder successor
		root.right = deleteNode(root.right, temp.val)

	return root


def findNextRec(node, last, value):
    if node is None:
        return last.val
    if (value >= node.val):
        return findNextRec(node.right, last, value)
    elif (value < node.val):
        if node.right is None and node.val < value:
            return last.val
        else:
            last = node
            return findNextRec(node.left, last, value)

def findPrevRec(node, last, value):
    if node is None:
        return last.val
    if (value <= node.val):
        return findPrevRec(node.left, last, value)
    elif (value > node.val):
        if node.left is None and node.val > value:
            return last.val
        else:
            last = node
            return findPrevRec(node.right, last, value)

# findmin
def findMinRec(root):
    if root.left is None:
        return (root.val)
    elif root.left is not None:
        return findMinRec(root.left)


# findmax
def findMaxRec(root):
    if root.right is None:
        return (root.val)
    elif root.right is not None:
        return findMaxRec(root.right)

# A utility function to do inorder traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.val)
        inorder(root.right)


# Driver program to test
#	 50
# /	 \
# 30	 70
# / \ / \
# 20 40 60 80
r = Node(50)
insertRec(r, Node(30))
insertRec(r, Node(20))
insertRec(r, Node(40))
insertRec(r, Node(70))
insertRec(r, Node(60))
insertRec(r, Node(80))
inorder(r)
# Print inoder traversal of the BST
print(findMinRec(r))
print(findMaxRec(r))
print("spacer")
print(findNextRec(r, r, 55))
print(findPrevRec(r, r, 45))
#deleteNode(r, 25)
print ("traversal")
inorder(r)

