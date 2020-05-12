def getRandomArray(n):
    import random
    list = []
    while len(list) < n:
        r = random.random()
        if r not in list: list.append(r)
    return list

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

# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

    # Recursive function to insert key in
    # subtree rooted with node and returns
    # new root of subtree.
    def insert(self, root, key):

        # Step 1 - Perform normal BST
        if not root:
            return TreeNode(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

            # Step 2 - Update the height of the
        # ancestor node
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced,
        # then try out the 4 cases
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)

            # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)

            # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

            # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):

        y = z.right
        T2 = y.left

        # Perform rotation
        y.left = z
        z.right = T2

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def rightRotate(self, z):

        y = z.left
        T3 = y.right

        # Perform rotation
        y.right = z
        z.left = T3

        # Update heights
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))

        # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.height

    def getBalance(self, root):
        if not root:
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.val), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Driver program to test above function

randList = getRandomArray(10000)

myTree = AVL_Tree()
root = None
for i in randList:
    root = myTree.insert(root, i)

print("AVL tree done")

r = Node(0)
for i in randList:
    insertIter(r, Node(i))

print("BST Tree done")


