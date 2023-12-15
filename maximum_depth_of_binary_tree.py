# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# git add . && git commit -m "completed maximum_depth_of_binary_tree" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        stack = [(root, 0)]

        while len(stack) != 0:
            current_node, parent_depth = stack.pop()
            if current_node != None:
                ans = max(ans, parent_depth + 1)
                stack.append((current_node.left, parent_depth + 1))
                stack.append((current_node.right, parent_depth + 1))

        return ans
