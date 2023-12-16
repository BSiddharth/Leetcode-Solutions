# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
# git add . && git commit -m "completed kth_smallest_element_in_a_bst" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # little fast
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(current_node, count):
            if current_node == None:
                return count, None

            count, val = helper(current_node.left, count)
            if val != None:
                return count, val
            count += 1
            if count == k:
                return count, current_node.val
            count, val = helper(current_node.right, count)
            if val != None:
                return count, val
            return count, None

        return helper(root, 0)[1]

    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     count = 0
    #     buffer = []
    #     def helper(current_node):
    #         nonlocal buffer
    #         if current_node == None:
    #             return
    #
    #         helper(current_node.left)
    #         buffer.append(current_node.val)
    #         helper(current_node.right)
    #
    #     helper(root)
    #     return buffer[k-1]
