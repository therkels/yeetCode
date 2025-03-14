# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode({self.val})"
        
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
