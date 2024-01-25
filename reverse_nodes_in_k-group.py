# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# git add . && git commit -m "completed reverse_nodes_in_k-group" && git push && exit

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current_node = head
        last_visited_node = None
        to_visit = None
        next_segment_last_node = head
        last_segment_last_node = None
        current_segment_last_node = None
        return_set = False
        to_return_node = head

        count = 0 

        while next_segment_last_node != None:
            count += 1
            next_segment_last_node = next_segment_last_node.next

            if count == k:
                current_segment_last_node = current_node
                while current_node != next_segment_last_node:
                    to_visit = current_node.next 
                    current_node.next = last_visited_node
                    if to_visit == next_segment_last_node:
                        if not return_set:
                            return_set = True
                            to_return_node = current_node
                        if last_segment_last_node != None:
                            last_segment_last_node.next = current_node
                        last_segment_last_node = current_segment_last_node
                        last_segment_last_node.next = to_visit

                    last_visited_node = current_node
                    current_node = to_visit

                count = 0

        return to_return_node
