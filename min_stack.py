# https://leetcode.com/problems/min-stack/description/
# git add . && git commit -m "completed min_stack" && git push && exit


class Node:
    def __init__(self, val, n=None, p=None) -> None:
        self.val = val
        self.next = n
        self.prev = p


class MinStack:
    def __init__(self):
        self.head = None
        self.min_head = None

    def push(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            self.min_head = Node(val)
        else:
            new_node = Node(val, None, self.head)
            self.head.next = new_node
            self.head = self.head.next
            if val <= self.min_head.val:
                new_node = Node(val, None, self.min_head)
                self.min_head.next = new_node
                self.min_head = self.min_head.next

    def pop(self) -> None:
        if self.top() == self.min_head.val:
            self.min_head = self.min_head.prev
            if self.min_head != None:
                self.min_head.next = None

        self.head = self.head.prev
        if self.head != None:
            self.head.next = None

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.min_head.val
