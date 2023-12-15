# https://leetcode.com/problems/same-tree/description/
# git add . && git commit -m "completed same_tree" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(a: Optional[TreeNode], b: Optional[TreeNode]):
            if a == None and b == None:
                return True

            if not (a != None and b != None):
                return False

            if a.val != b.val:
                return False

            return helper(a.left, b.left) and helper(a.right, b.right)

        return helper(p, q)
