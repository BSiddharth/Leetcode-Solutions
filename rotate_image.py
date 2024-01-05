# https://leetcode.com/problems/rotate-image/description/
# git add . && git commit -m "completed rotate_image" && git push && exit

class Solution:
    def next(self,pointer,tl,br):
        px = pointer[0]
        py = pointer[1]

        if (px!=tl[0] and py == br[1]):
            return ((px-1,py))
        elif (px == tl[0] and py != tl[0]):
            return ((px,py-1))
        elif (py == tl[0] and px != br[0]):
            return ((px+1,py))
        elif (px == br[0] and py!= br[1]):
            return ((px,py+1))
        return pointer

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(tl,br):
            can_break = False
            p1 = (tl[0],br[1])
            p2 = br
            while True:
                can_break = True
                matrix[p1[0]][p1[1]], matrix[p2[0]][p2[1]] = matrix[p2[0]][p2[1]] , matrix[p1[0]][p1[1]]
                p1 = self.next(p1,tl,br)
                p2 = self.next(p2,tl,br)

                can_break = True
                if can_break and p1 == br:
                    break

            if br[0]-tl[0] > 1:
                helper((tl[0]+1, tl[1]+1),(br[0]-1,br[1]-1))
        helper((0,0),(len(matrix)-1, len(matrix[0])-1))
