class TreeNode:
    def __init__(self, val: int):
        self.left = None
        self.right = None
        self.val = val

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if root.val == key:
        return root
    if root.val < key:
        root.right = insert(root.right, key)
    else:
        root.left = insert(root.left, key)
    return root

def inorder_traverse(root):
    if root:
        inorder(root.left)
        print(root.val, end = " ")