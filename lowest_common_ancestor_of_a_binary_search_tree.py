# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
# git add . && git commit -m "completed lowest_common_ancestor_of_a_binary_search_tree" && git push && exit


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        # with considering tree as bst
        current_node = root
        while True:
            if current_node.val > p.val and current_node.val > q.val:
                current_node = current_node.left
            elif current_node.val < p.val and current_node.val < q.val:
                current_node = current_node.right
            else:
                return current_node

        # # forgot it is a bst so did for general binary tree
        # found = 0
        # lca: Optional[TreeNode] = None
        # def helper(current_node: Optional[TreeNode], p, q):
        #     nonlocal lca, found
        #     if current_node == None:
        #         return 0
        #     if found == 2:
        #         return 0
        #
        #     local_count = 0
        #     if current_node == p or current_node == q:
        #         found += 1
        #         local_count += 1
        #         if found == 2:
        #             return 1
        #     assert current_node is not None
        #     left_ans = helper(current_node.left, p, q)
        #     right_ans = helper(current_node.right, p, q)
        #
        #     if local_count + left_ans + right_ans == 2 and lca == None:
        #         lca = current_node
        #
        #     return local_count + left_ans + right_ans
        #
        # helper(root, p, q)
        # assert lca is not None
        # return lca
