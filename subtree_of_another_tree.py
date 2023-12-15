# https://leetcode.com/problems/subtree-of-another-tree/description/
# git add . && git commit -m "completed subtree_of_another_tree" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root: Optional[TreeNode], subRoot: Optional[TreeNode]):
            if not (root or subRoot):
                return True
            if root == None or subRoot == None:
                return False
            if root.val != subRoot.val:
                return False

            return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)

        stack = [root]

        while len(stack) != 0:
            current_node = stack.pop()
            if helper(current_node, subRoot):
                return True
            if current_node != None:
                stack.append(current_node.right)
                stack.append(current_node.left)

        return False
