# https://leetcode.com/problems/reorder-list/description/
# git add . && git commit -m "completed reorder_list" && git push && exit


# Definition for singly-linked list.
from collections import deque
from typing import Deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        node_stack: Deque = deque()

        start = head
        end = head

        while end != None and end.next != None:
            end = end.next.next
            start = start.next

        while start != None:
            node_stack.append(start)
            start = start.next

        current_node = head

        while len(node_stack) != 0:
            popped_node = node_stack.pop()

            popped_node.next = current_node.next
            current_node.next = popped_node
            current_node = popped_node.next

        current_node.next = None
