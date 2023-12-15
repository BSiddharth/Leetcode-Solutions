# https://leetcode.com/problems/invert-binary-tree/description/
# git add . && git commit -m "completed invert_binary_tree" && git push && exit


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root: Optional[TreeNode]):
            if not (root.left == None and root.right == None):
                left_inverted = helper(root.left)
                right_inverted = helper(root.right)
                root.left = right_inverted
                root.right = left_inverted
            return root

        return helper(root)
