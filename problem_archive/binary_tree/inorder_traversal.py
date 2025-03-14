from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()
        
def construct_binary_tree(values: List[int]) -> TreeNode:
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    for i, node in enumerate(nodes):
        if node is not None:
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            if left_child < len(nodes):
                node.left = nodes[left_child]
            if right_child < len(nodes):
                node.right = nodes[right_child]
    return nodes[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret_vals = []
        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)
                ret_vals.append(node.val)
                inorder_traversal(node.right)
        inorder_traversal(root)
        return ret_vals


if __name__ == "__main__":
    S = Solution()
    tree = construct_binary_tree([1, None, 2, 3])
    print(S.inorderTraversal(tree))