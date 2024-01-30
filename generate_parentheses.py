# https://leetcode.com/problems/generate-parentheses/description/
# git add . && git commit -m "completed generate_parentheses" && git push && exit

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(current_state,open_count,close_count):
            if open_count == close_count == 0:
                result.append(current_state)

            if close_count == 0:
                return

            if open_count != 0:
                helper(current_state+'(',open_count-1,close_count)
            if close_count != 0 and close_count > open_count:
                helper(current_state+')',open_count,close_count-1)

        helper("",n,n)

        return result
