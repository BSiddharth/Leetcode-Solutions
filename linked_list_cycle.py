# https://leetcode.com/problems/linked-list-cycle/description/
# git add . && git commit -m "completed linked_list_cycle" && git push && exit


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast != None:
            slow = slow.next
            if fast.next == None:
                return False
            fast = fast.next.next

            if slow == fast:
                return True
        return False
