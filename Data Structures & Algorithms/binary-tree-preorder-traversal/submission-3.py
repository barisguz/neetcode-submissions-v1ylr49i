# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        tree = []

        def dsf(node): 

            if node is None:
                return
            tree.append(node.val)
            dsf(node.left)
            dsf(node.right)
        dsf(root)
        return tree



