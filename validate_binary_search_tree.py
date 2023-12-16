# https://leetcode.com/problems/validate-binary-search-tree/description/
# git add . && git commit -m "completed validate_binary_search_tree" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(current_node, min_val, max_val):
            if current_node == None:
                return True
            if not (min_val < current_node.val < max_val):
                return False
            if current_node.left != None and current_node.left.val > current_node.val:
                return False
            if current_node.right != None and current_node.right.val < current_node.val:
                return False

            return helper(current_node.left, min_val, current_node.val) and helper(
                current_node.right, current_node.val, max_val
            )

        return helper(root, -math.inf, math.inf)
