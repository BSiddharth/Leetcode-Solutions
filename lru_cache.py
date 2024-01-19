# https://leetcode.com/problems/lru-cache/description/
# git add . && git commit -m "completed lru_cache" && git push && exit

class Node:
    def __init__(self,val,key,prev = None, next = None) -> None:
        self.val = val
        self.key = key
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ancient = None
        self.recent = None
        self.lookup_dict = {}

    def get(self, key: int) -> int:
        if key in self.lookup_dict:
            to_be_recent = self.lookup_dict[key]
            to_be_recent_val = to_be_recent.val
            if self.recent == to_be_recent:
                return to_be_recent_val
            if self.ancient == to_be_recent:
                self.ancient = to_be_recent.next
            # assert(self.recent != None)
            self.recent.next = to_be_recent
            to_be_recent.next.prev = to_be_recent.prev
            if to_be_recent.prev != None:
                to_be_recent.prev.next = to_be_recent.next

            to_be_recent.next = None
            to_be_recent.prev = self.recent
            self.recent = to_be_recent
            return to_be_recent_val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.lookup_dict:
            self.lookup_dict[key].val = value
            self.get(key)
        else:
            if len(self.lookup_dict) == self.capacity:
                
                # capacity > 0 else self.ancient.val will be None
                # assert(self.ancient != None)
                # assert(self.ancient.val != None)
                del self.lookup_dict[self.ancient.key]
                self.ancient = self.ancient.next
                if self.ancient == None:
                    self.recent = None
                else:
                    self.ancient.prev = None


            new_node = Node(value,key,self.recent)

            if self.recent != None:
                self.recent.next = new_node
                self.recent = new_node
            else:
                self.ancient = new_node
                self.recent = new_node
            
            self.lookup_dict[key] = new_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
