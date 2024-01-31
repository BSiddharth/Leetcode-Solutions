# https://leetcode.com/problems/balanced-binary-tree/description/
# git add . && git commit -m "completed balanced_binary_tree" && git push && exit

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):

        def helper(root):
            if root == None:
                return (0,True)
            
            left_height,left_is_balanced = helper(root.left)
            right_height,right_is_balanced = helper(root.right)

            return ((left_height + 1 ) if left_height > right_height else (right_height + 1), left_is_balanced and right_is_balanced and  -1 <= left_height - right_height <= 1)
        
        return helper(root)[1]
