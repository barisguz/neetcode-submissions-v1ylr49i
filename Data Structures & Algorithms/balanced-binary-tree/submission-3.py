# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ## DFS first, check if the dif between left and right is 1 in total, if it exceeds then return False 

        ## base case will check if the value exists there, and then wil check if the diff is moere than 1 
        def dfs(root):
            if not root:
                return [True,0]
            left,right = dfs(root.left), dfs(root.right)
            balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)
            return[balance, 1+ max(left[1],right[1])]
        return dfs(root)[0]
        