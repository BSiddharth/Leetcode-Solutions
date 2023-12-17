# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# git add . && git commit -m "completed construct_binary_tree_from_preorder_and_inorder_traversal" && git push && exit


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(ps, pe, ist, ie):
            head_node_val = preorder[ps]
            head_index = inorder.index(head_node_val, ist, ie + 1)
            if head_index - ist > 0:
                left_node = helper(ps + 1, ps + head_index - ist, ist, head_index - 1)
            else:
                left_node = None
            if ie - head_index > 0:
                right_node = helper(ps + head_index - ist + 1, pe, head_index + 1, ie)

            else:
                right_node = None

            head_node = TreeNode(head_node_val, left_node, right_node)
            head_node.left = left_node
            head_node.right = right_node
            return head_node

        if len(preorder) == 0:
            return None
        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
