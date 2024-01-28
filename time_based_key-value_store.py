# https://leetcode.com/problems/time-based-key-value-store/description/
# git add . && git commit -m "completed time_based_key-value_store" && git push && exit

class TimeMap:

    def __init__(self):
        self.db = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.db:
            self.db[key] = []
        
        self.db[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.db:
            return ""

        left = 0
        right = len(self.db[key]) - 1

        if timestamp >= self.db[key][-1][0]:
            return self.db[key][-1][1]
        elif timestamp < self.db[key][0][0]:
            return ''

        while left < right:
            mid = (left+right)//2
            if self.db[key][mid][0] < timestamp:
                left = mid + 1
            elif self.db[key][mid][0] > timestamp:
                right = mid - 1
            else:
                return self.db[key][mid][1]

        if self.db[key][left][0] == timestamp:
            return self.db[key][left][1]
        elif self.db[key][left][0] < timestamp:
            return self.db[key][left][1]
        elif self.db[key][left][0] > timestamp:
            if left == 0:
                return ''
            else:
                return self.db[key][left-1][1]
        
    
