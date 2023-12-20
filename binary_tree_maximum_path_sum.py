# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
# git add . && git commit -m "completed binary_tree_maximum_path_sum" && git push && exit

import math
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -math.inf

        def helper(current_node):
            nonlocal res
            if current_node is None:
                return 0
            left = helper(current_node.left)
            right = helper(current_node.right)
            res = max(
                res,
                current_node.val + left + right,
                current_node.val + max(0, left, right),
            )
            return current_node.val + max(0, left, right)

        helper(root)
        return res
