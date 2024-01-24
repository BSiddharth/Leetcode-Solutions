# https://leetcode.com/problems/binary-tree-right-side-view/description/
# git add . && git commit -m "completed binary_tree_right_side_view" && git push && exit

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level_list = []

        q = deque()
        q.append((root,0))

        last_seen_node_and_level = (None,0)

        while len(q) != 0:
            current_node,current_level = q.popleft()
            if current_node == None:
                continue
            if current_level != last_seen_node_and_level[1]:
                level_list.append(last_seen_node_and_level[0])
            last_seen_node_and_level = (current_node.val,current_level)

            q.append((current_node.left,current_level+1))
            q.append((current_node.right,current_level+1))

        if last_seen_node_and_level[0] != None:
            level_list.append(last_seen_node_and_level[0])
        return level_list
