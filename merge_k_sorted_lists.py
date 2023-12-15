# https://leetcode.com/problems/merge-k-sorted-lists/description/
# git add . && git commit -m "completed merge_k_sorted_lists" && git push && exit


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_list(a: Optional[ListNode], b: Optional[ListNode]):
            new_head = None
            new_tail = None
            while a and b:
                smaller_node = a if a.val < b.val else b
                if new_head == None:
                    new_head = smaller_node
                    new_tail = smaller_node
                else:
                    new_tail.next = smaller_node
                    new_tail = new_tail.next

                if smaller_node == a:
                    a = a.next
                else:
                    b = b.next

            rest = a if a != None else b

            if new_tail:
                new_tail.next = rest
            else:
                new_tail = rest
                new_head = rest
            return new_head

        return_head = None
        for ll in lists:
            return_head = merge_two_list(return_head, ll)

        return return_head
