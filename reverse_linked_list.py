# https://leetcode.com/problems/reverse-linked-list/description/
# git add . && git commit -m "completed reverse_linked_list" && git push

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # # iteratively
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     prev_node = None
    #     current_node = head
    #     while current_node != None:
    #         next_node = current_node.next
    #         current_node.next = prev_node
    #         prev_node = current_node
    #         current_node = next_node
    #
    #     return prev_node

    # recurively
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node: ListNode) -> ListNode:
            if node != None and node.next != None:
                last_node, reversed_list_head = helper(node.next)
                last_node.next = node
                node.next = None
                return node, reversed_list_head
            else:
                return node, node

        return helper(head)[1]
