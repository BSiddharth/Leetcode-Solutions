# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# git add . && git commit -m "completed remove_nth_node_from_end_of_list" && git push && exit


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head
        for _ in range(n - 1):
            right = right.next

        last_left = None
        while right.next != None:
            right = right.next
            last_left = left
            left = left.next
        if last_left != None:
            last_left.next = last_left.next.next

        else:
            head = head.next
        return head
