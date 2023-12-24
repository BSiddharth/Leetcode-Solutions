# https://leetcode.com/problems/clone-graph/description/
# git add . && git commit -m "completed clone_graph" && git push && exit


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        buffer = {}

        def helper(node):
            if not node:
                return node
            if node.val not in buffer:
                buffer[node.val] = Node(node.val)
            for neybur in node.neighbors:
                if neybur.val not in buffer:
                    buffer[neybur.val] = helper(neybur)
                buffer[node.val].neighbors.append(buffer[neybur.val])
            return buffer[node.val]

        return helper(node)
