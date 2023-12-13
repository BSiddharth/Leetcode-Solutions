# https://leetcode.com/problems/merge-two-sorted-lists/description/
# git add . && git commit -m "completed merge_two_sorted_lists" && git push


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        new_list_head = None
        new_list_tail = None

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                next_list1 = list1.next
                if new_list_head == None:
                    new_list_head = list1
                    new_list_tail = list1
                else:
                    new_list_tail.next = list1
                    new_list_tail = new_list_tail.next
                list1 = next_list1

            else:
                next_list2 = list2.next
                if new_list_head == None:
                    new_list_head = list2
                    new_list_tail = list2
                else:
                    new_list_tail.next = list2
                    new_list_tail = new_list_tail.next
                list2 = next_list2

        for rem_list in [list1, list2]:
            while rem_list != None:
                new_list_tail.next = rem_list
                new_list_tail = new_list_tail.next
                rem_list = rem_list.next
        return new_list_head
