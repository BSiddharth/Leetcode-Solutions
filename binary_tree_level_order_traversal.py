# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# git add . && git commit -m "completed binary_tree_level_order_traversal" && git push && exit

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_list: List[List[int]] = []

        q = deque()

        q.append((root, 0))

        while len(q) != 0:
            current_node, level = q.popleft()
            if current_node == None:
                continue
            if len(return_list) <= level:
                return_list.append([current_node.val])
            else:
                return_list[level].append(current_node.val)

            q.append((current_node.left, level + 1))
            q.append((current_node.right, level + 1))

        return return_list
