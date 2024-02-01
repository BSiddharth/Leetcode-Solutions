# https://leetcode.com/problems/k-closest-points-to-origin/description/
# git add . && git commit -m "completed k_closest_points_to_origin" && git push && exit

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k == len(points):
            return points
        
        distance_collection = []

        for point in points:
            distance_collection.append(((point[0]**2) + (point[1]**2),point))

        heapq.heapify(distance_collection)

        result = []

        for _ in range(k):
            result.append(heapq.heappop(distance_collection)[1])
            
        return result
