# https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
# git add . && git commit -m "completed count_good_nodes_in_binary_tree" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        result = 0
        def helper(max_till_now,current_node):
            nonlocal result
            if current_node == None:
                return
            if current_node.val >= max_till_now:
                result += 1
                max_till_now = current_node.val

            helper(max_till_now,current_node.left)
            helper(max_till_now,current_node.right)


        helper(root.val,root)
        
        return result
